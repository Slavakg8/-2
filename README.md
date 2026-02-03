# Telegram AI Bot

Простой Telegram-бот на Python, который отвечает на сообщения через модель OpenAI.

## Настройка

1. Создайте бота через [@BotFather](https://t.me/BotFather) и получите токен.
2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Установите переменные окружения:

```bash
export TELEGRAM_TOKEN="ваш_телеграм_токен"
export OPENAI_API_KEY="ваш_openai_api_key"
# необязательно:
export OPENAI_MODEL="gpt-4o-mini"
export SYSTEM_PROMPT="Ты полезный ассистент. Отвечай кратко и по делу."
```

4. Запустите:

```bash
python bot.py
```

## Команды

- `/start` — приветственное сообщение.

Бот отвечает на любые текстовые сообщения.
