# slacker-processor
Python script that allows for Pentesters/Bug Bounty teams save time on running commands/sharing results.

This script prompts for a user provided command to run to on their local machine (example: nmap, zenmap, whoami, ipconfig, etc.). Once ran, the results of the command are then sent through a Slack webhook to a channel of your choosing.

The steps for setting up an incoming Slack webhook can be found here:
https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack
