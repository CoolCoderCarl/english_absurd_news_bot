# News generator

Generator for random funny news  
API - https://github.com/eternnoir/pyTelegramBotAPI

## Prehistory
This bot was developed for fun and having a good time

> Why not create a funny bot ?
> (c) Author

Enjoy.

## Start 

First clone repo `git clone https://github.com/CoolCoderCarl/newsGenerator` then go to dir `cd newsGenerator/`

### Docker Compose method
`docker-compose up -d`

### Systemd method
1) `cp english_absurd_news_bot.* /etc/systemd/system/`
2) `systemctl daemon-reload`
3) `systemctl start english_absurd_news_bot.service` 
4) `systemctl enable --now english_absurd_news_bot.timer` 

### Docker build method
1) `docker build -t news_generator:1.0 .`
2) `docker run -d --restart=always --name news_generator -e API_TOKEN=BOT_TOKEN news_generator:1.0`

### P.S.
Or just pull it from here - https://hub.docker.com/repository/docker/h0d0user/news_generator  
Like this - `docker pull h0d0user/news_generator:latest`
