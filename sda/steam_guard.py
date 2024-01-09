import os
import time
import hmac
import json
import struct
import base64
import requests
from hashlib import sha1
import glob

class SteamGuard:

    BAR_LEN = 37
    elements = ['-', '\\', '|', '/']
    symbols = '23456789BCDFGHJKMNPQRTVWXY'

    def getQueryTime(self):
        try:
            request = requests.post('https://api.steampowered.com/ITwoFactorService/QueryTime/v0001', timeout=30)
            json_data = request.json()
            server_time = int(json_data['response']['server_time']) - time.time()
            return server_time
        except:
            return 0


    def getGuardCode(self):
        ma_json = self.loadMaFile()
        shared_secret = ma_json['shared_secret']
        code = ''
        timestamp = time.time() + self.getQueryTime()
        _hmac = hmac.new(base64.b64decode(shared_secret), struct.pack('>Q', int(timestamp/30)), sha1).digest()
        _ord = ord(_hmac[19:20]) & 0xF
        value = struct.unpack('>I', _hmac[_ord:_ord+4])[0] & 0x7fffffff
        for i in range(5):
            code += self.symbols[value % len(self.symbols)]
            value = int(value / len(self.symbols))

        return code

    def loadMaFile(self):
        file_pattern = "*.maFile"

        file_path = glob.glob(file_pattern)

        if file_path:
            try:
                with open(file_path[0], "r") as file:
                    json_data = json.load(file)
                    return json_data
            except FileNotFoundError:
                print(f"File not found: {file_path[0]}")
        else:
            print("No .maFile found")