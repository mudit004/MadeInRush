
# Screenshot Capture / Browser Extension

# Features

- Secure by design
- Capture Viewport
- Crop and Save (automatic save)
- Crop and Wait (manual save)
- Configurable Keyboard Shortcut
- Save screenshot as PNG or JPG image file
- Copy screenshot to clipboard as Data URL String or Binary Image
- Preserve or downscale screenshot size on HDPI displays like Retina
- Unique screenshot date/time file name
- No special permissions required

# Options

1. Pin the extension to your browser toolbar
2. Click on the extension button using your **Right** Mouse Button
3. Select `Options` from the context menu

# Table of Contents

- **[Capture Method](#capture-method)**
- **[Image Format](#image-format)**
- **[Build](#build)**

# Capture Method

#### **`Crop and Save`**

1. Activate the extension by using the [keyboard shortcut](#keyboard-shortcut) or by clicking on the extension button
2. Hold down your left mouse button anywhere on the page and drag your mouse in any direction
3. Release the mouse button when you are ready, the selected area will be cropped

# Image Format

- **`PNG`** - better image quality but larger file size. Best suited for cropping and capturing simple web pages

- **`JPG`** - smaller file size with slightly lower image quality. Useful when capturing the entire screen area especially with lots of images on screen or when capturing still shots of videos. The quality of the JPEG can be adjusted from 100 to 0 (highest to lowest)

## Build

1. Clone this repository
2. Execute `sh build/package.sh chrome`
3. Navigate to `chrome://extensions`
4. Make sure that the `Developer mode` switch is enabled
5. Click on the `Load unpacked` button and select the cloned directory


  [chrome]: https://chromewebstore.google.com/detail/screenshot-capture/giabbpobpebjfegnpcclkocepcgockkc
