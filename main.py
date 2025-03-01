from bs4 import BeautifulSoup
import requests

# Get the HTML content of the page
url = "https://appbrewery.github.io/news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract article titles and links correctly
article_tags = soup.find_all("span", class_="titleline")
article_texts = [article.find("a").text for article in article_tags]  # Extracting text
article_links = [article.find("a")["href"] for article in article_tags]  # Extracting href attribute

# Extract upvotes
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# Find the index of the most upvoted article
if article_upvotes:  # Check if there are any upvotes to avoid index errors
    biggest_upvote = article_upvotes.index(max(article_upvotes))
    print(article_texts[biggest_upvote], article_links[biggest_upvote], article_upvotes[biggest_upvote])
else:
    print("No upvotes found.")
