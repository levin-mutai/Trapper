
# Trapper: News Aggregator and API

Trapper is a news aggregation project built using Scrapy to fetch news from various news sites and then serves them through a FastAPI-based API. It aims to provide users with a convenient way to access news articles from different sources.

## Features

- Fetches news articles from multiple news sites.
- Provides a user-friendly API to access the fetched news.
- Allows filtering news by source, category, date, and more.

## Folder Structure

```plaintext
- .github             # GitHub-related files (actions, workflows, etc.)
- API                 # FastAPI application for serving news through an API
- crawler             # Scrapy-based news crawler
- .gitignore          # Git ignore file
- README.md           # Project documentation (you're here!)
- requirements.txt    # List of project dependencies
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/trapper.git

   # navigate to the root folder
   cd trapper

   pip install requirements.txt

   ```

2. Set up the crawler:
   - Navigate to the `crawler` directory.
   
    ```bash

    # enable execution of run.sh file

    chmod +x run.sh

    # run crawler
    ./run.sh
    
    ```


3. Set up the API:
   - Navigate to the `API` directory.
   - Install the required dependencies using `pip install -r requirements.txt`.
   - Customize the API to serve the fetched news articles.
   - Run the FastAPI application using `uvicorn api:app --reload`.

4. Access the API:
   - Open your browser or use a tool like `curl` to access the API endpoints.
   - Retrieve news articles and explore the API features.

## Contributing

We welcome contributions from the community. If you find a bug or have a feature request, please open an issue. Pull requests are also welcome!



## License

This project is licensed under the [MIT License](LICENSE).

---

