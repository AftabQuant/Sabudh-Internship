import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt23790740/?ref_=hm_fanfav_tt_i_3_pd_fp1_r"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

storyline = ""
storyline_tag = soup.find('span', {'data-testid': 'plot-l'})
if not storyline_tag:
    storyline_tag = soup.find('span', {'data-testid': 'plot-xl'})  # fallback
if storyline_tag:
    storyline = storyline_tag.text.strip()
else:
    storyline = "Storyline not found."

print("## Storyline\n")
print(storyline, "\n")

reviews_link = soup.find('a', {'data-testid': 'reviews-header'})
if reviews_link:
    reviews_url = "https://www.imdb.com" + reviews_link['href']
else:
    reviews_url = url.split('?')[0] + "reviews"

reviews_response = requests.get(reviews_url, headers=headers)
reviews_soup = BeautifulSoup(reviews_response.text, 'html.parser')

review_blocks = reviews_soup.find_all('div', class_='review-container', limit=3)
if not review_blocks:
    review_blocks = reviews_soup.find_all('div', {'data-testid': 'review-container'}, limit=3)

print("## First 3 Reviews\n")
if review_blocks:
    for idx, review in enumerate(review_blocks, 1):
        title_tag = review.find('a', class_='title')
        if not title_tag:
            title_tag = review.find('span', {'data-testid': 'review-title'})
        review_title = title_tag.text.strip() if title_tag else ""
        content_tag = review.find('div', class_='text')
        if not content_tag:
            content_tag = review.find('div', {'data-testid': 'review-content'})
        review_content = content_tag.text.strip() if content_tag else ""
        print(f"**Review {idx}:**")
        if review_title:
            print(f"*{review_title}*")
        print(review_content, "\n")
else:
    print("No reviews found or IMDb page structure has changed.")
