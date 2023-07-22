import os
import requests
import discord
import dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
dotenv.load_dotenv()
token = os.getenv("DC_SECRET")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#listen to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    
    if message.content.startswith("$help"):
        await message.channel.send("Hello, welcome to the Cryptocurrency Price Checker! \n To check the price of a cryptocurrency, type $price followed by the name of the cryptocurrency.")


    if message.content.startswith("$price"):
        # extract the cryptocurrency name from the message
        crypto_name = message.content.split("$price ", 1)[1].lower()
        # construct the url
        url = "https://api.coingecko.com/api/v3/simple/price?ids=" + crypto_name + "&vs_currencies=usd&include_market_cap=true&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=10"
        
        try:
            # make the request
            response = requests.get(url)
            # check if the request was successful
            if response.status_code == 200:
                data = response.json()
                if crypto_name in data:
                    # extract the price and market cap from the response
                    price = data[crypto_name]["usd"]
                    market_cap = data[crypto_name]["usd_market_cap"]
                    # send the price and market cap to the channel
                    await message.channel.send(
                        f"The current price of {crypto_name} is ${price}.\n"
                        f"Market Cap of {crypto_name} is ${market_cap}."
                    )
                else:
                    await message.channel.send(f"Error: {crypto_name} is not found in the API data. Please use the api key instead on CoinGecko coin page.")
            else:
                await message.channel.send(f"Error: Status code {response.status_code}.")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")

try:
    client.run(token)
except Exception as e:
    print(e)

