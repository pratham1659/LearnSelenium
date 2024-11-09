import sys

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities.readProperties import ReadConfig

# Define Chrome options to handle SSL and other configurations
# Disable SSL certificate verification
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")

# Define Edge options (optional, you can add more configurations)
edge_options = Options()
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--incognito")

# Define the `--browser` argument in pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="Specify browser: chrome or firefox"
    )
    parser.addoption(
        "--html-report", action="store", default="HtmlReports/report.html", help="Specify HTML report output file"
    )


@pytest.fixture(scope="function")
def setup_and_teardown(request):

    browser = request.config.getoption("--browser")
    # browser = ReadConfig.get_browser()

    # Initialize the driver based on the browser choice
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(), options=edge_options)
    else:
        raise ValueError("Unsupported browser type")

    driver.maximize_window()
    driver.implicitly_wait(10)

    web_url = ReadConfig.get_url()
    driver.get(web_url)

    yield driver

    driver.quit()


# Hook to capture screenshots on failure and add to the report
def pytest_runtest_makereport(item, call):
    # Only capture screenshots if the test has failed
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get('setup_and_teardown')  # Get the driver from the fixture
        if driver:
            screenshot_dir = "Screenshots"  # Directory where screenshots will be saved
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            screenshot_name = f"{item.nodeid.replace('::', '_')}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

            # Append screenshot path to the report for later use
            item.user_properties.append(("screenshot", screenshot_path))


# Hook to add environment information to the HTML report
def pytest_configure(config):
    html_report = config.getoption("--html-report")
    if not html_report:
        html_report = "HtmlReports/report.html"
    config.option.html = html_report

    # Modify environment information in the HTML report
    config._html = {
        "browser": ReadConfig.get_browser(),
        "browser_version": "95.0",  # You can retrieve this dynamically or statically (e.g., Chrome version)
        "platform": "Windows 10",  # You can retrieve the platform dynamically using `platform.system()` or statically
        "python_version": "3.9",  # You can use `sys.version` or manually define it
        "pytest_version": pytest.__version__,
        "test_framework": "Selenium WebDriver"
    }


# Hook to modify the HTML report title
def pytest_html_report_title(report):
    report.title = "My Selenium Test Report"  # Customize the report title


# Hook to add a custom header to the HTML report (add Screenshot column)
def pytest_html_results_table_header(cells):
    cells.insert(2, "Screenshot")  # Add a Screenshot column after the Status column


# Hook to add screenshots to the report when a test fails
def pytest_html_results_table_row(report, cells):
    # Retrieve the screenshot path from the report's user_properties
    screenshot = None
    for prop in report.user_properties:
        if prop[0] == "screenshot":
            screenshot = prop[1]
            break

    if screenshot:
        # Use relative path for the screenshot to ensure it's correctly displayed in the HTML
        relative_screenshot_path = os.path.relpath(screenshot, start=os.getcwd())
        # Add a clickable screenshot (image thumbnail) to the table
        cells.insert(2,
                     f'<a href="{relative_screenshot_path}" target="_blank"><img src="{relative_screenshot_path}" width="100"/></a>')
    else:
        cells.insert(2, "N/A")  # If no screenshot, show "N/A"


# Optional: This can be used to add custom footer or environment data to the report
def pytest_html_results_summary(prefix, summary, postfix):
    summary.append("<div><b>Environment:</b></div>")
    summary.append(f"<div>Browser: {ReadConfig.get_browser()}</div>")
    summary.append(f"<div>Platform: Windows 10</div>")
    summary.append(f"<div>Python Version: {sys.version}</div>")







