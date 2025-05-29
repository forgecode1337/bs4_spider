# 🕷️ bs4_spider.py

A lightweight Python web crawler for reconnaissance and data extraction.  
Built using `requests` and `BeautifulSoup4`, this script crawls websites, follows links, and extracts all HTML form actions and methods.

## 🚀 Features

- Recursive crawling up to a specified depth
- Extracts all `<form>` actions and methods
- Resolves and follows relative and absolute links
- Simple and minimal—no browser required

## 🛠️ Requirements

- Python 3.x  
- Install dependencies:

```bash
pip install requests beautifulsoup4
```

## ⚙️ Usage

```bash
python3 bs4_spider.py <URL>
```
This will:
- Start crawling http://example.com
- Follow all links (up to 2 levels deep by default)
- Print any forms found with their action and method
  
## 🔒 Note

This script is for educational and authorized use only. Always get permission before scanning or crawling external websites.

## 📁 File Structure

```
bs4_spider.py     # Main crawler script
README.md         # This file
```

## 👨‍💻 Author

ForgeCode
