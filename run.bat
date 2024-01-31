@echo off

REM Set the path to the virtual environment
set venv_path=.venv\Scripts\

REM Activate the virtual environment
call %venv_path%\activate.bat

REM You can add any command here
pytest -m "sanity" --html=./reports/report.html tests/ --browser=edge

REM Deactivate the virtual environment
call %venv_path%\deactivate.bat

REM Pause the execution to see the output
pause