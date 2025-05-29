import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Solar_storm"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)
    data = []
    for idx, link in enumerate(links, start=1):
        tag_str = str(link)
        href = link.get("href")

        full_url = urljoin(url, href)
        data.append({
            "sl.no": idx,
            "hyperlink tag": tag_str,
            "link": full_url
        })

    df = pd.DataFrame(data, columns=["sl.no", "hyperlink tag", "link"])
    print(df)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
