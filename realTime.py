import requests
import random
from  datetime import datetime
from pytz import timezone

fuso = timezone('America/Sao_Paulo')
url = "https://api"
calor = 0
umidade = 0

while calor < 100:
    calor += 1
umidade = random.random()
data = datetime.now(tz=fuso)

    
payload = [
    {
        "UMIDADE": umidade,
        "CALOR": calor,
        "DATA": str(data)
    }
]
r = requests.post(url, json=payload)

time.sleep(2)

        
        


# print(calor)