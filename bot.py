import json
import discord
import datetime
import logging
from discord.ext import commands

from src.constants import (
    LOGGING_FILE, AUTH_FILE, TIMEOUT
)
from src.utils import (
    send_message, y_n_emoji, repeat_request, dm_check
)

from src.discord_helper import DiscordHelper

logging.basicConfig(filename=LOGGING_FILE, encoding='utf-8',
                    level=logging.INFO)

# -----------------------------------------------------------------------------#
# START CONFIGURATIONs

intents = discord.Intents(messages=True, guilds=True,
                          members=True, message_content=True, reactions=True)
# Can change the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# -----------------------------------------------------------------------------#
# START COMMANDS


@bot.command(
    name='ping',
    help="Example ping command"
)
async def br_setup(ctx):
    logging.info(f"Ping command from guild: {ctx.guild.id}")
    try:
        current_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        # Can send messages to the original channel the request was given in!
        await send_message(ctx.channel,
                           f"Pong! 🏓. Server time: {current_time}")

        logging.info(f"Successfully sent ping response to {ctx.guild.id}")
    except Exception as e:
        logging.exception(e)
        await send_message(ctx.channel,
                           f"Error encountered when handling request: {e}")


@bot.command(
    name='dm',
    help="Example dm command"
)
async def br_stop(ctx):
    logging.info(f"Dm command from guild {ctx.guild.id}")
    try:
        user_id = ctx.author.id
        requester = DiscordHelper.get_user(ctx.guild, user_id)
        # Can send messages to users in a DM!
        await send_message(requester, "Hello! Please write something that " +
                                      "starts with the letter 'A'")

        # Will repeatedly ask for a response based on some condition
        message, user = await repeat_request(
            bot=bot,
            auth_check=lambda message: dm_check(message, ctx),  # Checks for DM response
            valid_check=lambda message: message[0] == 'A',  # Checks for validity
            timeout=TIMEOUT,
            send_invalid_message=lambda message: send_message(  # Response in case of error
                requester,
                f"Message [{message}] doesn't start with 'A'"
            )
        )

        logging.info(f"Successfully DM'd user: {user_id}")
    except Exception as e:
        logging.exception(e)
        await send_message(ctx.channel,
                           f"Error encountered when handling request: {e}")


@bot.command(
    name='y-n',
    help="Example yes/no command"
)
async def br_push(ctx):
    logging.info(f"y/n command from {ctx.channel}")
    try:
        async def respond_public_channel(message):
            return (await send_message(ctx.channel, message))

        # Can do some fancy things with y/n emoji reactions!
        yes = await y_n_emoji(
            bot, respond_public_channel,
            "Yes or no?",
            ctx.author, TIMEOUT
        )
        respond_public_channel("Yes!" if yes else "No!")

        logging.info(f"Successfully replied to y/n command from {ctx.channel}")
    except Exception as e:
        logging.exception(e)
        await send_message(ctx.channel,
                           f"Error encountered when handling request: {e}")


# -----------------------------------------------------------------------------#
# START EVENTS

@bot.event
async def on_connect():
    logging.info("Bot conected!")


@bot.event
async def close():
    logging.info("Bot shutting down!")

# -----------------------------------------------------------------------------#
# START BOT

bot.run(json.load(open(AUTH_FILE))['token'])
