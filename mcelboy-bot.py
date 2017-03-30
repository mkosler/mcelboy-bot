#!/usr/bin/python3.2

import os
from mastodon import Mastodon

FILENAME = os.getcwd() + '/boy-list.txt'

bot = Mastodon(
    client_id = os.getcwd() + '/clientcred.txt',
    access_token = os.getcwd() + '/usercred.txt')

lines = ''

with open(FILENAME, 'r') as f:
    lines = f.readlines()

bot.toot(lines[0])

lines += [lines.pop(0)]

with open(FILENAME, 'w') as f:
    f.writelines(lines)
