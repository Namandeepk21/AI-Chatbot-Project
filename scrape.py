import requests
#*This line imports the requests library to handle HTTP requests.
from bs4 import BeautifulSoup
#*This line imports the BeautifulSoup class from the bs4 library to parse HTML content.
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #*This function takes a URL as input, sends an HTTP GET request to fetch the webpage content, and parses it using BeautifulSoup.

    text = soup.get_text(separator=" ")
    #*This block extracts the text content from the parsed HTML, using a space as a separator between different text elements.

    clean_text = " ".join(text.split())
    #*This line cleans up the extracted text by removing extra whitespace and joining the words with a single space.

    return clean_text
#*This line returns the cleaned text content of the webpage.


if __name__ == "__main__":
    website_text = scrape_website("https://botpenguin.com/")
    print(website_text[:1000])  
    #*This block tests the scrape_website function by scraping text from a specified website and printing the first 1000 characters of the scraped text.
