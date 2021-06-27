import time
import schedule
import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from socket import gaierror

## SMTP DETAILS
port = 465
smtp_server = 'smtp.gmail.com'
login = ''
password = ''
mail_from = ''

# List of urls that we want to Manage: Website/Hostname: Email of the person responsible
url_list = {
    'http://davidepollicino.com/'  : 'davidepollicino2015@gmail.com'
}


# Send Message to the Bot
def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# Monitor status of the websites and server
def report():
    error_message = ''
    for website in url_list.keys():
        page = requests.get(website)
        if(page.status_code != 200):
            error_message = website +' returns status: '+ str(page.status_code)
            telegram_bot_sendtext(error_message)
            contact_tester_member(url_list[website], error_message)

         # Ping server 
         response = os.system("ping -c 1 " + website)
         if response != 0:
            error_message = website + ' server is down'
            telegram_bot_sendtext(error_message)
            contact_tester_member(url_list[website], error_message)



# Send an email to the Project Manager or team member responsible for the maintenace
def contact_tester_member(email_responsible, error_message):
    msg = EmailMessage()
    msg.set_content(error_message)
    msg['Subject'] = 'Website/Server Error'
    msg['From'] = mail_from
    msg['To'] = email_responsible
    try: 
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(login, password)
        server.send_message(msg)
        server.quit()
        print('sent')
    except:
        print('error')


if __name__ == "__main__":
    report()    
