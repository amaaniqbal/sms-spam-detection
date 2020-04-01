FROM python:3.8-slim-buster

LABEL "com.github.actions.name"="SMS Spam Detection Action"
LABEL "com.github.actions.description"="SMS Spam Detection Action enables a user to check if any given message is a `spam` or a `ham`"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="green"
LABEL "repository"="https://github.com/amaaniqbal/sms-spam-detection"
LABEL "homepage"="https://github.com/amaaniqbal/sms-spam-detection"
LABEL "maintainer"="Amaan Iqbal <amaaniqbal2786@gmail.com>"
LABEL "version" = "1.x"

RUN pip install --upgrade pip
RUN pip install nltk
RUN pip install pandas
RUN pip install sklearn

COPY main.py /main.py
COPY entrypoint.sh /entrypoint.sh

RUN pwd
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
