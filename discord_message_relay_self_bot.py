"""Relays messages from a Discord channel to a different channel.

  Copies a message from a specific channel in a Discord server into
  a different channel. Can be a channel from the same server or a
  different server.
"""

import discord
from discord.ext import commands
import requests
import asyncio

# Insert your Discord account's token (PREFERRABLY AN ALT).
TOKEN = "AccountTokenHere"
# Insert your webhook URL for the channel you want the copied text to go.
WEBHOOK_URL = "YourOwnChannelWebHookURL"
# Insert your webhook URL for the channel you want the embedded stock to go.
EMBEDDED_STOCK_URL = "YourOwnChannelWebHookURL2"
# Insert your webhook URL for the channel you want the embedded eggs to go.
EMBEDDED_EGGS_URL = "YourOwnChannelWebHookURL3"
# Insert the server's ID that you want to copy the message from.
GUILD_ID = 1371970717444341802
# Inset the server's channel ID that you want to copy the message from.
CHANNEL_ID = 1371986851346386944
# Replace with the server's role IDs for the crops.
ROLE_IDS = {
  # Seeds
  "Carrot": 1372815089752739931,
  "Strawberry": 1372815176814034984,
  "Blueberry": 1372815230060728431,
  "Orange Tulip": 1372815271198331003,
  "Tomato": 1372815318380187699,
  "Corn": 1372815353696223253,
  "Daffodil": 1372815384956239953,
  "Watermelon": 1372452314266210315,
  "Pumpkin": 1372452293844406292,
  "Apple": 1372815518695952384,
  "Bamboo": 1372452206795554867,
  "Coconut": 1372452261334355999,
  "Cactus": 1372452222994092134,
  "Dragon Fruit": 1372452177867575327,
  "Mango": 1372452145034563647,
  "Grape": 1372451824866689045,
  "Mushroom": 1372452342091223081,
  "Pepper": 1372452163908796486,
  "Cacao": 1372452363067195443,
  "Beanstalk": 1373415455632392212,
  "Ember Lily": 1381033956610408489,
  "Sugar Apple": 1383914061649023006,
  "Cauliflower": 1386081116150042758,
  "Green Apple": 1386081963810488462,
  "Avocado": 1386082116365717595,
  "Banana": 1386082332389412957,
  "Pineapple": 1386082565827592365,
  "Kiwi": 1386082697620881612,
  "Bell Pepper": 1386082762313699439,
  "Prickly Pear": 1386082836766916608,
  "Loquat": 1386083080686669844,
  "Feijoa": 1386083160185634967,

  # Gears
  "Watering Can": 1372814927076786206,
  "Trowel": 1372814844817969222,
  "Recall Wrench": 1372815973299650560,
  "Basic Sprinkler": 1372814869015040020,
  "Advanced Sprinkler": 1372452574027976764,
  "Godly Sprinkler": 1372452630240170014,
  "Master Sprinkler": 1372452602872201327,
  "Tanning Mirror": 1386080730089652324,
  "Cleaning Spray": 1383914169677516840,
  "Favorite Tool": 1372814811603144704,
  "Harvest Tool": 1375973801753448489,
  "Friendship Pot": 1381033769649049702,

  # Eggs
  "Common Egg": 1372818043075563540,
  "Uncommon Egg": 1372818095927726170,
  "Rare Egg": 1372452481304629310,
  "Legendary Egg": 1372452534098202694,
  "Mythical Egg": 1373415657076555868,
  "Bug Egg": 1372452558513246299,
  "Common Summer Egg": 1386080128475594834,
  "Rare Summer Egg": 1386080182095581244,
  "Paradise Egg": 1386080215763259484
}
# Items that will be displayed between stars to indicate that it is good.
GOOD_ITEMS = [
  # Seeds
  "Loquat", "Feijoa", "Sugar Apple",
  # Gears
  "Master Sprinkler",
  # Eggs
  "Legendary Egg", "Mythical Egg", "Bug Egg", "Rare Summer Egg", "Paradise Egg"
]


