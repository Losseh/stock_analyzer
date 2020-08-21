#!/bin/bash
docker rm stock_analyzer
docker build -t losseh/stock_analyzer . && docker run --name stock_analyzer losseh/stock_analyzer
