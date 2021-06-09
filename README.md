# Telegram Bot and Email to notify you if your website does not respond correctly or the server is down

## The ServerStatusBot
The bot that I have implemented using python, will allow me to:
Check on a regular basis the response of websites and ping the server that I want to monitor.
Get a telegram message in case of a negative response (For example 404, 502, 405 etc…).
Send an email to a team member responsible for this project, in case of both server-downtime or unexpected response.

## Creating your bot
On Telegram, 
1. search @ BotFather 
2. send him a “/start” message
3. Send another “/newbot” message, then follow the instructions to set up a name and a username
Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your bot_token

## Getting your Chat id
On Telegram, search your bot (by the username you just created), press the “Start” button, or send a “/start” message
Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this:
Look for “id”, for instance, 14XXXXXXabove is my chat id. Look for yours and put it as your bot_chatID in the code above
Now, you have the data needed to send messages to your own bot. Let’s see how to send a custom message using python.
Implementing the bot

## Email alert
To communicate via email, I had to use an SMTP server. For testing purposes, you can use a free Gmail SMTP or mailgun.
To easily know which Team Member to contact according to the website or server that needs immediate attention, I have used a key-value relation between the server and the email of the maintainer, using the server name as key and email as value. Implementing this logic is possible using a python dictionary (also known as unodered_map).


## Crontab job to run our Python Script
This type of monitoring task requires that our script will run very often, but in this case, the sleep function is not probably needed, to avoid getting the script running constantly.
Instead, we can use the system cronjob, which will execute for us script every time we need it. In this case, I wish to do one request to the website and one ping to the server every 5 minutes.
### First, set our script file as executable:
```chmod +x <python file>```
Once the script is executable, define a new cron job, by typing in the terminal
```crontab -e```
and pasting the following crontab job definition, that will mean: every 5 minutes, run python3 <path_to_the_file_to_execute_>
```*/5 * * * * python3 /home/<user_name>/server_status_bot.py >> ~/cron.log 2>&1```

## In case of an error for schedule module not found
```pip3 install schedule```
