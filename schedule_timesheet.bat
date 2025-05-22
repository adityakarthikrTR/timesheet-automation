@echo off
:: Schedule timesheet automation task
echo Setting up weekly timesheet automation...

:: Get the current directory
set "SCRIPT_PATH=%~dp0automate_timesheet_edge1.py"
set "PYTHON_PATH=python"

:: Delete existing task if it exists
SCHTASKS /DELETE /TN "Weekly_Timesheet_Automation" /F 2>nul

:: Create the task with wake and privilege options
SCHTASKS /CREATE /SC WEEKLY /D FRI /TN "Weekly_Timesheet_Automation" /TR "%PYTHON_PATH% %SCRIPT_PATH%" /ST 11:00 /RL HIGHEST /F ^
/DELAY 0001:00 ^
/RU "%USERNAME%" ^
/NP

echo Task scheduled successfully!
echo The timesheet will be filled automatically every Friday at 11:00 AM with the following features:
echo - Will run with highest privileges
echo - Will retry after 1 hour if initial run fails
echo - Will run task as soon as possible if computer was off
echo.
echo To verify the task, open Task Scheduler and look for "Weekly_Timesheet_Automation"
echo Note: For wake from sleep, please configure this in Task Scheduler:
echo 1. Open Task Scheduler
echo 2. Find "Weekly_Timesheet_Automation"
echo 3. Right-click and select Properties
echo 4. Check "Wake computer to run this task"
echo 5. Click OK to save
pause
