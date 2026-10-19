# Food Order Telegram Bot

![Tests](https://github.com/J4m80/Telegram-Bot/actions/workflows/tests.yml/badge.svg)

A demo Telegram bot for ordering food: browse a menu, manage a cart, and share a delivery location.

## Features
- Reply-keyboard menu (View Menu, My order, Clear cart, Delivery, Help)
- Add items to the cart (Pizza, Burger, French fries, Ribeye)
- Remove an item by typing its number
- Clear the cart
- Request the user's location for delivery

## Tech
Python 3, pyTelegramBotAPI (telebot), pytest, GitHub Actions

## Project structure
- `bot.py` – Telegram handlers and keyboards
- `cart.py` – cart logic (add, remove, clear), no Telegram dependency
- `test_cart.py` – pytest tests for the cart logic
- `.github/workflows/tests.yml` – CI that runs tests on every push

## Run
    pip install pyTelegramBotAPI
    set BOT_TOKEN=your_token_from_BotFather      (Windows CMD)
    python bot.py

## Run tests
    pip install pytest
    pytest

## Testing notes
Besides automated tests, I manually tested the bot: invalid item numbers, non-ASCII digits (e.g. `²`) and unknown text. The digit input crash was found this way and fixed.

## Limitations
- Cart is stored in memory (lost on restart)
- No payment, prices or order confirmation
- Location is received but not stored

## TODO
- [ ] Use `clear_cart` from `cart.py` in the bot
- [ ] Tests for more edge cases
