import discord
import logging
import requests

from typing import (
    Union, Any
)
from src.utils import (
    send_message
)
from src.constants import (
    LOGGING_FILE
)

logging.basicConfig(filename=LOGGING_FILE, encoding='utf-8',
                    level=logging.INFO)


class DiscordHelper:
    @staticmethod
    def get_attachment(
        url: str
    ) -> Union[None, str]:
        """
        Params: 'url' - The url corresponding to a discord attachment
        Returns: The discord attachment for the given attachment url
        """
        return requests.get(url).content.decode('utf-8') if url else None

    @staticmethod
    async def create_channel(
        guild: Any, name: str,
        overwrites: Any
    ) -> int:
        """
        Params: 'guild' - The guild in which to create a channel
                'name' - The channel name
                'overwrites' - The appropriate overwrites for the channel
                               (found via discord API)
        Returns: The channel id for the newly created channel
        """
        return (
            await guild.create_text_channel(name, overwrites=overwrites)
        ).id

    @staticmethod
    async def create_thread(
        channel: Any,
        starting_message: str,
        thread_name: str
    ) -> Any:
        """
        Params: 'channel' - The channel in which to create the thread
                'starting_message' - The starting message to created the
                                     thread off of
                'thread_name' - The name of the thread
        Returns: The newly created discord thread
        """
        message = await send_message(channel, starting_message)
        return await message.create_thread(name=thread_name)

    @staticmethod
    def get_role(
        guild: Any,
        role_id: int
    ) -> Any:
        """
        Params: 'guild' - The guild in which the role is
                'role_id' - The role ID to get
        Returns: The role object corresponding to the given role ID
        """
        return discord.utils.get(guild.roles, id=role_id)

    @staticmethod
    def get_user(
        guild: Any,
        user_id: int
    ) -> Any:
        """
        Params: 'guild' - The guidl in which the user is
                'user_id' - The user ID to get
        Returns: The role object corresponding to the given role ID
        """
        return discord.utils.get(guild.members, id=user_id)

    @staticmethod
    def get_thread(
        guild: Any,
        thread_id: int
    ) -> Any:
        """
        Params: 'guild' - The guild in which the role is
                'thread_id' - The thread ID to get
        Returns: The thread object corresponding to the given thread ID
        """
        return discord.utils.get(guild.threads, id=thread_id)
