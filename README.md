# BlankDiscordBot
This script library allows you to create your own discord bot (hopefully) easily!

**Warning:** If youre planning on using version control with this project, make sure you DO NOT commit your discord API token found within `store/auth.json`

## Setup
There is a non-trivial amount of setup required to start executing this discord bot on your local machine, which has been segmented into the 3 primary parts below.
### Python
First, download Anaconda from the [offical website](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). You should then be able to create a conda environment for the necessary python installation requirements
```bash
conda create --name discord-bot python=3.9
cnda activate discord-bot
```
Then, install the python dependencies
```bash
pip install -r requirements.txt
```
Currently, each of the listed requirements individually may/may not be actually necessary for the bot to function.
### Bash
Give the bash executables permissions to run
```bash
chmod +x bash/keep-running.sh
chmod +x bash/kill.sh
```

### Discord & API Tokens
First, you'll have to actually create and register the Discord application / bot via this [portal](https://discord.com/developers/applications). Create a new application, then create a new Bot within that application (feel free to name both of these what you wish, but the bot's name and image are what will show up on it's discord profile).

When you create the bot, copy it's token and paste it into `store/auth.json`, replacing the string labeled `TODO`. You'll also need to enable the server members and message content intents such that it is able to view server users and read command messages.

To actually add the bot to your discord use the following URL:

https://discord.com/api/oauth2/authorize?client_id=TODO&permissions=1497064598640&scope=bot%20applications.commands

Make sure to replace the client_id TODO with the one found on your Application's OAuth2 page.

## Running the Bot
Note that both of the following scripts assume that you have no other processes running on your computer launched using `python3.9`. Before running, it's worth checking if this assumption is valid via the following command:
```bash
ps -A | grep python3.9
```
If the command returns non-empty results, the following scripts should not be used and you should develop your own version of them that is compatible with the device in question.

To start running the bot execute the following terminal command:
```bash
./bash/keep-running.sh &
```
This will create a wrapper infinitely-looping process that consistently checks whether or not the bot has crashed (this frequently happens to me due to socket-related / internet connectivity issues). If it has, it relaunches so the bot is always up.

If you want to stop these infinitely looping processes (the `keep-running` script and the actual running bot), execute the follwoing:
```bash
./bash/kill.sh
```
This will stop the bot and related wrapper process.

# Using the Bot

If you aren't the owner of the bot in question, or if you've already completed the set up then the following describes how to use the bot with relevant commands

## Discord Command Examples
The provided starter code has a couple of simple commands implemented so you can get a feel for how to build your own! Try these out and then the world is your oyster. You can use whatever data structures behind the scenes to represent necessary information, and can even save to a file to keep persistent state after the bot shuts down.

# Development
## Directory Layout
- `bash`
    - Where the bash scripts are located
    - `keep-running.sh`
        - Allows the bot to relaunch itself on crash
    - `kill.sh`
        - Kills both the currently running bot and `keep-running.sh`
- `src`
    - Where the actual library implementations exist.
    - `constants.py`
        - Constant definition within the bot
            - Might be worth changing for your specific use case
    - `discord_helper.py`
        - Useful discord-related commands:
            - Getting user from server
            - Sending message to channel
            - etc.
    - `exceptions.py`
        - Custom exception definitions
    - `utils.py`
        - Useful functions used throughout the library
- `store`
    - For general storage purposes. Houses the user's Ed API token.
    - `logging`
        - Where the activity logs are stored
- `tests`
    - Where to add any unit tests
- `bot.py`
    - Launch this to run the python bot
