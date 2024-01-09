import eel
import random
from datetime import datetime
import time
from web.web_controller import Webcontroller

class UI:

    def __init__(self):
        eel.init('web')
        self.wc = Webcontroller()
        self.wc.initBrowser()

    def test_selenium(self):
        self.wc.openPage("https://google.com")

    @eel.expose
    def get_random_name():
        eel.prompt_alerts('Random name')

    @eel.expose
    def get_random_number():
        eel.prompt_alerts(random.randint(1, 100))

    @eel.expose
    def get_date():
        eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    @eel.expose
    def get_ip():
        eel.prompt_alerts('127.0.0.1')

    def start(self):
        eel.start('index.html')

ui = UI()
ui.start()
@eel.expose
def test_selenium():
    ui.test_selenium()