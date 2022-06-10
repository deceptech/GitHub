#/usr/bin/python3

import os
import json
import sys
import random
import requests

command_to_execute = input("Enter the command you wish to run:")

def command():
    with os.popen(command_to_execute) as f:
     results = f.read()
    return results
print(command())

def slacker(results):
    url = "" #Enter Slack Webhook URL here (Visit https://api.slack.com/messaging/webhooks#posting_with_webhooks if you don't know how to get one)
    message = ("The script " + command_to_execute + " has finished running!" + "\n" + "Results:" + "\n" + results)
    title = (f"Cool Title Here!") #Customize this!
    slack_data = {
        "username": "Python-Bot", #Change this for customization
        "icon_emoji": ":zap:", #Check out https://www.webfx.com/tools/emoji-cheat-sheet/ for different emoji's to use
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


if __name__ == '__main__':
    results = command()
    slacker(results)