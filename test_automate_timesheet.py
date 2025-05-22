import unittest
from unittest.mock import patch, MagicMock
from automate_timesheet import fill_timesheet

class TestAutomateTimesheet(unittest.TestCase):
    @patch("automate_timesheet.webdriver.Chrome")
    def test_fill_timesheet(self, MockWebDriver):
        # Mock the WebDriver and its methods
        mock_driver = MagicMock()
        MockWebDriver.return_value = mock_driver
        
        # Call the function to test
        fill_timesheet()
        
        # Verify that the WebDriver was initialized and navigated to the URL
        MockWebDriver.assert_called_once_with("path/to/your/webdriver")
        mock_driver.get.assert_called_once_with("https://mytime.thomsonreuters.com/")
        
        # Verify interactions with the login elements
        mock_driver.find_element.assert_any_call("id", "username")
        mock_driver.find_element.assert_any_call("id", "password")
        
        # Verify interactions with the timesheet elements
        mock_driver.find_element.assert_any_call("id", "monday_hours")
        mock_driver.find_element.assert_any_call("id", "submit_button")
        
        # Verify that the browser was closed
        mock_driver.quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
