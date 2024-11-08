import os
from datetime import datetime

def capture_screenshot(driver, screenshot_name):
    # If no screenshot name is provided, use the current timestamp as the filename
    if screenshot_name is None:
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    else:
        screenshot_name = f"{screenshot_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    # Define the path for saving the screenshot (folder + filename)
    screenshot_folder = os.path.join(os.getcwd(), "Screenshots")

    # Create the Screenshots folder if it doesn't exist
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)

    # Complete screenshot file path
    screenshot_path = os.path.join(screenshot_folder, screenshot_name)

    # Capture the screenshot
    driver.save_screenshot(screenshot_path)

    # Print the path where the screenshot is saved (for debugging purposes)
    print(f"Screenshot saved at: {screenshot_path}")
    return screenshot_path
