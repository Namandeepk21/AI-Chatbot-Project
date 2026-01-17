def process_text(text, max_length=2000):
    return text[:max_length]
#*This function takes a string 'text' and an optional 'max_length' parameter (default is 2000).


if __name__ == "__main__":
    from scrape import scrape_website
    #*This line imports the scrape_website function from the scrape.py file for testing purposes.

    raw_text = scrape_website("https://botpenguin.com/")
    processed = process_text(raw_text)
    print(processed)
#*This block tests the process_text function by scraping text from a specified website and printing the processed (length-limited) text.