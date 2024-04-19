# My RPA News Scraper Solution
---
> An automated web scraping bot to extract news data from various websites.
---

## Overview

This project automates the process of extracting news articles from a news website using Robotic Process Automation (RPA). It leverages the RPA framework and Selenium for web automation to streamline the extraction process.

## Features

- Search for news articles based on a specified search phrase.
- Filter news articles by category, section, or topic.
- Extract data such as title, date, description, and picture URL for each news article.
- Store extracted data in an Excel file for further analysis or reporting.
- Download images associated with news articles and link them to the corresponding Excel entry.
- Count occurrences of the search phrase in the title and description of each news article.
- Identify if the title or description contains any monetary values.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/tony-rsa/rpa-news-scraper.git
   ```

2. Navigate to the project directory:
   ```bash
   cd rpa-news-scraper
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and place it in the project directory.

## Usage

1. Open the `config.ini` file and set the desired parameters:
   - `search_phrase`: The keyword or phrase to search for in news articles.
   - `news_category`: Optional parameter to filter news articles by category, section, or topic.
   - `num_months`: Specifies the number of months for which to retrieve news articles (0 or 1 for the current month, 2 for the current and previous month, and so on).

2. Run the main Python script to start the automation process:
   ```bash
   python main.py
   ```

3. After execution, the extracted data will be saved in an Excel file (`news_data.xlsx`) located in the `output` directory.

## Parameters

- **Search Phrase**: The keyword or phrase to search for in news articles.
- **News Category/Section/Topic**: Optional parameter to filter news articles by category, section, or topic.
- **Number of Months**: Specifies the number of months for which to retrieve news articles (0 or 1 for the current month, 2 for the current and previous month, and so on).

These parameters can be provided via the `config.ini` file or as command-line arguments.

## Directory Structure

- **src/**: Contains the main Python script for the RPA News Scraper.
- **output/**: Directory to store output files such as Excel files and downloaded images.
- **tests/**: Directory containing unit tests for the RPA News Scraper.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Please let me know if there are any additional details you'd like to include or modify!
