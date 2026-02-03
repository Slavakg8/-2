import os


def _get_env(name, default=None, required=False):
    value = os.getenv(name, default)
    if required and not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


settings = {
    "TELEGRAM_TOKEN": _get_env("TELEGRAM_TOKEN", required=True),
    "OPENAI_API_KEY": _get_env("OPENAI_API_KEY", required=True),
    "OPENAI_MODEL": _get_env("OPENAI_MODEL", "gpt-4o-mini"),
    "SYSTEM_PROMPT": _get_env(
        "SYSTEM_PROMPT",
        "Ты полезный ассистент. Отвечай кратко и по делу.",
    ),
}
