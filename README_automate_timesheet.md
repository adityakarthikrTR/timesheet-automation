# Automated Timesheet Script

## Features
- Automatically fills timesheet for the current week
- Runs every Friday (with manual override option)
- Splits 8 hours between two projects:
  * 4 hours for RKH-RST-Fedramp-ND
  * 4 hours for RKH-Westlaw US Gen AI-DA

## Setup Instructions

1. Ensure you have required dependencies:
```bash
pip install selenium python-dotenv
```

2. Set up .env file with credentials:
```
USERNAME=your_username
PASSWORD=your_password
```

3. Schedule the script to run every Friday:

### Windows Task Scheduler Setup
1. Open Task Scheduler
2. Create a new Basic Task:
   - Name: "Weekly Timesheet Automation"
   - Trigger: Weekly, Friday
   - Action: Start a program
   - Program/script: `python`
   - Arguments: `"path_to_script\automate_timesheet_edge1.py"`
   
## Usage

### Automatic Mode
- The script will run automatically every Friday when scheduled
- It will fill the current week's timesheet

### Manual Override
To run the script on any day:
```bash
python automate_timesheet_edge1.py --force
```

## Error Handling
- The script creates a screenshot named "login_debug.png" if any errors occur
- Check the console output for detailed error messages
- The script will only proceed with timesheet filling on Fridays unless the --force flag is used

## Notes
- The script requires Microsoft Edge browser
- Ensure PingID authentication is handled promptly when the script runs
- The script assumes a standard Monday to Friday work week
- Each day is filled with 8 hours total (4 hours per project)
