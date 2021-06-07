import time
import schedule
import requests
import os


# List of URLS I want to monitor
url_list = [
    'http://davidepollicino.com/'
]


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def report():
    for website in url_list:
        page = requests.get(website)
        if(page.status_code != 200):
		telegram_bot_sendtext(website + 'returns a ' + page.status_code)

        response = os.system("ping -c 1 " + website)
        #and then check the response...
        if response != 0:
            telegram_bot_sendtext(website + ' server is down')
  

if __name__ == "__main__":
    report()
    
    
