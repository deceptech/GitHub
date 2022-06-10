# slacker-processor
Python script that allows for Pentesters/Bug Bounty teams save time on running commands/sharing results.

This script prompts for a user provided command to run to on their local machine (example: nmap, zenmap, whoami, ipconfig, etc.). Once ran, the results of the command are then sent through a Slack webhook to a channel of your choosing.

The steps for setting up an incoming Slack webhook can be found here:
https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack

![slack-alert](https://user-images.githubusercontent.com/83108604/173144463-e3e09d8f-7be8-453f-9d5f-7693410cad7b.png)
