from selenium import webdriver
from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
from selenium_stealth import stealth
from sda.steam_guard import SteamGuard
import json
import time
import os
from selenium.webdriver.chrome.service import Service

class Webcontroller:
    def __init__(self):
        self.initBrowser()
        self.sda = SteamGuard()

    def initBrowser(self):
        chrome_driver_path = "ucdriver.exe"
        
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--lang=en-US")
        options.add_argument("--window-size=1280,800")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        service = Service(executable_path='ucdriver.exe')
        self.driver = webdriver.Chrome(service=service,options=options)
        self.actions = ActionChains(self.driver)
        stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            # run_on_insecure_origins= False,
            )

    def openPage(self, url):
        self.driver.get(url)

    def loginToTradeit(self):
        current_dir = os.getcwd()
        target_url = "https://steamcommunity.com/openid/loginform?need_password=1&force=1&goto=%2Fopenid%2Flogin%3Fopenid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.ns_sreg%3Dhttp%253A%252F%252Fopenid.net%252Fextensions%252Fsreg%252F1.1%26openid.sreg_optional%3Dnickname%252Cemail%252Cfullname%252Cdob%252Cgender%252Cpostcode%252Ccountry%252Clanguage%252Ctimezone%26openid.ns.ax%3Dhttp%253A%252F%252Fopenid.net%252Fsrv%252Fax%252F1.0%26openid.ax.mode%3Dfetch_request%26openid.ax.type.fullname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%26openid.ax.type.firstname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%252Ffirst%26openid.ax.type.lastname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%252Flast%26openid.ax.type.email%3Dhttp%253A%252F%252Faxschema.org%252Fcontact%252Femail%26openid.ax.required%3Dfullname%252Cfirstname%252Clastname%252Cemail%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fconnect-tradeit.com%252Fauth%252Fsteam%252Freturn%253FsendTo%253Dhttps%253A%252F%252Ftradeit.gg%252Fapi%252Fv2%252Fsteam%252Flogin%26openid.realm%3Dhttps%253A%252F%252Fconnect-tradeit.com%252F%26openid_mode%3Dcheckid_setup%26nonce%3D2ca8a67ad9494535637ed1b9"
        with open('blank.html', 'w') as f:
            f.write(f'<a href="{target_url}" target="_blank">link</a>')

        self.driver.get(f'file://{current_dir}/blank.html')
        links = self.driver.find_elements(By.XPATH, "//a[@href]")
        time.sleep(5)
        links[0].click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.get("https://tradeit.gg/")
        # login_field = WebDriverWait(self.driver, 300).until(
                        # EC.presence_of_element_located((By.XPATH, "//header[not(contains(@class, 'mobile'))]//button[contains(@class, 'login-btn')]"))
                    # )
        # login_field = WebDriverWait(self.driver, 300).until(
                        # EC.element_to_be_clickable((By.XPATH, "//header[not(contains(@class, 'mobile'))]//button[contains(@class, 'login-btn')]"))
                    # )
        
        # self.actions.move_to_element(login_field).click().perform()
        # self.driver.get("https://steamcommunity.com/openid/loginform?need_password=1&force=1&goto=%2Fopenid%2Flogin%3Fopenid.mode%3Dcheckid_setup%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.ns_sreg%3Dhttp%253A%252F%252Fopenid.net%252Fextensions%252Fsreg%252F1.1%26openid.sreg_optional%3Dnickname%252Cemail%252Cfullname%252Cdob%252Cgender%252Cpostcode%252Ccountry%252Clanguage%252Ctimezone%26openid.ns.ax%3Dhttp%253A%252F%252Fopenid.net%252Fsrv%252Fax%252F1.0%26openid.ax.mode%3Dfetch_request%26openid.ax.type.fullname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%26openid.ax.type.firstname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%252Ffirst%26openid.ax.type.lastname%3Dhttp%253A%252F%252Faxschema.org%252FnamePerson%252Flast%26openid.ax.type.email%3Dhttp%253A%252F%252Faxschema.org%252Fcontact%252Femail%26openid.ax.required%3Dfullname%252Cfirstname%252Clastname%252Cemail%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fconnect-tradeit.com%252Fauth%252Fsteam%252Freturn%253FsendTo%253Dhttps%253A%252F%252Ftradeit.gg%252Fapi%252Fv2%252Fsteam%252Flogin%26openid.realm%3Dhttps%253A%252F%252Fconnect-tradeit.com%252F%26openid_mode%3Dcheckid_setup%26nonce%3D2ca8a67ad9494535637ed1b9")

        login_field = WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class*="newlogindialog_TextInput"][type="text"]'))
                    )
        password_field = WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class*="newlogindialog_TextInput"][type="password"]'))
                    )
        submit_button = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class*="newlogindialog_SubmitButton"][type="submit"]'))
                    )
        login_data = self.getLoginData()
        login_field.send_keys(login_data['SteamLogin'])
        password_field.send_keys(login_data['SteamPassword'])
        self.actions.move_to_element(submit_button).click().perform()
        self.enterMobileCode()
        self.login()
        

    def enterMobileCode(self):
        mobile_code = self.sda.getGuardCode()
        # time.sleep(10)
        inputs = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[class*="segmentedinputs_Input"][type="text"]'))
                    )
        for i, input_element in enumerate(inputs):
            input_element.send_keys(mobile_code[i])

    def login(self):
        button = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id*="imageLogin"][type="submit"]'))
                    )
        login_field = WebDriverWait(self.driver, 300).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id*="imageLogin"][type="submit"]'))
                    )
        self.actions.move_to_element(button).click().perform()

    def getLoginData(self):
        try:
            with open("sda/glebasdpolbf0100.json", "r") as file:
                file_content = file.read()
                lines = file_content.splitlines()
                json_data = {}
                for line in lines:
                    key, value = line.split(":", maxsplit=1)
                    key = key.strip()
                    value = value.strip()
                    json_data[key] = value

                json_object = json.dumps(json_data, indent=4)
                login_data = json.loads(json_object)
                
            return login_data
            
        except FileNotFoundError:
            print(f"File not found: ") 