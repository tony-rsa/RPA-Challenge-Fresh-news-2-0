# RPA-Challenge-Fresh-news-2-0
---

> An automated web scraping bot to extract 

--

# NewsBot Automation

The NewsBot Automation project is designed to automate the extraction of news data from a website. It uses Selenium WebDriver to interact with the website and extract news articles based on search parameters provided by the user.

## Installatio
To use the NewsBot Automation project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/newsbot-automation.git
```

2. Navigate to the project directory:

```bash
cd newsbot-automation
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Make sure you have Chrome browser installed on your system. If not, download and install it from [here](https://www.google.com/chrome/).

## Usage

To use the NewsBot Automation project, follow these steps:

1. Open the `main.py` file in your preferred text editor.

2. Modify the `search_phrase`, `news_category`, and `num_months` variables in the `main()` function to specify your search parameters.

3. Run the `main.py` file:

```bash
python main.py
```

4. The program will launch a Chrome browser, navigate to the news website, extract news data based on your search parameters, and save it to an Excel file (`news_data.xlsx`) in the project directory.

5. After data extraction, the program will download the associated news pictures and save them to a directory named `pictures` in the project directory.

6. Finally, the program will close the Chrome browser.

## Contributing

Contributions to the NewsBot Automation project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README provides clear instructions on how to install, use, and contribute to the project. You can customize it further based on your specific project requirements. Let me know if you need any further assistance or if there's anything else you'd like to add!
