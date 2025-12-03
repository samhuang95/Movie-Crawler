import requests
from bs4 import BeautifulSoup
import time
import csv

def scrape_page(page_num, writer):
    url = f"https://ssr1.scrape.center/page/{page_num}"
    print(f"Scraping {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.select('.el-card.item')

        for item in items:
            # Title
            title_tag = item.select_one('h2.m-b-sm')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            # Categories
            categories = [cat.get_text(strip=True) for cat in item.select('.categories .category span')]
            categories_str = ', '.join(categories)

            # Score
            score_tag = item.select_one('.score')
            score = score_tag.get_text(strip=True) if score_tag else "N/A"

            # Cover Image
            cover_tag = item.select_one('.cover')
            cover_url = cover_tag['src'] if cover_tag else "N/A"

            # Write to CSV
            writer.writerow([title, cover_url, score, categories_str])

            print(f"Saved: {title}")

    except Exception as e:
        print(f"Error scraping page {page_num}: {e}")

def main():
    # Open the CSV file for writing
    with open('movie.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Title', 'Cover URL', 'Score', 'Categories'])

        for i in range(1, 11):
            scrape_page(i, writer)
            # Be polite and wait a bit between requests
            time.sleep(1)

    print("Done! Data saved to movie.csv")

if __name__ == "__main__":
    main()
