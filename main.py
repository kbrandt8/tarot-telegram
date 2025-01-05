import os
from typing import final

from dotenv import load_dotenv
load_dotenv()
from tarot_img import TarotImage
from tarot_reader import Reading, MONGO_URL

from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes,Updater

TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
CONNECTION_STRING = os.getenv('MONGO_URL')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_text = (f"Let's start your reading, {update.effective_user.first_name}\n"
                  f"Pick a reading:\n"
                  f"/three_Card:\n"
                  f"The classic 'past present future' reading\n"
                  f"/four_Card: \n"
                  f"Best for a yes or no answer")

    await update.message.reply_text(reply_text)


async def three_card_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_text = f""
    reading = Reading()
    three_card = reading.three_card()

    for card in three_card:
        reversed = "Reversed" if card['is_reversed'] else "Upright"
        reply_text += f"{card['title']}: {card['name']} ({reversed}) \n"
    print(reply_text)
    images = TarotImage(three_card)
    await context.bot.send_photo(update.effective_chat.id, open("tarot.jpg", 'rb'), caption=reply_text)


async def four_card_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_text = f""
    reading = Reading()
    four_card = reading.four_card()
    for card in four_card:
        reversed = "Reversed" if card['is_reversed'] else "Upright"
        reply_text += f"{card['title']}: {card['name']} ({reversed}) \n"
    images = TarotImage(four_card)
    await context.bot.send_photo(update.effective_chat.id, open("tarot.jpg", 'rb'), caption=reply_text)


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("three_card", three_card_command))
    app.add_handler(CommandHandler("four_card", four_card_command))


    # Errors
    app.add_error_handler(error)
    print('Polling...')
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()
