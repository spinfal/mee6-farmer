import requests
import time as t
import random
import os
from termcolor import colored as cl
token = input(cl('token: ', 'white'))
channel = input(cl('channelID: ', 'white'))
if channel.isnumeric() == False:
  print(cl('the channel ID can only contain numbers.', 'red'))
  t.sleep(2)
  os.system('python3 main.py')
print(cl('farming has started!', 'green'))

#change your words here
message = ['hm', 'bruh', 'main is lame', 'hmhm', 'imbored', 'aaaamtired']
#then change line 21 to correspond with the word-count

headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}

while True:
  sel = random.randint(0,5)
  sleep = random.randint(61,65)
  sendmsg = requests.post('https://discordapp.com/api/v6/channels/' + channel + '/messages', json={'content': message[sel]}, headers=headers)
  print(cl(message[sel], 'cyan') + ' sent in the channel ' + cl(channel, 'cyan'))
  t.sleep(sleep)