View dataAnalysis.py and dataScraping.py for core code.

# Web Scraping and Text Analysis

## Overview
This project performs web scraping and text analysis to extract articles from given URLs, analyze their sentiment, and compute various text-based metrics. The results are saved in an Excel file for further evaluation.

## Features
- **Web Scraping**: Extracts text content from web pages using BeautifulSoup.
- **Text Analysis**: Computes various linguistic and sentiment analysis metrics.
- **Sentiment Scores**: Identifies positive and negative words.
- **Readability Analysis**: Computes Fog Index and complexity metrics.
- **Output in Excel**: Saves the results in an Excel file for further analysis.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install pandas requests beautifulsoup4 openpyxl
```

## Project Structure
```
📂 InternShip_webScraping
│── 📂 Dictionary
│   ├── positive-words.txt
│   ├── negative-words.txt
│── 📂 TextFiles (Contains extracted text files from URLs)
│── web_scraper.py (Extracts text from web pages)
│── text_analysis.py (Performs text analysis and computes metrics)
│── Input.xlsx (Contains URLs to be processed)
│── Output.xlsx (Stores the analysis results)
│── README.md (Project documentation)
```

## How to Use
### 1. **Web Scraping**
Run `web_scraper.py` to extract content from URLs listed in `Input.xlsx`. The extracted text is saved in individual `.txt` files.
```sh
python web_scraper.py
```

### 2. **Text Analysis**
Run `text_analysis.py` to analyze the extracted text files and generate an Excel report.
```sh
python text_analysis.py
```

### 3. **Results**
After execution, `Output.xlsx` will contain the following metrics for each URL:
- Positive & Negative Score
- Polarity & Subjectivity Score
- Average Sentence Length
- Fog Index
- Complex Word Count
- Personal Pronoun Count
- Average Word Length

## Example Output
| URL_ID | POSITIVE SCORE | NEGATIVE SCORE | POLARITY SCORE | SUBJECTIVITY SCORE | AVG SENTENCE LENGTH |
|--------|---------------|---------------|---------------|------------------|------------------|
| 001    | 15            | 5             | 0.5           | 0.25             | 20               |
| 002    | 10            | 8             | 0.11          | 0.18             | 18               |

## Notes
- Ensure `Input.xlsx` contains valid URLs.
- Positive and negative words are stored in `Dictionary/` folder.

## License
This project is open-source and available for use under the MIT License.

