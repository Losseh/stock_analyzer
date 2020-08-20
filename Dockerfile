FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip
RUN pip install yfinance

RUN mkdir -p /home/pi/stock_analyzer
COPY . /home/pi/stock_analyzer

ENTRYPOINT ["python", "/home/pi/stock_analyzer/main.py"]