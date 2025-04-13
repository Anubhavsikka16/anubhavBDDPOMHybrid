rm -rf allureReports/*
behave --no-capture -f  allure_behave.formatter:AllureFormatter -o AllureReports
allure serve AllureReports