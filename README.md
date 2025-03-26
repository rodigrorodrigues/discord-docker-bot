# Discord Docker Bot

## 📋 Description

Discord bot developed to control Docker containers through simple Discord commands.

## 🛠️ Technologies Used

- Python 3.9
- discord.py
- Docker SDK for Python
- python-dotenv

## 🚀 Features

- Start container (`!start`)
- Stop container (`!stop`)
- Automatic event and error logging

## ⚙️ Setup

### Prerequisites

- Python 3.9 or higher
- Docker installed
- A registered Discord application to obtain the token

### Environment Variables

Create an `.env` file in the project root with:

```env
DISCORD_TOKEN=your_discord_token
DOCKER_IMAGE=docker/image
DOCKER_CONTAINER_NAME=containerName
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/rodigrorodrigues/discord-docker-bot.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the bot:

```bash
python src/bot.py
```

### Using Docker Compose

To run using Docker Compose:

```bash
docker-compose up --build
```

## 📌 Bot Commands

- `!start` - Starts the container
- `!stop` - Stops the container

## 🧪 Tests

To run the tests:

```bash
python -m unittest tests/test_docker_service.py
```

## 📄 License

This project is under the MIT license.
