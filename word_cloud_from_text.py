import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud_from_url(url):
    # Fetching text data from URL
    response = requests.get(url)
    text = response.text


    # Generating word cloud
    wordcloud = WordCloud(width = 800, height = 800,
                          background_color ='white',
                          min_font_size = 10).generate(text)

    # Displaying the WordCloud
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def main():
    # Prompting user for URL
    url = input("Please enter the URL of the text file: ")
    generate_wordcloud_from_url(url)

if __name__ == "__main__":
    main()
