import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Replace with the path to your WebDriver (e.g., chromedriver.exe)
WEBDRIVER_PATH = "path/to/your/webdriver"

# Replace with your timesheet URL
TIMESHEET_URL = "https://mytime.thomsonreuters.com/"

# Replace with your login credentials
USERNAME = "your_username"
PASSWORD = "your_password"

def fill_timesheet():
    # Initialize the WebDriver
    driver = webdriver.Chrome(WEBDRIVER_PATH)
    
    try:
        # Open the timesheet URL
        driver.get(TIMESHEET_URL)
        
        # Wait for the page to load
        time.sleep(5)
        
        # Log in (update selectors as per the login page structure)
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
        
        # Wait for the dashboard to load
        time.sleep(5)
        
        # Fill the timesheet (update selectors as per the timesheet page structure)
        # Example: Filling Monday's hours
        driver.find_element(By.ID, "monday_hours").send_keys("8")
        driver.find_element(By.ID, "tuesday_hours").send_keys("8")
        driver.find_element(By.ID, "wednesday_hours").send_keys("8")
        driver.find_element(By.ID, "thursday_hours").send_keys("8")
        driver.find_element(By.ID, "friday_hours").send_keys("8")
        
        # Submit the timesheet
        driver.find_element(By.ID, "submit_button").click()
        
        # Wait for confirmation
        time.sleep(5)
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    fill_timesheet()
