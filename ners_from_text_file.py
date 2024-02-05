import requests
import spacy

def fetch_text_from_url(url):
    """Fetch text from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response is not 2xx
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the document: {e}")
        return None

def extract_named_entities(text):
    """Extract named entities from text using spaCy."""
    # Load the pre-trained spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract and return named entities
    return [(ent.text, ent.label_) for ent in doc.ents]

def main():
    # Prompt the user for a URL
    url = input("Please enter the URL to a text document: ")

    # Fetch text from the URL
    text = fetch_text_from_url(url)

    if text:
        # Extract named entities
        named_entities = extract_named_entities(text)

        # Print the named entities
        print("\nNamed Entities Found:")
        for entity, label in named_entities:
            print(f"{entity} ({label})")

if __name__ == "__main__":
    main()
