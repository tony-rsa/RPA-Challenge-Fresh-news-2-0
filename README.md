# NewsBot-Automation

This is an RPA (Robotic Process Automation) project designed to automate the process of extracting news articles from a news website. The project utilizes the RPA framework along with Selenium for web automation.

## Overview

The purpose of this project is to demonstrate the automation of tedious but critical business processes, specifically the extraction of news data from a news website. By automating this process, we aim to save time and effort for businesses that rely on staying up-to-date with the latest news in their industry.

## Features

- Search for news articles based on a given search phrase.
- Filter news articles by category/section/topic.
- Extract data such as title, date, description, and picture URL for each news article.
- Store extracted data in an Excel file.
- Download images associated with news articles and specify the file name in the Excel file.
- Count occurrences of the search phrase in the title and description of each news article.
- Determine if the title or description contains any amount of money.

## Usage

To use this RPA News Scraper, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Set up the required parameters such as the search phrase, news category, and number of months for which news articles should be retrieved.
4. Run the main script to start the automation process.

## Parameters

The process accepts the following parameters:

- **Search phrase:** The phrase to search for in news articles.
- **News category/section/topic:** The category, section, or topic of news articles to filter by.
- **Number of months:** The number of months for which to retrieve news articles (0 or 1 for the current month, 2 for the current and previous month, and so on).

These parameters can be provided via command-line arguments or through a configuration file.

## Directory Structure

- **src/**: Contains the main Python script for the RPA News Scraper.
- **output/**: Directory to store output files such as Excel files and downloaded images.
- **tests/**: Directory containing unit tests for the RPA News Scraper.
- **docs/**: Documentation files, including this README.md.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
