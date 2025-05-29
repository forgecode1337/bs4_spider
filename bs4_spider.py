# crawler_bs4.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

def crawl(url, max_depth=2, visited=None, depth=0):
    if visited is None:
        visited = set()

    if depth > max_depth or url in visited:
        return

    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print(f"Failed: {url} ({e})")
        return

    visited.add(url)
    print(f"[*] Crawling: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print forms
    for form in soup.find_all('form'):
        action = form.get('action')
        method = form.get('method', 'get').lower()
        print(f"[FORM] action={action}, method={method}")

    # Extract and follow links
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            joined_url = urljoin(url, href)
            parsed = urlparse(joined_url)
            if parsed.scheme.startswith('http'):
                crawl(joined_url, max_depth, visited, depth + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawler_bs4.py <URL>")
        sys.exit(1)

    start_url = sys.argv[1]
    crawl(start_url)
