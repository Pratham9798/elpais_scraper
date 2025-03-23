from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator
import requests
from PIL import Image
from io import BytesIO
from collections import Counter

# BrowserStack credentials
BROWSERSTACK_USERNAME = "prathamgupta_Zpm7vc"
BROWSERSTACK_ACCESS_KEY = "YVE4hxETfy6fXbVunRV1"

# Function to initialize BrowserStack driver
def init_browserstack_driver(capabilities):
    options = webdriver.ChromeOptions()
    for key, value in capabilities.items():
        options.set_capability(key, value)
    return webdriver.Remote(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options,
    )

# Function to scrape El País articles
def scrape_el_pais(driver):
    # Visit El País Opinion section directly
    driver.get("https://elpais.com/opinion")
    print("Page Title:", driver.title)
    print("Page URL:", driver.current_url)

    # Wait for the articles to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".c c-o c-d c--c c--m-n"))
        )
    except Exception as e:
        print("Error loading articles:", e)
        return []

    # Scrape the first 5 articles
    articles = driver.find_elements(By.CSS_SELECTOR, ".c c-o c-d c--c c--m-n")[:5]
    scraped_data = []

    for article in articles:
        try:
            title = article.find_element(By.CSS_SELECTOR, "h2").text
            content = article.find_element(By.CSS_SELECTOR, "p").text
            image_element = article.find_element(By.CSS_SELECTOR, "img")
            image_url = image_element.get_attribute("src")

            # Download and save the cover image
            image_name = f"{title[:20]}.jpg".replace("/", "_")
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.save(image_name)

            scraped_data.append({
                "title": title,
                "content": content,
                "image": image_name,
            })
        except Exception as e:
            print("Error scraping article:", e)

    return scraped_data

# Function to translate titles
def translate_titles(scraped_data):
    translator = Translator()
    for article in scraped_data:
        try:
            translated_title = translator.translate(article["title"], src="es", dest="en").text
            article["translated_title"] = translated_title
        except Exception as e:
            print("Error translating title:", e)
    return scraped_data

# Function to analyze translated headers
def analyze_headers(scraped_data):
    all_words = []
    for article in scraped_data:
        words = article["translated_title"].split()
        all_words.extend(words)

    word_count = Counter(all_words)
    repeated_words = {word: count for word, count in word_count.items() if count > 2}
    return repeated_words

# Function to run on BrowserStack
def run_on_browserstack():
    capabilities = [
        {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "os_version": "10"},
        {"browserName": "Firefox", "browserVersion": "latest", "os": "Windows", "os_version": "10"},
        {"browserName": "Safari", "browserVersion": "latest", "os": "OS X", "os_version": "Big Sur"},
        {"browserName": "Chrome", "browserVersion": "latest", "os": "OS X", "os_version": "Big Sur"},
        {"browserName": "iPhone", "device": "iPhone 12", "os_version": "14", "real_mobile": "true"},
    ]

    for cap in capabilities:
        driver = init_browserstack_driver(cap)
        print(f"Running on {cap['browserName']} {cap.get('browserVersion', '')} {cap.get('os', '')} {cap.get('os_version', '')}")
        try:
            # Scrape and process data
            scraped_data = scrape_el_pais(driver)
            scraped_data = translate_titles(scraped_data)
            repeated_words = analyze_headers(scraped_data)

            # Print results
            for article in scraped_data:
                print(f"Title (Spanish): {article['title']}")
                print(f"Title (English): {article['translated_title']}")
                print(f"Content: {article['content'][:100]}...")  # Print first 100 chars
                print(f"Image saved as: {article['image']}")
                print("-" * 50)

            print("Repeated words in translated headers:")
            for word, count in repeated_words.items():
                print(f"{word}: {count}")
        finally:
            driver.quit()

# Main execution
if __name__ == "__main__":
    # Run locally first
    options = Options()
    options.add_argument("--lang=es")
    driver = webdriver.Chrome(options=options)
    scraped_data = scrape_el_pais(driver)
    scraped_data = translate_titles(scraped_data)
    repeated_words = analyze_headers(scraped_data)

    # Print results
    for article in scraped_data:
        print(f"Title (Spanish): {article['title']}")
        print(f"Title (English): {article['translated_title']}")
        print(f"Content: {article['content'][:100]}...")  # Print first 100 chars
        print(f"Image saved as: {article['image']}")
        print("-" * 50)

    print("Repeated words in translated headers:")
    for word, count in repeated_words.items():
        print(f"{word}: {count}")

    driver.quit()

    # Run on BrowserStack
    run_on_browserstack()