import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from flask import Flask, request, jsonify
import google.generativeai as palm
import webbrowser
from dotenv import load_dotenv
load_dotenv()

save_folder = os.getenv('save_folder')
app = Flask(__name__)

def get_latest_file_in_directory(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def run_info_py():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://astica.ai/vision/object-detection/")

    upload_image_button_xpath = "/html/body/div[2]/div[3]/div[16]/div/div/div[1]/div[1]/div/span"
    upload_image_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, upload_image_button_xpath))
    )
    upload_image_button.click()

    upload_file_input_xpath = "/html/body/div[2]/div[3]/div[7]/div/div/div[2]/div/div/input"
    upload_file_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, upload_file_input_xpath))
    )
    path_to_img = get_latest_file_in_directory(save_folder)
    upload_file_input.send_keys(path_to_img)

    analyze_button_xpath = "/html/body/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div[1]/table[2]/tbody[3]/tr[1]/td[3]/button[1]"
    analyze_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, analyze_button_xpath))
    )
    driver.execute_script("arguments[0].click();", analyze_button)

    output_text_xpath = "/html/body/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[4]/div[2]/p"
    output_text_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, output_text_xpath))
    )
    time.sleep(10)
    text = output_text_element.text

    driver.quit()

    return text

def run_search_py(description):
    os.environ['API_KEY'] = 'AIzaSyBZShnCDwXE3tt-0WnwiWmGVx-8JSacSTw'

    palm.configure(api_key=os.environ['API_KEY'])

    prompt = f"Extract the main object a user might be interested in purchasing from the following description, just give the object no other context: {description}"

    response = palm.generate_text(prompt=prompt)

    if response and response.result:
        generated_text = response.result
    else:
        generated_text = "No response or empty result."

    search_query = generated_text.replace(' ', '+')
    amazon_search_url = f"https://www.amazon.in/s?k={search_query}"

    try:
        webbrowser.open_new_tab(amazon_search_url)
        return f"Opened Amazon search for: {generated_text}"
    except Exception as e:
        return f"Failed to open Amazon search: {e}"

@app.route('/Find_Object', methods=['POST'])
def find_object():
    description = run_info_py()
    result = run_search_py(description)
    return jsonify({"description": description, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
