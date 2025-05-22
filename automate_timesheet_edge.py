from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os

# Load credentials from environment variables
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Set up Edge WebDriver
driver = webdriver.Edge()

try:
    # Navigate to the timesheet URL
    driver.get("https://mytime.thomsonreuters.com/mytime/WeeklyView.htm")

    # Input credentials and login
    print(f"Using Username: {username}")
    print(f"Using Password: {'******' if password else 'Not provided'}")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "signOnButton").click()

    # Wait for PingID approval and page load with retry logic
    print("Waiting for PingID approval and page load...")
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        time.sleep(30)  # Wait for authentication
        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        
        # Check if we need to navigate to Weekly View
        if "MyTimeHome.htm" in current_url:
            print("Successfully authenticated, at MyTimeHome page")
            time.sleep(5)  # Wait for page to fully load
            break
        elif "FORBIDDEN" in current_url or "auth" in current_url:
            print("Authentication in progress, retrying...")
            driver.get("https://mytime.thomsonreuters.com/mytime/WeeklyView.htm")
            retry_count += 1
            time.sleep(5)
        else:
            print("Checking current page...")
            time.sleep(5)
            
    if retry_count >= max_retries:
        print("Failed to authenticate after multiple attempts")
        raise Exception("Authentication failed")

    # Locate and click on the "Weekly View" button or link
    print("Navigating to Weekly View...")
    try:
        weekly_view_button = driver.find_element(By.LINK_TEXT, "Weekly View")
        weekly_view_button.click()
        time.sleep(5)  # Wait for the Weekly View page to load
        print("Weekly View page loaded.")
    except Exception as e:
        print("Failed to navigate to Weekly View:", e)

    try:
        found_date = False
        while not found_date:
            # Check the date range header
            header_element = driver.find_element(By.ID, "txtHeaderDteRange")
            header_text = header_element.text
            print(f"Checking date range: {header_text}")
            
            # Get target date before starting the loop
            if not 'target_date' in locals():
                target_date = input("Enter the target date (e.g., 'Jun 1'): ").strip().lower()
                print(f"Looking for week containing {target_date}...")

            # Convert header text to lowercase for comparison
            header_text_lower = header_text.lower()
            print(f"Current week: {header_text}")
            
            # Check if the target date is in the header
            # Split the target date into month and day
            target_parts = target_date.split()
            if len(target_parts) == 2:
                target_month, target_day = target_parts
                # Parse the date range from header (e.g., "Week of Jun 8 - Jun 14, 2025 (Week 24)")
                # Extract start and end dates
                date_range = header_text.split("Week of ")[1].split(",")[0]  # Get "Jun 8 - Jun 14"
                start_date, end_date = date_range.split(" - ")  # Split into "Jun 8" and "Jun 14"
                
                # Extract month and day from start and end dates
                start_month, start_day = start_date.strip().split(" ")
                end_month, end_day = end_date.strip().split(" ")
                
                # Convert days to integers for comparison
                start_day = int(start_day)
                end_day = int(end_day)
                target_day = int(target_day)
                
                # Check if months match and day is in range
                if (start_month.lower() == target_month.lower() and start_day <= target_day <= end_day):
                    print(f"Found the week containing {target_date}!")
                    found_date = True
                else:
                    print("Target date not found in current week, clicking Next...")
                    # Click the "Next" button to navigate to the next week
                    next_button = driver.find_element(By.ID, "date_next_button")
                    next_button.click()
                    time.sleep(3)  # Wait for page to update
                    continue  # Skip the rest and continue to next iteration
            
            # Only proceed with filling timesheet if we found the correct week
            if found_date:
                
                # Fill the timesheet for both projects
                print("Filling timesheet fields with 4.0 hours for both projects...")
                
                # Fill hours from Monday to Friday using indices 2-6
                print("Filling hours for RKH-RST-Fedramp-ND...")
                for i in range(2, 7):  # Monday to Friday (using indices 2-6)
                    field_id = f"timecards[0].days[{i}].hours"
                    input_field = driver.find_element(By.ID, field_id)
                    input_field.clear()
                    input_field.send_keys("4.0")
                    time.sleep(1)  # Brief pause between inputs
                    print(f"Filled day {i} with 4.0 hours for first project")

                # Second project (RKH-Westlaw US Gen AI-DA)
                print("Filling hours for RKH-Westlaw US Gen AI-DA...")
                for i in range(2, 7):  # Monday to Friday (using indices 2-6)
                    field_id = f"timecards[2].days[{i}].hours"
                    input_field = driver.find_element(By.ID, field_id)
                    input_field.clear()
                    input_field.send_keys("4.0")
                    time.sleep(1)  # Brief pause between inputs
                    print(f"Filled day {i} with 4.0 hours for second project")
                
                # Save the timesheet
                print("Saving timesheet...")
                save_button = driver.find_element(By.ID, "submitProjectChanges")
                save_button.click()
                time.sleep(3)  # Wait for save to complete
                print("Timesheet saved successfully")
                break
            
            # If not the correct week, click Next
            next_button = driver.find_element(By.ID, "date_next_button")
            next_button.click()
            time.sleep(3)  # Wait for page to update
            
    except Exception as e:
        print(f"An error occurred: {e}")
    # Add logic here to locate and populate timesheet fields
    driver.save_screenshot("login_debug.png")
    # Log any error messages on the page
    try:
        error_message = driver.find_element(By.CLASS_NAME, "ping-error").text
        print(f"Error Message: {error_message}")
    except Exception as e:
        print("No error message found on the page.")

    print(f"Current URL after login attempt: {driver.current_url}")

finally:
    # Close the browser
    driver.quit()
