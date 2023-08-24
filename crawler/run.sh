#!/bin/bash

# Start Scrapyd server in the background
scrapyd > ./logs/scrapyd_logs.txt 2>&1 & 

# Deploy your Scrapy project using scrapyd-deploy
scrapyd-deploy default

# Start ScrapydWeb in the background
scrapydweb  > ./logs/scrapydweb_logs.txt 2>&1 &