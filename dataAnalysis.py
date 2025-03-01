import os
import re
import pandas as pd

text_files_folder = r"C:\Users\Prakhar\Desktop\InternShip_webScraping"

# Loading positive and negative words from text files
def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip().lower() for word in file.readlines())

positive_words_file = r"C:\Users\Prakhar\Desktop\InternShip_webScraping\Dictionary\positive-words.txt"  
negative_words_file = r"C:\Users\Prakhar\Desktop\InternShip_webScraping\Dictionary\negative-words.txt" 

positive_words = load_words(positive_words_file)
negative_words = load_words(negative_words_file)

def count_syllables(word):
    return len(re.findall(r'[aeiouyAEIOUY]+', word))

def is_complex(word):
    return count_syllables(word) > 2

def calculate_polarity(positive_score, negative_score):
    return (positive_score - negative_score) / ((positive_score + negative_score) + 1e-6)  

def calculate_subjectivity(positive_score, negative_score, word_count):
    return (positive_score + negative_score) / (word_count + 1e-6)  

output_data = []

for file_name in os.listdir(text_files_folder):
    if file_name.endswith(".txt"):
        url_id = file_name.replace(".txt", "")
        url = f"https://example.com/{url_id}" 
        file_path = os.path.join(text_files_folder, file_name)

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        sentences = re.split(r'[.!?]', text)  
        word_list = re.findall(r'\b\w+\b', text)  
        word_count = len(word_list)
        sentence_count = len(sentences)
        avg_sentence_length = word_count / sentence_count if sentence_count else 0
        avg_number_of_words_per_sentence = avg_sentence_length 
        avg_word_length = sum(len(word) for word in word_list) / word_count if word_count else 0

        positive_score = sum(1 for word in word_list if word.lower() in positive_words)
        negative_score = sum(1 for word in word_list if word.lower() in negative_words)

        complex_word_count = sum(1 for word in word_list if is_complex(word))
        syllable_count = sum(count_syllables(word) for word in word_list)
        percentage_complex_words = (complex_word_count / word_count) * 100 if word_count else 0
        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

        personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us|me|mine|ourselves|yours|yourself)\b', text, re.IGNORECASE))

        polarity_score = calculate_polarity(positive_score, negative_score)
        subjectivity_score = calculate_subjectivity(positive_score, negative_score, word_count)

        output_data.append({
            "URL_ID": url_id,
            "URL": url,
            "POSITIVE SCORE": positive_score,
            "NEGATIVE SCORE": negative_score,
            "POLARITY SCORE": polarity_score,
            "SUBJECTIVITY SCORE": subjectivity_score,
            "AVG SENTENCE LENGTH": avg_sentence_length,
            "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
            "FOG INDEX": fog_index,
            "AVG NUMBER OF WORDS PER SENTENCE": avg_number_of_words_per_sentence,
            "COMPLEX WORD COUNT": complex_word_count,
            "WORD COUNT": word_count,
            "SYLLABLE PER WORD": syllable_count / word_count if word_count else 0,
            "PERSONAL PRONOUNS": personal_pronouns,
            "AVG WORD LENGTH": avg_word_length
        })

# Saving results
output_df = pd.DataFrame(output_data)
output_df.to_excel("Output.xlsx", index=False)

print("Analysis complete! Results saved to 'Output.xlsx'.")

