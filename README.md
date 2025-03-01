# Hacker News Web Scraper

## Overview
This project is a Python-based web scraper that extracts article titles, links, and upvote counts from **Hacker News**. It identifies the most upvoted article and displays its details.

## Features
- Scrapes article titles and links from **Hacker News**.
- Extracts upvote counts for each article.
- Identifies and prints the most upvoted article.

## Technologies Used
- **Python**
- **BeautifulSoup** (for web scraping)
- **Requests** (for fetching webpage content)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/hacker-news-scraper.git
   cd hacker-news-scraper
   ```
2. Install dependencies:
   ```sh
   pip install beautifulsoup4 requests
   ```

## Usage
Run the script using:
```sh
python scraper.py
```

### Expected Output
The script prints the **most upvoted** article title, its link, and the number of upvotes.

Example output:
```
Most upvoted article: "Example Title" (https://example.com) with 125 upvotes.
```

## Notes
- The website structure may change, so ensure the HTML elements are correctly targeted.
- Some articles may not have upvotes, so error handling is included.

## Contributing
Feel free to submit issues or pull requests to enhance functionality.

## License
This project is licensed under the MIT License.

