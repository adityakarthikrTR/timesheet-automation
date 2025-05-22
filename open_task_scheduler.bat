@echo off
echo Opening Windows Task Scheduler...
taskschd.msc
echo.
echo Please follow these steps:
echo 1. Look for "Weekly_Timesheet_Automation" in the Task Scheduler Library
echo 2. Right-click on it and select "Properties"
echo 3. Go to the "Conditions" tab
echo 4. Check "Wake the computer to run this task"
echo 5. Click "OK" to save changes
pause
