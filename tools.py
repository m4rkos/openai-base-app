import datetime
import json
import os
import uuid
import shutil
import requests


class Tools:
    def save_info(self, data):
        timex = datetime.datetime.now()
        path = f'logs/{str(timex.strftime("%d-%m-%Y"))}.json'

        if not os.path.exists('logs'):
            os.makedirs('logs')

        data = bytes(json.dumps(data).encode("utf-8"))
        # print(data)

        try:
            file_data = open(path, "ab")
            file_data.write(data)
            file_data.close()
        except IOError:
            file_data = open(path, "wb")
            file_data.write(data)
            file_data.close()


    def save_prompt_images(self, data, images, text_prompt):
        timex = datetime.datetime.now()
        
        folder = str(text_prompt).replace(" ", "_").lower().lstrip()
        path = f'images/{folder}'

        if not os.path.exists(path):
            os.makedirs(path)

        json_data = f'/{str(timex.strftime("%d-%m-%Y"))}.json'
        data = bytes(json.dumps(data).encode("utf-8"))
        
        try:
            file_data = open(path + json_data, "ab")
            file_data.write(data)
            file_data.close()
        except IOError:
            file_data = open(path + json_data, "wb")
            file_data.write(data)
            file_data.close()

        for img in images:
            res = requests.get(img['url'], stream = True)
            with open(path + '/' + str(uuid.uuid4()) + '.png', 'wb') as f:
                shutil.copyfileobj(res.raw, f)


    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
