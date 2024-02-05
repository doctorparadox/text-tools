import requests
from collections import Counter
import matplotlib.pyplot as plt
import nltk

# Download punkt
nltk.download('punkt')

# Download and cache the stop words from NLTK
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Set of English stop words
stop_words = set(stopwords.words('english'))

def download_text(url):
    """Download text content from a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Will raise an error for bad responses
    return response.text

def clean_and_tokenize(text):
    """Tokenize text and remove stop words and punctuation."""
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    return words

def count_word_frequencies(words):
    """Count word frequencies in a list of words."""
    return Counter(words)

def plot_histogram(word_counts):
    """Plot a histogram of word frequencies."""
    words, counts = zip(*word_counts.most_common(25))
    plt.figure(figsize=(10, 8))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 25 Word Frequencies')
    plt.show()

def main():
    url = input("Please enter the URL to a .txt file: ")
    text = download_text(url)
    words = clean_and_tokenize(text)
    word_counts = count_word_frequencies(words)
    plot_histogram(word_counts)

if __name__ == "__main__":
    main()
