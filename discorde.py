import requests
import time
from datetime import datetime
import json

def send_message(channel_id, token,mesaj):
    message = {'content': mesaj}
    headers = {'Authorization': token}
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=message, headers=headers)
    return r
def send_intreact(token,payload):
    message = payload
    header = {'Authorization': token}
    r = requests.post("https://discord.com/api/v9/interactions",json=payload,headers=header)
    return r

with open('config.json','r') as f:
    config = json.load(f)


kanal_id ="1053726991309877269"

payload1 = {
        'type': 2,
        'application_id': '624187616312426512',
        'guild_id': '787718450206343218',
        'channel_id': kanal_id,
        'session_id': '6a2b27034b8ad231a6e4b3ab59d5ef5b',
        'data': {
            'version': '1091396033331871884',
            'id': '1091396032694337540',
            'name': 'hunt',
        }
    }

token1 = config["token1"]
token2 = config["token2"]
token3 = config["token3"]
token4 = config["token4"]
times = int(input('Tekrarlanacak işlem sayisini giriniz: '))

b = 1
for i in range(times):
    response=send_intreact(token1,payload1)
    time.sleep(15)
    response=send_intreact(token1,payload1)
    time.sleep(5)
    send_message(kanal_id,token1,("Komut Gönderildi:"+f"{b}"))
    response=send_intreact(token2,payload1)
    time.sleep(15)
    response=send_intreact(token2,payload1)
    time.sleep(5)
    send_message(kanal_id,token2,("Komut Gönderildi:"+f"{b}"))
    response=send_intreact(token3,payload1)
    time.sleep(15)
    response=send_intreact(token3,payload1)
    time.sleep(5)
    send_message(kanal_id,token3,("Komut Gönderildi:"+f"{b}"))
    response=send_intreact(token4,payload1)
    time.sleep(15)
    response=send_intreact(token4,payload1)
    time.sleep(5)
    send_message(kanal_id,token4,("Komut Gönderildi:"+f"{b}"))
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print('Yapilan işlem sayisi: {}  Saat: {}'.format(b, current_time))
    b += 1
    time.sleep(615)
