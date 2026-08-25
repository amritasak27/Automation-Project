@echo off
REM Generate a static Allure HTML report and open it (requires allure commandline on PATH)
allure generate reports\allure-results -o reports\allure-report --clean
allure open reports\allure-report
pause
