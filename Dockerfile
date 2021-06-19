FROM python:3-alpine as builder

COPY ["bot.py", "/opt/"]
COPY ["items/", "/opt/items/"]
COPY requirements.txt requirements.txt

RUN  pip3 install --no-cache-dir -r requirements.txt

FROM builder

CMD python3 /opt/bot.py
