from groq import Groq
#*This line imports the Groq library, which allows us to connect to a free AI language model (LLaMA) and generate chatbot responses.
from scrape import scrape_website
#*This line imports the scrape_website function from the scrape.py file, which is responsible for scraping text content from a specified website.
from process_data import process_text
#*This line imports the process_text function from the process_data.py file, which processes and limits the length of the scraped text for better performance.

client = Groq(api_key="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")
#*This line initializes a Groq client using an API key, enabling access to the LLaMA language model for generating chatbot responses.

print("✅ Groq client created")
#*This line prints a confirmation message indicating that the Groq client has been successfully created.

website_text = scrape_website("https://botpenguin.com/")
#*This line calls the scrape_website function with the URL "https://botpenguin.com/" to scrape the text content from that website.
context = process_text(website_text)
#*This line processes the scraped text using the process_text function to limit its length for optimal performance in the chatbot.
print("✅ Website data loaded")

def chatbot_response(user_input):
    prompt = f"""
Answer ONLY using the following website content:
#*This prompt instructs the AI to respond solely based on the provided website content.

{context}

User question: {user_input}
#*This section includes the user's question, which the AI will answer using the context from the website.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    #*This block sends the constructed prompt to the LLaMA model via the Groq client and retrieves the AI-generated response.

    return response.choices[0].message.content
#*This line extracts and returns the content of the AI's response.


print("🤖 Free Chatbot Ready! Type 'exit' to quit.\n")
#*This line prints a message indicating that the chatbot is ready for interaction and provides instructions to exit.

while True:
    user_input = input("You: ")
    #*This line prompts the user for input in an infinite loop to facilitate continuous interaction with the chatbot.

    if user_input.lower() == "exit":
        print("Chatbot: Bye 👋")
        break
    #*This block checks if the user wants to exit the chatbot. If the user types "exit", it prints a goodbye message and breaks the loop.

    print("Chatbot:", chatbot_response(user_input))
    #*This line calls the chatbot_response function with the user's input and prints the AI-generated response from the chatbot.
