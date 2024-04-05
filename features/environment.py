from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities import ConfigReader


def before_scenario(context, driver):
    options = Options()
    # options.binary_location = "/usr/bin/google-chrome-stable"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_config("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()
