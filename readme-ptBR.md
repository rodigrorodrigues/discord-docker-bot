# Discord Docker Bot

## 📋 Descrição

Bot do Discord desenvolvido para controlar containers Docker através de comandos simples no Discord.

## 🛠️ Tecnologias Utilizadas

- Python 3.9
- discord.py
- Docker SDK para Python
- python-dotenv

## 🚀 Funcionalidades

- Iniciar o container (`!start`)
- Parar conteiner (`!stop`)
- Logging automático de eventos e erros

## ⚙️ Configuração

### Pré-requisitos

- Python 3.9 ou superior
- Docker instalado
- Uma aplicação registrada no Discord para obter o token

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
DISCORD_TOKEN=seu_token_do_discord
DOCKER_IMAGE=imagem/docker
DOCKER_CONTAINER_NAME=nomeDoConteiner
```

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/discord-docker-bot.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o bot:

```bash
python src/bot.py
```

### Usando Docker Compose

Para executar usando Docker Compose:

```bash
docker-compose up --build
```

## 📌 Comandos do Bot

- `!start` - Inicia o conteiner
- `!stop` - Para o conteiner

## 🧪 Testes

Para executar os testes:

```bash
python -m unittest tests/test_docker_service.py
```

## 📄 Licença

Este projeto está sob a licença MIT.
