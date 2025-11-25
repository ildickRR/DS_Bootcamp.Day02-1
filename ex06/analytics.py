import sys
from random import randint
import logging
import config
import requests

logging.basicConfig(
    filename="analytics.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)


class Research:
    def __init__(self, path):
        self.path = path
        logging.info("__init__ вызван")


    def file_reader(self, has_header=True):
        try:

            with open(self.path, "r") as file:
                lines = [line.strip() for line in file if line.strip()]

        except FileNotFoundError:
            raise Exception("file not found")

        if not lines:
            raise Exception("file is empty")
      
        if has_header:
            lines = lines[1:]

        data = []
        for line in lines:
            parts = line.split(",")
            if parts not in [["0", "1"], ["1", "0"]]:
                raise Exception("invalid data format")
            data.append([int(parts[0]), int(parts[1])])
        logging.info("file_reader вызван")

        return data


    def send_telegram_message(self, text):
        try:
            url = f"https://api.telegram.org/bot{config.TG_TOKEN}/sendMessage"
            data = {"chat_id": config.TG_CHAT_ID, "text": text}
            requests.post(url, data=data)

            logging.info("Telegram message sent")
        except Exception as e:
            logging.error(f"Telegram error: {e}")

    class Calculations:
        
        def __init__(self, data):
            self.data = data
            logging.info("__init2__вызван")

        def counts(self):
            heads = sum(1 for x in self.data if x == [1, 0])
            tails = sum(1 for x in self.data if x == [0, 1])
            logging.info("counts вызван")
            return (heads, tails)

        
        def fractions(self, heads, tails):
            total = heads + tails
            logging.info("fraction вызван")

            if total == 0:
                return (0, 0)
            else:    
                return (heads / total * 100 , tails / total * 100)

class Analytics(Research.Calculations):

    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            flip = randint(0, 1)
            if flip == 1:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        logging.info("predict_random вызван")
        return predictions  

    def predict_last(self):
        logging.info("predict_last вызван")
        return self.data[-1]

    def save_file(self, data, filename, extension):
        fullname = f"{filename}.{extension}"
        with open(fullname, "w", encoding="utf-8") as file:
            file.write(data)
        
        logging.info("save_file вызван")
        return fullname

            
