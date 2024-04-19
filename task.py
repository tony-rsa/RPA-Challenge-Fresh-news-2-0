from RPA.Robocloud.Items import get_work_item, set_work_item_variable
from RPA.Excel.Files import Workbook
from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
from RPA.Logging import RobotLogger
from datetime import datetime, timedelta
import os
import re

logger = RobotLogger()

class NewsBot:
    def __init__(self):
        self.search_phrase = None
        self.news_category = None
        self.num_months = None
        self.browser = Selenium()
        self.http = HTTP()

    def process_work_item(self):
        """Retrieve parameters from Robocloud work item."""
        work_item = get_work_item()
        self.search_phrase = work_item["search_phrase"]
        self.news_category = work_item["news_category"]
        self.num_months = int(work_item["num_months"])

    def extract_data(self):
        """Extract news data from the website."""
        logger.info(f"Extracting news data for search phrase '{self.search_phrase}' and category '{self.news_category}'...")
        self.browser.open_available_browser("https://news.yahoo.com")
        self.browser.input_text("name=pc", self.search_phrase)
        self.browser.press_keys("name=pc", "ENTER")
        self.browser.wait_until_page_contains_element("class=yfin-tile")
        # If a news category is specified, select it from the dropdown menu
        if self.news_category:
            self.browser.click_link("text=" + self.news_category)
        # Extract titles, dates, descriptions, and picture URLs of news articles
        titles = self.browser.get_webelements("class=yfin-tile h3")
        dates = self.browser.get_webelements("class=yfin-tile time")
        descriptions = self.browser.get_webelements("class=yfin-tile p")
        picture_urls = self.browser.get_webelements("class=yfin-tile img")
        data = []
        # Calculate the start date based on the specified number of months
        start_date = datetime.now() - timedelta(days=self.num_months * 30)
        for idx, (title, date, description, picture_url) in enumerate(zip(titles, dates, descriptions, picture_urls)):
            # Convert the date string to a datetime object
            news_date = datetime.strptime(date.text, "%b %d, %Y")
            # Filter out articles outside the specified time period
            if news_date >= start_date:
                # Count occurrences of search phrase in title and description
                search_phrase_count = title.text.count(self.search_phrase) + description.text.count(self.search_phrase)
                # Determine if title or description contains any amount of money
                contains_money = bool(re.search(r'\$[\d,]+(?:\.\d{1,2})?|\d+\s(?:USD|dollars?)', title.text)) or bool(re.search(r'\$[\d,]+(?:\.\d{1,2})?|\d+\s(?:USD|dollars?)', description.text))
                data.append({
                    "title": title.text,
                    "date": date.text,
                    "description": description.text,
                    "picture_url": picture_url.get_attribute("src"),
                    "search_phrase_count": search_phrase_count,
                    "contains_money": contains_money
                })
        return data

    def download_images(self, data):
        """Download images associated with news articles."""
        logger.info("Downloading images...")
        for idx, entry in enumerate(data):
            image_url = entry["picture_url"]
            filename = f"picture_{idx + 1}.jpg"
            image_path = os.path.join("outputs", "images", filename)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            self.http.download(image_url, image_path)
            entry["image_path"] = image_path  # Update the data with image path

    def save_to_excel(self, data):
        """Save news data to an Excel file."""
        logger.info("Saving news data to Excel...")
        wb = Workbook()
        wb.new_sheet("News Data")
        wb.append_row(["Title", "Date", "Description", "Picture URL", "Search Phrase Count", "Contains Money"])
        for entry in data:
            wb.append_row([
                entry["title"],
                entry["date"],
                entry["description"],
                entry["picture_url"],
                entry["search_phrase_count"],
                entry["contains_money"]
            ])
        excel_file = os.path.join("outputs", "news_data.xlsx")
        os.makedirs(os.path.dirname(excel_file), exist_ok=True)
        wb.save(excel_file)

    def run(self):
        """Main execution method."""
        try:
            logger.info("Starting script execution...")
            self.process_work_item()
            data = self.extract_data()
            self.download_images(data)
            self.save_to_excel(data)
            logger.info("Script execution completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            raise

if __name__ == "__main__":
    # Instantiate NewsBot and run the script
    news_bot = NewsBot()
    news_bot.run()
  
