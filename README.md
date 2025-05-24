# Discord Message Relay Self Bot [Branch: Grow A Garden - Embedded]
- By Thomas Truong

## ! WARNING !
- Self bots are against Discord's TOS, use at your own discretion.
  - Highly recommended to use an alt account (throw-away account).

## About
- Grow A Garden is a ROBLOX game.
- Relays messages from Grow A Garden's official stock Discord to my own server.
  - Customizes the relayed message with embedded style.

## Prerequisites
- discord.py-self
  - > pip install -U discord.py-self
- requests
  - > pip install -U requests
- Developer Mode enabled on Discord
  - Only needed for setting up the bot; not needed after.
    - You can leave it enabled or disable if you want; personally, I always have it enabled.
  - Settings -> Advanced -> Developer Mode.
- Join the server with your Discord selfbot account.
  - Needs to be able to read from the target channel to relay.

## Usage
- Insert information needed in [discord_message_relay_self_bot.py](discord_message_relay_self_bot.py).
  - TOKEN
    - Your Discord account's token (PREFERRABLY AN ALT ACCOUNT).
    1. Press CTRL + Shift + I to open inspect element.
        - Switch to web browser version if this doesn't work.
    2. Click on Network
    3. Refresh (Ctrl + R or click the refresh button if browser).
    4. Filter for `messages`.
    5. Select it and look under `Request Headers` -> `Authorization:` for the token.
        - Recommended to keep this private.
  - WEBHOOK_URL
    - Your webhook URL for the channel you want the copied text to go.
    - Your Server -> Right-Click Channel -> Edit Channel -> Integrations -> Webhooks -> New Webhook -> Click on Webhook -> Copy Webhook URL.
        - Recommended to keep this private.
  - EMBEDDED_STOCK_URL
    - Insert your webhook URL for the channel you want the embedded stock message to go.
    - Your Server -> Right-Click Channel -> Edit Channel -> Integrations -> Webhooks -> New Webhook -> Click on Webhook -> Copy Webhook URL.
        - Recommended to keep this private.
  - EMBEDDED_EGGS_URL
    - Insert your webhook URL for the channel you want the embedded eggs message to go.
    - Your Server -> Right-Click Channel -> Edit Channel -> Integrations -> Webhooks -> New Webhook -> Click on Webhook -> Copy Webhook URL.
        - Recommended to keep this private.
  - GUILD_ID
    - The server's ID that you want to copy the message from.
      - Right-Click on Target Server -> Copy Server ID.
  - CHANNEL_ID
    - The server's channel ID that you want to copy the message from.
      - Select Server -> Right-Click on Target Channel -> Copy Channel ID.
  - ROLE_IDS
    - Replace with the server's role IDs for the crops.
      - Right-Click on Your Server -> Server Settings -> Roles -> Right-Click a Role -> Copy Role ID.
  - GOOD_ITEMS
    - Items that will be displayed between stars to indicate that it is good.
      - Example: ⭐ Bug Egg ⭐
- Run [discord_message_relay_self_bot.py](discord_message_relay_self_bot.py) and it should automatically work once a new message is sent in the target channel.
- 24/7 Hosting: [Wispbyte](http://wispbyte.com/)
  - I came across this site which offers free 24/7 hosting and I am currently using this.