#!/bin/bash

# Get the directory name of the script being executed
script_dir=$(dirname "$0")

# Get the current working directory
current_dir=$(pwd)

# Compare the script directory with the current directory
if [ "$script_dir" == "$current_dir" ]; then
  echo "Script is being run from the same directory."
else
  echo "Changing to the required directory."
  cd $script_dir
fi

logs_dir="./logs"

# Check if logs directory exists
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

cd $current_dir

