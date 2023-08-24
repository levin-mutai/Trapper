#!/bin/bash


# Specify the directory path
logs_dir="./logs"

# Check if the directory exists
if [ ! -d "$logs_dir" ]; then
    echo "Creating directory $logs_dir"
    mkdir "$logs_dir"
fi
# Start Scrapyd server in the background
scrapyd > ./logs/scrapyd_logs.txt 2>&1 & 

# Deploy your Scrapy project using scrapyd-deploy
scrapyd-deploy default

# Start ScrapydWeb in the background
scrapydweb  > ./logs/scrapydweb_logs.txt 2>&1 &

cat ./logs/scrapyd_logs.txt