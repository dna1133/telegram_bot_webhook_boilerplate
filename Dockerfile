FROM python:3.12-slim as builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without=dev -o requirements.txt 

RUN pip install --upgrade virtualenv
RUN virtualenv -p python venv

RUN pip install -r requirements.txt

FROM builder as final

COPY --from=builder app/venv app/venv

WORKDIR /app

COPY . .

CMD ["python", "-m", "src.tg_bot_webhook.bot.bot"]