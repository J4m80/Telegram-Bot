# Food Order Telegram Bot

A demo Telegram bot for ordering food: browse a menu, manage a cart, and share a delivery location.

## Features
- Reply-keyboard menu (View Menu, My order, Clear cart, Delivery, Help)
- Add items to the cart (Pizza, Burger, French fries, Ribeye)
- Remove an item by typing its number
- Clear the cart
- Request the user's location for delivery

## Tech
Python 3, pyTelegramBotAPI (telebot)

## Run
    pip install pyTelegramBotAPI
    export BOT_TOKEN="your_token_from_BotFather"
    python bot.py

## Limitations
- Cart is stored in memory (lost on restart)
- No payment, prices or order confirmation
- Location is received but not stored

## What I learned
Telegram Bot API, message handlers, reply keyboards, per-user state, environment variables for secrets.

## TODO
- [ ] Fix input validation (non-ASCII digits)
- [ ] Reply to unknown messages
- [ ] Unit tests for cart logic