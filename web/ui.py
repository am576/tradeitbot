import sqlite3
import eel
import random
from datetime import datetime
import time
import json
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

    def loadItems(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM items")
        data = c.fetchall()

        keys = ['id', 'name', 'price']
        json_data = [dict(zip(keys, row)) for row in data]

        json_string = json.dumps(json_data)
        conn.close()

        return json_string
    
    def saveItems(self, items):
    # Connect to the SQLite database
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()

        # Insert the items into the table
        for item in items:
            name = item['name']
            price = item['price']
            c.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

ui = UI()

@eel.expose
def loadItems():
    items = ui.loadItems()
    eel.createItemRows(items)

@eel.expose
def saveItems(items):
    ui.saveItems(items)

ui.start()