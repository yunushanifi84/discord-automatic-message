import json

with open('config.json','r')as f:
    config = json.load(f)

token1 = config["token1"]
token2 = config["token2"]
token3 = config["token3"]
token4 = config["token4"]

print(f'1. token : {token1}')
print(f'2. token : {token2}')
print(f'3. token : {token3}')
print(f'4. token : {token4}')