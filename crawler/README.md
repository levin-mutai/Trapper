# Trapper

This project demonstrates a news web scraper built using Scrapy framework, deployed using Scrapyd, and monitored using ScrapydWeb.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Scraper](#running-the-scraper)
  - [Monitoring with ScrapydWeb](#monitoring-with-scrapydweb)
- [Logs](#logs)
- [Contributing](#contributing)


## Project Structure

. <br>
├── logs/ <br>
├── trapper/ <br>
├── README.md <br>
├── requirements.txt <br>
├── run.sh <br>
├── scrapy.cfg <br>
├── scrapydweb_settings_v10.py <br>
└── setup.py


- `logs/`: Log files for Scrapyd and ScrapydWeb.
- `trapper/`: Scrapy project directory.This is where you will find the spiders
- `README.md`: This file.
- `requirements.txt`: Project dependencies.
- `run.sh`: Script to run the scraper, deploy, and monitor.
- `scrapy.cfg`: Scrapy project configuration.
- `scrapydweb_settings_v10.py`: ScrapydWeb settings.
- `setup.py`: Project setup and metadata.


## Getting Started

### Prerequisites

- Python 3.7 and above
- Scrapy
- Scrapyd
- scrapyd-client
- ScrapydWeb
- postgresql db

### Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/levin-mutai/trapper.git

   cd trapper

   ```
### usage

#### Running the scraper
1. Install requirements

```python
    pip install -r requirements.txt
```
2. Running the scrapper.

```sh
    sudo chmod +x run.sh

    ./run.sh
```
#### Monitoring with scrapydweb

After running run.sh, scrapyweb is started automaticall. You can access it from:

```html
    http://localhost:8000
```

### Logs
`logs/scrapyd_logs.txt`: Scrapyd server logs. <br>
`logs/scrapydweb_logs.txt`: ScrapydWeb logs.
### Contributing
Contributions are welcome! Feel free to create issues or pull requests (only if you have access to this repo).