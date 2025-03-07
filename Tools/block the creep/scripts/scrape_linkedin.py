from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run Chrome in the background
options.add_argument("--disable-gpu")  # Avoid GPU-related errors
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-webrtc")  # Disable WebRTC to avoid STUN errors
options.add_argument("--incognito")  # Run Chrome in incognito mode

driver = webdriver.Chrome(options=options)


try:
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    print("Opened LinkedIn login page...")

    # Wait for the page to load
    time.sleep(3)

    # Find login input fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter credentials (replace with your own)
    username_field.send_keys("your_email@example.com")
    password_field.send_keys("your_password")

    # Submit the form
    password_field.send_keys(Keys.RETURN)
    print("Logged in successfully!")

    # Wait for redirect
    time.sleep(5)

    # Navigate to the profile viewers page
    driver.get("https://www.linkedin.com/me/profile-views/")
    print("Navigated to profile viewers page...")

    # Wait for content to load
    time.sleep(5)

    # Extract profile viewers (modify as needed)
    viewers = driver.find_elements(By.CLASS_NAME, "profile-viewer-class-name")
    for viewer in viewers:
        print("Viewer:", viewer.text)

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
    print("WebDriver closed.")
