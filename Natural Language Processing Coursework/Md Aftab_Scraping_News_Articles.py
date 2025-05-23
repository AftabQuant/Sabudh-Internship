import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Base URL of Indian Express
BASE_URL = "https://indianexpress.com/"

# Headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def fetch_homepage():
    """Fetch the homepage HTML content"""
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print("Failed to fetch homepage:", e)
        return None

def extract_article_links(html):
    """Extract article links from the homepage"""
    soup = BeautifulSoup(html, 'html.parser')
    article_links = set()

    # Targeting major headlines (Top News / Latest News)
    for section in soup.find_all('div', class_='nation'):
        for a_tag in section.find_all('a', href=True):
            link = a_tag['href']
            if link.startswith('https://indianexpress.com/article/') and 'liveblog' not in link:
                article_links.add(link)

    # Additional links from the main content
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith('https://indianexpress.com/article/') and 'liveblog' not in link:
            article_links.add(link)

    # Return only the first 30 unique links
    return list(article_links)[:30]

def fetch_article_content(url):
    """Fetch the full content of a news article"""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').get_text(strip=True)

        # Extract the article body paragraphs
        paragraphs = soup.find_all('p')
        full_text = ' '.join(p.get_text(strip=True) for p in paragraphs)

        return title, full_text
    except Exception as e:
        print(f"Error fetching article: {url}\n{e}")
        return None, None

def main():
    homepage_html = fetch_homepage()
    if not homepage_html:
        return

    article_links = extract_article_links(homepage_html)
    print(f"Found {len(article_links)} article links.")

    data = []
    for idx, url in enumerate(article_links):
        print(f"Scraping {idx + 1}/{len(article_links)}: {url}")
        title, full_text = fetch_article_content(url)
        if title and full_text:
            data.append({
                "NEWS_TITLE": title,
                "NEWS_LINK": url,
                "FULL_SCRAPED_TEXT": full_text
            })

        # Polite delay between requests
        time.sleep(random.uniform(1.5, 3.5))

    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv("indian_express_scraped_news.csv", index=False)
    print("✅ Scraping completed. Saved to 'indian_express_scraped_news.csv'.")

if __name__ == "__main__":
    main()