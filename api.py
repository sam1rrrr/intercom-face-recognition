import requests

class Intercom:
    def __init__(self):
        self.UUID = ''
        self.JWT_TOKEN = ''
        self.stream_url = ''


    def open_door(self):
        url = f'http://api.mobile.gorod.sputnik.systems/api/mobile/v2/devices/{UUID}/open_door'

        headers = {
            "jwt": self.JWT_TOKEN,
            "Host": "api.mobile.gorod.sputnik.systems",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.0"
        }

        r = requests.post(url, headers=headers)

        return r.json()
