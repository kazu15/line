import requests
import datetime
import pytz

time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time = time.strftime('%Y/%m/%d/ %H:%M:%S')

#GET TOKEN
TOKEN = 'wtuI6Umpk9aqlULBd1FRF43e3LvtJBB2ClE7cFKoy3a'
#API URL
api_url = 'https://notify-api.line.me/api/notify'
#send time
# send_contents = time
send_message = """
Check
https://forms.gle/L6pjycxa5esnwKcq9"""

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_message}

image_file = 'turtle.jpg'
# binary = open(image_file, mode='rb')
# image_dic = {'imageFile':binary}

requests.post(api_url, headers=TOKEN_dic, data=send_dic)