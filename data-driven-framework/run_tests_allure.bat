@echo off
REM Activate your virtualenv first if not active, e.g. .venv\Scripts\activate
pytest %*
if exist reports\allure-results (
  echo Allure results saved to %CD%\reports\allure-results
) else (
  echo No allure-results found
)
pause
