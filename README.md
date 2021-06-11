# News generator

Generator for random funny news

## Start 

First of all clone repo`git clone https://github.com/CoolCoderCarl/newsGenerator` then go to dir `cd newsGenerator/`

### Systemd method
1) `cp english_absurd_news_bot.* /etc/systemd/system/`
2) `systemctl daemon-reload`
3) `systemctl start english_absurd_news_bot.service` 
4) `systemctl enable --now english_absurd_news_bot.timer` 

### Docker method
1) `docker build -t news_generator:1.0 .`
2) `docker run -d --restart=always --name news_generator -e API_TOKEN=YOUTOKENHERE news_generator:1.0`