# Tarot Reading Telegram Bot
A Python-based Telegram bot to perform virtual tarot card readings. Users can get personalized tarot readings directly in their Telegram chat, with visual representations of the cards.

## Features
- **Interactive Commands**: A variety of tarot spreads are available:
    - `/three_card` – A 'Past, Present, Future' reading for insights across time.
    - `/four_card` – A layout to answer specific yes/no questions.

- **Visual Tarot Cards**: Generates an image showcasing the selected tarot cards, along with their orientation (upright or reversed).
- **Dynamic Responses**: Cards are selected randomly, ensuring unique readings for each session.
- **MongoDB Database Support**: Tarot card information is stored and efficiently queried using MongoDB.

## How It Works
The bot performs tarot readings by interacting with Telegram users via simple commands. Here's an overview of its components:
1. **`main.py` **:
    - Handles command parsing using the Telegram Bot API.
    - Defines commands like `/start`, `/three_card`, and `/four_card`.
    - Uses helper functions to send readings and images.

2. **`tarot_reader.py` **:
    - Interfaces with MongoDB to fetch a random set of tarot cards.
    - Formats the selected cards with additional metadata (orientation, title).

3. **`tarot_img.py` **:
    - Generates the visual representation of tarot cards.
    - Creates an image by combining card images with proper formatting.

## Setup and Installation
Follow these steps to run the bot on your local environment:
1. Clone the repository:
``` bash
   git clone https://github.com/your-repository-url.git
   cd tarot-telegram-bot
```
1. Install dependencies:
``` bash
   pip install -r requirements.txt
```
1. Create a **`.env`** file to store sensitive information:
``` env
   TOKEN=your_telegram_bot_token
   BOT_USERNAME=your_bot_username
   MONGO_URL=mongodb_connection_string
```
1. Launch the bot:
``` bash
   python main.py
```
## Commands
![Start Command](/img/bot_start.png)
- **Start the bot**:
``` 
  /start
```
Explains how to use the bot, detailing the types of readings available.
- **Perform a reading**:
### Three Card Reading:
![Three Card Reading](/img/bot_three_card.jpg)

``` 
  /three_card
```
Provides a traditional "Past, Present, Future" spread, with visual cards and their interpretations.
### Four Card Reading
![Four Card Reading](/img/bot_four_card.png)

``` 
  /four_card
```
Offers insight for a specific question, producing a four-card spread.

### See the bot in action:
![Three Card Reading](/img/qr_code.jpg)
### @Tarot_ReaderBot