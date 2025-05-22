# Automated Timesheet Filler

Automatically fill MyTime timesheets every Friday with pre-configured project hours.

## Features

- 🕒 Automatic weekly timesheet filling
- 📅 Runs every Friday at 11:00 AM
- 💤 Can wake computer from sleep
- 🔄 Handles missed executions if computer was off
- 🔐 Secure credential management using .env file

## Installation

1. Clone this repository:
```bash
git clone [your-repo-url]
cd automated-timesheet
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a .env file with your credentials:
```bash
USERNAME=your_username
PASSWORD=your_password
```

## Setup

1. Schedule the task:
```bash
.\schedule_timesheet.bat
```

2. Configure wake settings:
```bash
.\open_task_scheduler.bat
```
Then follow the on-screen instructions to enable "Wake computer to run this task"

## Usage

The script will run automatically every Friday at 11:00 AM. For manual execution:

```bash
# Normal execution (only on Fridays)
python automate_timesheet_edge1.py

# Force execution on any day
python automate_timesheet_edge1.py --force
```

## Project Structure

- `automate_timesheet_edge1.py`: Main script that fills the timesheet
- `schedule_timesheet.bat`: Windows Task Scheduler setup
- `open_task_scheduler.bat`: Helper to configure wake settings
- `.env`: Credentials file (not included in repository)
- `requirements.txt`: Python dependencies
- `timesheet_log.txt`: Execution log (created automatically)

## How It Works

1. Automatically runs every Friday at 11:00 AM
2. Logs into MyTime using your credentials
3. Navigates to the current week
4. Fills Monday-Friday with:
   - 4 hours for RKH-RST-Fedramp-ND
   - 4 hours for RKH-Westlaw US Gen AI-DA
5. Saves the timesheet
6. Logs successful execution

## Security Notes

- Credentials are stored locally in .env file
- .env file is excluded from git repository
- Task runs with user privileges only

## Troubleshooting

1. If the script doesn't run at scheduled time:
   - Check Task Scheduler for any error messages
   - Verify computer was not shut down
   - Ensure network connectivity

2. If authentication fails:
   - Verify credentials in .env file
   - Check network connectivity
   - Ensure PingID is accessible

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use and modify as needed.
