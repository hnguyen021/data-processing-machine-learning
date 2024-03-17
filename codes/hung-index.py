from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from googletrans import Translator
def translate_vietnamese_to_english(vietnamese_text):
    translator = Translator()
    english_text = translator.translate(vietnamese_text, src='vi', dest='en').text
    return english_text

# def find_corresponding_sentence(english_text, english_sentences, start_index, end_index):
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform(english_sentences[start_index:end_index])

#     similarities = cosine_similarity(tfidf_matrix, tfidf_vectorizer.transform([english_text]))
#     max_sim_index = np.argmax(similarities)

#     return english_sentences[start_index + max_sim_index]

# def find_corresponding_sentence(english_text, english_sentences):
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform(english_sentences + [english_text])

#     similarities = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])
#     max_sim_index = np.argmax(similarities)

#     return english_sentences[max_sim_index]


# def main(vietnamese_file, english_file, output_file):
#     with open(vietnamese_file, 'r', encoding='utf-8') as vietnamese_file:
#         vietnamese_sentences = vietnamese_file.readlines()

#     with open(english_file, 'r', encoding='utf-8') as english_file:
#         english_sentences = english_file.readlines()

#     result = []
#     for vietnamese_sentence in vietnamese_sentences:
#         english_translation = translate_vietnamese_to_english(vietnamese_sentence.strip())
#         corresponding_sentence = find_corresponding_sentence(english_translation, english_sentences)
#         result.append(f"Vietnamese: {vietnamese_sentence.strip()}\nEnglish: {corresponding_sentence.strip()}\n")

#     with open(output_file, 'w', encoding='utf-8') as output:
#         output.writelines(result)
# def main(vietnamese_file, english_file, output_file):
#     with open(vietnamese_file, 'r', encoding='utf-8') as vietnamese_file:
#         vietnamese_sentences = vietnamese_file.readlines()

#     with open(english_file, 'r', encoding='utf-8') as english_file:
#         english_sentences = english_file.readlines()

#     result = []
#     for index, vietnamese_sentence in enumerate(vietnamese_sentences):
#         print(index)
#         english_translation = translate_vietnamese_to_english(vietnamese_sentence.strip())
#         corresponding_sentence = find_corresponding_sentence(english_translation, english_sentences, index, 30)
#         print(corresponding_sentence)
#         result.append(f"Vietnamese: {vietnamese_sentence.strip()}\nEnglish: {corresponding_sentence.strip()}\n")

#     with open(output_file, 'w', encoding='utf-8') as output:
#         output.writelines(result)

def calculate_similarity(sentence1, sentence2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([sentence1, sentence2])
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2]).flatten()
    print(cosine_similarities)
    return cosine_similarities[0]
def find_corresponding_sentence(english_text, english_sentences, start_index, end_index):
    start_range = start_index
    end_range = end_index + start_index
    if start_range < 20:
        start_range = 0
    elif start_range >= 20:
        start_range = start_index - 20
    
    if end_range > len(english_sentences):
        end_range = end_index
    english_sentences_subset = english_sentences[start_range:end_range]
    if not english_sentences_subset:
        return None

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(english_sentences_subset)
    similarities = cosine_similarity(tfidf_matrix, tfidf_vectorizer.transform([english_text]))
    max_sim_index = np.argmax(similarities)

    return english_sentences[start_index + max_sim_index]


def main(vietnamese_file, english_file, output_file):
    with open(vietnamese_file, 'r', encoding='utf-8') as vietnamese_file:
        vietnamese_sentences = vietnamese_file.readlines()

    with open(english_file, 'r', encoding='utf-8') as english_file:
        english_sentences = english_file.readlines()

    result = []
    for index, vietnamese_sentence in enumerate(vietnamese_sentences):
        print(index)
        english_translation = translate_vietnamese_to_english(vietnamese_sentence)
        corresponding_sentence = find_corresponding_sentence(english_translation, english_sentences, index, 30)
        print(corresponding_sentence)
        result.append(corresponding_sentence)

    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(result)

if __name__ == "__main__":
    vietnamese_file = "data/output/Cleaned_Data_Tom_Sawyer.txt"  
    english_file = "data/output/Craw_data_eng.txt"  
    output_file = "data/output/mapped-dataset-En.txt" 
    main(vietnamese_file, english_file, output_file)
