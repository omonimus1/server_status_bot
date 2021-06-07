## Requirement
* Schedule: pip3 install schedule

## How to run it
python3 send.py

## Telegram Bot to notify you if your websites do not respond correctly

On the cloud, there are tons of resources that could notify you if your website does not respond anymore, or if your whole resource (Cloud Server/VPS), is now 'off' if your resource is using a modest amount of hardware resources, such that this usage level could be considered critical.
Many traditional providers, do not offer this kind of notification, and your website could be down, without any kind of alert given to you. 
This is the reason why on a boring Sunday afternoon I have created a personal telegram bot, that would notify me if one of the websites that I am interested to monitor is not available. Of course, there are already professional products in charge of this, but I am going to share with you my experiment. 

### Creating your bot
On Telegram:
1. Search @ BotFather
2. Send him a "/start" message
3. Send another "/newbot" message, then follow the instructions to setup a name and a username
4 Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your bot_token

### Getting your Chat id
On Telegram, search your bot (by the username you just created), press the "Start" button or send a "/start" message
Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this:

Look for "id", for instance, 14XXXXXXabove is my chat id. Look for yours and put it as your bot_chatID in the code above
Now you are all set, run the code, and enjoy receiving messages from yourself :)
