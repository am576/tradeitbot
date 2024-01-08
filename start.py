from selenium import webdriver
# import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import chromedriver_binary  # Adds chromedriver binary to path
import time
import os

driver = None
actions = None

def find_chromedriver():
    bin_dir = './bin'
    for root, dirs, files in os.walk(bin_dir):
        if 'chromedriver.exe' in files:
            return os.path.join(root, 'chromedriver.exe')
    return None

def initBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.200 Safari/537.36")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    
    # options.binary_location =".bin/browser\\chrome.exe"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    driver.get("https://tradeit.gg/")
    wait = WebDriverWait(driver, 10)
    
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//header[not(contains(@class, 'mobile'))]//button[contains(@class, 'login-btn')]")))
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//header[not(contains(@class, 'mobile'))]//button[contains(@class, 'login-btn')]")))
    
    actions.move_to_element(login_button).click().perform()

    login_field = wait.until(EC.presence_of_element_located(('input[class*="newlogindialog_TextInput"][type="text"]')))
    password_field = wait.until(EC.presence_of_element_located(('input[class*="newlogindialog_TextInput"][type="password"]')))




def main():
    initBrowser()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass