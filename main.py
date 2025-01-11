import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler, ContextTypes

from tarot_reader import Reading

# Environment Variables
load_dotenv()
TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')



# Utility Functions
def format_reading(cards):
    reply_text = ""
    for card in cards:
        reversed = "Reversed" if card["is_reversed"] else "Upright"
        reply_text += f"{card['title']}: {card['name']}({reversed})\n"
    return reply_text


async def send_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, cards):
    caption = format_reading(cards)
    print(caption)
    try:
        with open("tarot.jpg", "rb") as photo:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo, caption=caption)
    except FileNotFoundError:
        await update.message.reply_text("Error: Image Not Found")


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_text = (f"Let's start your reading, "
                  f"{update.effective_user.first_name}\n"
                  f"Pick a reading:\n"
                  f"/three_Card:\n"
                  f"The classic 'past present future' reading\n"
                  f"/four_Card: \n"
                  f"Best for a yes or no answer")

    await update.message.reply_text(reply_text)


async def tarot_reading(update: Update, context: ContextTypes.DEFAULT_TYPE, num_cards: int):
    reading = Reading(num_cards)
    await send_reading(update, context, reading.cards)


async def three_card_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await tarot_reading(update, context, num_cards=3)


async def four_card_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await tarot_reading(update, context, num_cards=4)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("three_card", three_card_command))
    app.add_handler(CommandHandler("four_card", four_card_command))

    # Errors
    app.add_error_handler(error)
    print('Polling...')
    app.run_polling()


if __name__ == "__main__":
    print('Starting...')
    main()
