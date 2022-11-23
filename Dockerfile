FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app
#この環境変数で、flaskコマンド実行時の実行するpythonモジュールの名前を指定する。
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt