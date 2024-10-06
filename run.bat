@echo off
:: Create virtual environment and activate it
python -m venv venv
call venv\Scripts\activate

:: Install required packages
pip install -r requirements.txt

:: Create reports directory if it doesn't exist
if not exist reports (
    mkdir reports
)

:: Run pytest with html report and allure report, specify the browser as chrome
pytest --html=reports\report.html --alluredir=reports .\tests\ --browser=chrome
