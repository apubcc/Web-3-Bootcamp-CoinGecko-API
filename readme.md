# A Quick Guide of CoinGecko API using Discord Bot

## Introduction

This guide will walk you through the steps to create a Discord bot that fetches cryptocurrency prices using the CoinGecko API. The bot will respond to commands from users and provide real-time price data for cryptocurrencies.

## Prerequisites
- A Discord Account
- Basic knowledge of programming and the Python programming language
- Python and pip (package installer for Python) installed on your system

## Links
- https://discord.com/developers/docs/getting-started
- https://www.coingecko.com/en/api/documentation
- https://apiguide.coingecko.com/getting-started/introduction


## Steps
### 1. Set up Discord Bot
### 2. Invite the Bot to your server
### 3. Set up the project (You can fork the repo using Git Clone or just copy the code)
### 4. Write the bot code
### 5. Play around with CG API
### 6. Run the Bot


## What you can build using CG API
1. Crypto Price Bot (using /simple/price)
2. Trending Coins Bot (using /search/trending)
3. Exchanges + Derivatives Exchanges List Bot (using /exchanges + /derivative/exchanges)
4. DeFi Bot (using /global/decentralized_finance_defi) + defillama API + GeckoTerminal API
5. NFT Bot (using /nft/list)


## Public API vs Pro API

Example: 

**Public API**
<br>
https://api.coingecko.com/api/v3/ping
<br>
https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&x_cg_demo_api_key=YOUR_API_KEY


**Pro API**
<br>
https://pro-api.coingecko.com/api/v3/ping?x_cg_pro_api_key=YOUR_API_KEY
<br>
https://pro-api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&x_cg_pro_api_key=YOUR_API_KEY


**Pro API always**
Starts with: pro-api.coingecko.com/api/v3/
& Ends with: x_cg_pro_api_key=YOUR_API_KEY







