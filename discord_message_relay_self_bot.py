"""Relays messages from a Discord channel to a different channel.

  Copies a message from a specific channel in a Discord server into
  a different channel. Can be a channel from the same server or a
  different server.
"""

from discord.ext import commands
import requests

# Insert your Discord account's token (PREFERRABLY AN ALT).
TOKEN = "AccountTokenHere"
# Insert your webhook URL for the channel you want the copied text to go.
WEBHOOK_URL = "YourOwnChannelWebHookURL"
# Insert the server's ID that you want to copy the message from.
GUILD_ID = 0
# Inset the server's channel ID that you want to copy the message from.
CHANNEL_ID = 0


bot = commands.Bot(command_prefix = "", self_bot = True)

@bot.event
async def on_ready():
  """When the bot finishes loading up."""
  print("Bot is ready.")


@bot.event
async def on_message(message):
  """When a message is sent."""
  # Ignore messages not from the correct server or channel.
  if message.guild.id != GUILD_ID or message.channel.id != CHANNEL_ID:
    return

  # Ignore messages from itself or duplicates.
  if message.author.id == bot.user.id or message.webhook_id is not None:
    return

  # Correct message to relay found.
  content = f"{message.content}"

  # Replace role mentions with plain text.
  for role in message.role_mentions:
    mention_str = f"<@&{role.id}>"
    content = content.replace(mention_str, f"<@&{role.name}>")

  # Send message to webhook.
  requests.post(WEBHOOK_URL, json = {"content": content}, timeout = 60)



bot.run(TOKEN)
