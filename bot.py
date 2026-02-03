import asyncio
import logging

from openai import OpenAI
from openai import OpenAIError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("telegram-bot")


client = OpenAI(api_key=settings["OPENAI_API_KEY"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Привет! Отправь сообщение, и я отвечу с помощью ИИ."
        )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    user_text = update.message.text.strip()
    if not user_text:
        return

    await update.message.chat.send_action("typing")

    try:
        response = await asyncio.to_thread(
            client.responses.create,
            model=settings["OPENAI_MODEL"],
            input=[
                {"role": "system", "content": settings["SYSTEM_PROMPT"]},
                {"role": "user", "content": user_text},
            ],
        )
        answer = response.output_text.strip() if response.output_text else ""
    except OpenAIError as exc:
        logger.exception("OpenAI API error")
        await update.message.reply_text(
            "Произошла ошибка при обращении к модели. Попробуй позже."
        )
        return
    except Exception:
        logger.exception("Unexpected error")
        await update.message.reply_text(
            "Что-то пошло не так. Попробуй позже."
        )
        return

    if not answer:
        answer = "Не удалось получить ответ. Попробуй переформулировать запрос."

    await update.message.reply_text(answer)


def main() -> None:
    application = (
        ApplicationBuilder()
        .token(settings["TELEGRAM_TOKEN"])
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    logger.info("Telegram bot started")
    application.run_polling()


if __name__ == "__main__":
    main()
