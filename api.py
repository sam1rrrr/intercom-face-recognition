import requests

class Intercom:
    def __init__(self):
        self.stream_url = 'https://video14.sputnik.systems/5da8b494-7f6e-45f1-b0f7-8e784b55415a/video1.ts'


    def open_door(self):
        url = 'http://api.mobile.gorod.sputnik.systems/api/mobile/v2/devices/30aeea0e-6fbf-4a28-bcb1-ecbc45e6a8ca/open_door'

        headers = {
            "jwt": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0NjY3MzcsInNlc3Npb24iOjQ2OTQwNiwiZXhwaXJhdGlvbiI6MTYzOTUwNTYzN30.Cn9vl4oYH4cBkMqVR2cE4-wtQ4dyXMNvttsk4N8YCsE",
            "Host": "api.mobile.gorod.sputnik.systems",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.0"
        }

        r = requests.post(url, headers=headers)

        return r.json()