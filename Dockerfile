FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/tweepy_bots2.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "tweepy_bots2.py"]