bot = commands.Bot(command_prefix = "", self_bot = True)

@bot.event
async def on_ready():
  """ When the bot finishes loading up. """
  print("Bot is ready.")


@bot.event
async def on_message(message):
  """ When a message is sent. """
  # Ignore messages not from the correct server or channel.
  if message.guild.id != GUILD_ID or message.channel.id != CHANNEL_ID:
    return

  # Ignore messages from itself or duplicates.
  if message.author.id == bot.user.id or message.webhook_id is not None:
    return

  # Correct message to relay found.
  content = f"{message.content}"
  embedded_content = f"{message.content}"

  # Official server messed up on this for Friendship Pot.
  ping_roles = ""
  if "Friendship Pot" in message.content:
    content = content.replace("Friendship Pot (ROLE NOT FOUND)",
                              f"<@&{ROLE_IDS['Friendship Pot']}>")
    embedded_content = embedded_content.replace("Friendship Pot (ROLE NOT FOUND)", "Friendship Pot")
    ping_roles += f"<@&{ROLE_IDS['Friendship Pot']}>"


  # Replace role mentions with plain text.
  for role in message.role_mentions:
    # If the item isn't added to the bot yet, print and ignore.
    if role.name not in ROLE_IDS:
      print(f"{role.name} doesn't exist in ROLE_IDS!")
      continue

    mention_str = f"<@&{role.id}>"
    content = content.replace(mention_str, f"<@&{ROLE_IDS[role.name]}>")
    embedded_content = embedded_content.replace(mention_str, f"{role.name}")

  # Send message to webhook.
  requests.post(WEBHOOK_URL, json = {"content": content}, timeout = 60)

  # Send embedded message to webhook.
  embed = discord.Embed(color = 0xFEE9FF)

  # Extract and clean the title up.
  embedded_content_split = embedded_content.split("\n")
  cleaned_title = embedded_content_split[0].replace("## ", "")
  cleaned_title = cleaned_title.replace(" Update", "")
  cleaned_title = cleaned_title.replace("SeedStock", "Seeds Stock")
  cleaned_title = cleaned_title.replace("GearStock", "Gears Stock")
  cleaned_title = cleaned_title.replace("Egg Stock", "Eggs Stock")

  # Create embed message and obtain roles to ping.
  embedded_items_text = ""
  for i in range(1, len(embedded_content_split) - 1):
    # Switch from x# format into #x format.
    formatted_item_text = embedded_content_split[i].replace("x", "")
    formatted_item_text = formatted_item_text.replace("*", "")
    quantity_item_list = formatted_item_text.split(" ", 1)
    # Format based on whether the item is good or not (has stars around if good).
    if quantity_item_list[1] in GOOD_ITEMS:
      formatted_item_text = f"`{quantity_item_list[0]}x` :star: {quantity_item_list[1]} :star:"
    else:
      formatted_item_text = f"`{quantity_item_list[0]}x` {quantity_item_list[1]}"

    # If the role exists.
    if quantity_item_list[1] in ROLE_IDS:
      # Add to ping_roles if it is unique.
      if str(ROLE_IDS[quantity_item_list[1]]) not in ping_roles:
        ping_roles = ping_roles + f"<@&{ROLE_IDS[quantity_item_list[1]]}> "

    embedded_items_text = embedded_items_text + formatted_item_text + "\n"
  embed.add_field(name = cleaned_title, value = embedded_items_text,
                      inline = False)
  embed.add_field(name = "", value = embedded_content_split[-1], inline = False)

  # Message to be sent.
  payload = {
    "content": ping_roles,
    "embeds": [embed.to_dict()]
  }

  # Send to correct channel based on stock type.
  if cleaned_title in ("Seeds Stock", "Gears Stock"):
    requests.post(EMBEDDED_STOCK_URL, json = payload, timeout = 60)
    await asyncio.sleep(5)
  elif cleaned_title == "Eggs Stock":
    requests.post(EMBEDDED_EGGS_URL, json = payload, timeout = 60)
    await asyncio.sleep(5)


bot.run(TOKEN)
