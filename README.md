El País Web Scraping Project

This project demonstrates web scraping, API integration, and cross-browser testing using Selenium and BrowserStack. The goal is to scrape articles from the Opinion section of the Spanish news website El País, translate the article titles to English, and analyze the translated headers for repeated words. The solution is tested across multiple browsers and devices using BrowserStack.

Table of Contents

1) Features
2) Technologies Used
3) Setup and Installation
4) How It Works
5) Running the Project
6) BrowserStack Integration
7) Contributing
8) License

Features
Web Scraping: Scrapes the first five articles from the Opinion section of El País.
Translation: Translates article titles from Spanish to English using the Google Translate API.
Text Analysis: Identifies and counts repeated words in the translated titles.
Image Download: Downloads and saves the cover image of each article.
Cross-Browser Testing: Runs the solution on multiple browsers and devices using BrowserStack.

Technologies Used
Python: The programming language used for scripting.
Selenium: For web scraping and browser automation.
Google Translate API: For translating article titles.
BrowserStack: For cross-browser testing.
Pillow (PIL): For handling image downloads.
Requests: For downloading images.
Googletrans: Python library for Google Translate API integration.

Setup and Installation

Prerequisites
1) Python 3.x: Install Python from python.org.
2) BrowserStack Account: Sign up at BrowserStack and get your username and access key.
3) Google Cloud Translate API Key (Optional): If using the paid version of Google Translate API.

Installation

Clone the repository:
git clone https://github.com/your-username/elpais-scraper.git
cd elpais-scraper

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install the required dependencies:
pip install selenium requests pillow googletrans==4.0.0-rc1

Update the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY in the script with your BrowserStack credentials.

How It Works

1)Scraping:
The script navigates to the El País Opinion section.
It scrapes the first five articles, including their titles, content, and cover images.

2) Translation:
The article titles are translated from Spanish to English using the Google Translate API.

3) Text Analysis:
The script identifies words that are repeated more than twice in the translated titles.

4) Cross-Browser Testing:
The solution is tested across multiple browsers and devices using BrowserStack.

Running the Project

Locally
Run the script:
python elpais_scraper.py
The script will:

Print the article titles (in Spanish and English).
Print the first 100 characters of the article content.
Save the cover images locally.
Print repeated words in the translated titles.

On BrowserStack
Update the capabilities list in the script with your desired browser and device configurations.

Run the script:
python elpais_scraper.py
The script will execute on BrowserStack across the specified browsers and devices.

BrowserStack Integration

To run the script on BrowserStack:
Sign up for a BrowserStack account.
Replace your_browserstack_username and your_browserstack_access_key in the script with your credentials.
Update the capabilities list with your desired browser and device configurations.

Example capabilities:

capabilities = [
    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "os_version": "10"},
    {"browserName": "Firefox", "browserVersion": "latest", "os": "Windows", "os_version": "10"},
    {"browserName": "Safari", "browserVersion": "latest", "os": "OS X", "os_version": "Big Sur"},
    {"browserName": "iPhone", "device": "iPhone 12", "os_version": "14", "real_mobile": "true"},
]


License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

El País for the content.
BrowserStack for cross-browser testing.
Google Translate API for translation.
