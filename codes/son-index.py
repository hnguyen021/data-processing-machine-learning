from googletrans import Translator
import spacy
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

#Đọc các câu từ tệp văn bản và trích xuất nhãn POS (phân loại từ loại) cho mỗi từ trong mỗi câu.
def load_sentences_with_pos(filename, start_line=0):
    nlp = spacy.load("en_core_web_sm")  # SpaCy model for English
    with open(filename, 'r', encoding='utf-8') as file:
        sentences_with_pos = []
        lines = file.readlines()[start_line:]
        for line in lines:
            doc = nlp(line.strip())
            pos_tags = [(token.text, token.pos_) for token in doc]
            sentences_with_pos.append((line.strip(), pos_tags))
        return sentences_with_pos

#Đọc các câu tiếng Anh từ một tệp văn bản và trả về một danh sách các câu.
def load_english_sentences(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        english_sentences = [line.strip() for line in file.readlines()]
    return english_sentences

#Dịch một câu từ tiếng Việt sang tiếng Anh bằng thư viện Googletrans.
def translate_sentence(sentence, target_lang='en'):
    translator = Translator()
    translation = translator.translate(sentence, dest=target_lang)
    return translation.text

#Tính toán độ tương đồng giữa hai câu bằng cách sử dụng ma trận TF-IDF và độ tương đồng cosine.
# def calculate_similarity(sentence1, sentence2):
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])
#     similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
#     return similarity
def calculate_similarity(sentence1, sentence2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([sentence1, sentence2])
    cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:2]).flatten()
    print(cosine_similarities)
    return cosine_similarities[0]
#Tìm câu tiếng Anh tương ứng với một câu tiếng Việt dựa trên độ tương đồng cosine, và trả về câu tiếng Anh nếu độ tương đồng vượt qua ngưỡng cho trước.
def find_corresponding_english_sentence(vietnamese_sentence, english_sentences, threshold=0.3):
    translated_vietnamese_sentence = translate_sentence(vietnamese_sentence, target_lang='en')

    max_similarity = 0
    corresponding_english_sentence = None

    for english_sentence in english_sentences:
        similarity = calculate_similarity(translated_vietnamese_sentence, english_sentence)

        if similarity > max_similarity:
            max_similarity = similarity
            corresponding_english_sentence = english_sentence

    if max_similarity > 0:
        return corresponding_english_sentence, translated_vietnamese_sentence
    else:
        return None, translated_vietnamese_sentence


def main():
    english_sentences = load_english_sentences('data/output/DLT.txt')

    while True:
        vietnamese_sentence = input("Nhập một câu tiếng Việt (hoặc nhập 'q' để thoát): ")
        
        if vietnamese_sentence.lower() == 'q':
            break

        corresponding_english_sentence, translated_vietnamese_sentence = find_corresponding_english_sentence(
            vietnamese_sentence, english_sentences
        )

        if corresponding_english_sentence:
            print("Câu tiếng Anh gần nhất với câu tiếng Việt:", corresponding_english_sentence)
            print("Câu tiếng Anh được dịch từ câu tiếng Việt:", translated_vietnamese_sentence)
        else:
            print("Câu tiếng Anh được dịch từ câu tiếng Việt:", translated_vietnamese_sentence)
            print("Không tìm thấy câu tiếng Anh tương ứng.")


if __name__ == "__main__":
    main()