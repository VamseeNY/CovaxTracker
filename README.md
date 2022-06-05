# CovaxTracker
A bot that scans for vaccine availability in analytically targeted regions and sends notifications via telegram channels. 

## Libraries, Packages and technologies used
Python, Selenium, Flask, HTML, CSS, and Heroku

## Bot (CovaxTracker/covaxtrackerbackend/paren.py)
The bot was developed using python and was deployed on heroku.

## Telegram implementation
Telegram channels were accessed by the bot via a unique 'chatid'. They are accessible via a webpage (https://covaxtracker.herokuapp.com/login) developed using HTML, CSS, and Flask deployed on Heroku.

## Automation
The integration of the bot with the telegram channels was carried out by three automation scripts which created a channel, extracted its ID and invite link, and finally linked it to the bot.

## Challenges
Memory management was tricky during backend development as the script had to collect data for a vast number of regions (about 200). Dealing with large amounts of data implies slower runtimes. The code was refactored and optimized to achieve acceptable runtimes. 


