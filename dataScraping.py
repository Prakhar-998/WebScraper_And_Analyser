import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read input file
input_df = pd.read_excel('Input.xlsx')

for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title and article text
        title = soup.find('h1').get_text()
        paragraphs = soup.find_all('p')
        article_text = '\n'.join([p.get_text() for p in paragraphs])
        
        # Save to a text file
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(title + '\n\n' + article_text)
    except Exception as e:
        print(f"Error processing URL_ID {url_id}: {e}")



