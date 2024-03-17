# import re

# alphabets = "([A-Za-zÀ-Ỹà-ỹĂăÂâĐđÊêÔôƠơƯưƵƶ])"
# prefixes = "(Ông|Bà|Anh|Chị|Cô|Thầy|Cô|Tiến Sĩ|Thạc Sĩ|Trung Sĩ|Đại Tá|Thiếu Tá|Trung Tá|Tiểu Tá|Chú|Cậu|Bác|Bà|Ông Bà|Ông Chủ|Bà Chủ|Tiến Sĩ|Giáo Sư|Cô Giáo|Thầy Giáo|Cô Gái|Bé|Anh Chàng|Chị Gái|Thím|Bác Gái|Chú Gái|Ông Bụt|Bà Bụt|Thằng|Con|Người|Cái|Kia|Chỗ|Nơi|Khi Nào|Vào Khi Nào|Ngày|Tháng|Năm)[.]"
# suffixes = "(Công Ty|Cty|Tập Đoàn|Tđ|Tổ Chức|TC|Tập Đoàn|Tđ|Tổ Chức|TC|Tổ Chức|TC|Công Ty TNHH|CTy|Công Ty Cổ Phần|CTCP|Công Ty Trách Nhiệm Hữu Hạn|CTTNHH|Công Ty Hữu Hạn|CTHH|Công Ty TNHH MTV|CTy TNHH MTV|Công Ty TNHH Thương Mại|CTy TNHH TM|Công Ty TNHH Dịch Vụ|CTy TNHH DV|Công Ty TNHH DV|CTy TNHH ĐT|Công Ty TNHH XNK|CTy TNHH XNK|Công Ty TNHH SX|CTy TNHH SX|Công Ty TNHH TM|CTy TNHH TM|Công Ty TNHH PT|CTy TNHH PT|Công Ty TNHH GTVT|CTy TNHH GTVT|Công Ty TNHH DV GTVT|CTy TNHH DV GTVT|Công Ty TNHH Một Thành Viên|CTy TNHH MTV|Công Ty TNHH DV Một Thành Viên|CTy TNHH DV MTV|Công Ty TNHH XNK Một Thành Viên|CTy TNHH XNK MTV|Công Ty TNHH SX Một Thành Viên|CTy TNHH SX MTV|Công Ty TNHH TM Một Thành Viên|CTy TNHH TM MTV|Công Ty TNHH PT Một Thành Viên|CTy TNHH PT MTV|Công Ty TNHH GTVT Một Thành Viên|CTy TNHH GTVT MTV|Công Ty TNHH DV GTVT Một Thành Viên|CTy TNHH DV GTVT MTV|Công Ty TNHH Một Thành Viên|CTy TNHH MTV|Công Ty TNHH DV Một Thành Viên|CTy TNHH DV MTV|Công Ty TNHH XNK Một Thành Viên|CTy TNHH XNK MTV|Công Ty TNHH SX Một Thành Viên|CTy TNHH SX MTV|Công Ty TNHH TM Một Thành Viên|CTy TNHH TM MTV|Công Ty TNHH PT Một Thành Viên|CTy TNHH PT MTV|Công Ty TNHH GTVT Một Thành Viên|CTy TNHH GTVT MTV|Công Ty TNHH DV GTVT Một Thành Viên|CTy TNHH DV GTVT MTV)[.]"
# starters = "(Ông|Bà|Anh|Chị|Cô|Thầy|Cô|Tiến Sĩ|Thạc Sĩ|Trung Sĩ|Đại Tá|Thiếu Tá|Trung Tá|Tiểu Tá|Chú|Cậu|Bác|Bà|Ông Bà|Ông Chủ|Bà Chủ|Tiến Sĩ|Giáo Sư|Cô Giáo|Thầy Giáo|Cô Gái|Bé|Anh Chàng|Chị Gái|Thím|Bác Gái|Chú Gái|Ông Bụt|Bà Bụt|Thằng|Con|Người|Cái|Kia|Chỗ|Nơi|Khi Nào|Vào Khi Nào|Ngày|Tháng|Năm)"
# acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
# websites = "[.](com|net|org|io|gov|edu|me)"
# digits = "([0-9])"
# multiple_dots = r'\.{2,}'

# def split_into_sentences(text: str) -> list[str]:
#     """
#     Split the text into sentences.

#     If the text contains substrings "<prd>" or "<stop>", they would lead 
#     to incorrect splitting because they are used as markers for splitting.

#     :param text: text to be split into sentences
#     :type text: str

#     :return: list of sentences
#     :rtype: list[str]
#     """
#     text = " " + text + "  "
#     text = text.replace("\n", " ")

#     # Combine multiple patterns into a single call
#     patterns = [
#         (prefixes, "\\1<prd>"),
#         (websites, "<prd>\\1"),
#         (digits + "[.]" + digits, "\\1<prd>\\2"),
#         (multiple_dots, lambda match: "<prd>" * len(match.group(0)) + "<stop>"),
#         ("Thạc Sĩ", "Thạc_Sĩ"),
#         ("\s" + alphabets + "[.] ", " \\1<prd> "),
#         (acronyms + " " + starters, "\\1<stop> \\2"),
#         (alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>"),
#         (alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>"),
#         (" " + suffixes + "[.] " + starters, " \\1<stop> \\2"),
#         (" " + suffixes + "[.]", " \\1<prd>"),
#         (" " + alphabets + "[.]", " \\1<prd>")
#     ]

#     for pattern, replacement in patterns:
#         text = re.sub(pattern, replacement, text)

#     if "”" in text:
#         text = text.replace(".”", "”.")
#     if "\"" in text:
#         text = text.replace(".\"", "\".")
#     if "!" in text:
#         text = text.replace("!\"", "\"!")
#     if "?" in text:
#         text = text.replace("?\"", "\"?")
    
#     text = text.replace(".", ".<stop>")
#     text = text.replace("?", "?<stop>")
#     text = text.replace("!", "!<stop>")
#     text = text.replace("<prd>", ".")

#     sentences = text.split("<stop>")
#     sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty sentences
#     return sentences


# file_paths = ["data/input/Raw_Data_Tom_Sawyer.txt",
#               "data/input/Huckleberry_finn_vn.txt"
#              ]
# output_file_path = 'data/output/VN-Data.txt'

# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for file_path in file_paths:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()

#         sentences = split_into_sentences(text)

#         #output_file.write(f"=== Sentences from {file_path} ===\n")
#         for idx, sentence in enumerate(sentences, start=1):
#             output_file.write(sentence +"\n")
#         output_file.write("\n")


# import re
# def clean_text(text):
    
#     cleaned_text = re.sub(r'\s+', ' ', text)
#     cleaned_text = re.sub(r'[+++{}\[\]\-$%@*()@/=]', '', cleaned_text)
#     cleaned_sentence = re.sub(r'\.{2,}', '.', cleaned_text)
#     return cleaned_sentence.strip()

# def split_sentences(text):
#     sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
#     return sentences

# input_path = 'data/input/Raw_Data_Tom_Sawyer.txt'
# output_path = 'data/output/Cleaned_Data_Tom_Sawyer.txt'

# with open(input_path, 'r', encoding='utf-8') as file:
#     text = file.read()

# cleaned_text = clean_text(text)
# sentences = split_sentences(cleaned_text)
# pattern = re.compile(r'Chương\s+\d+(\s+\d+)*(?=\s*\.?$)')
# with open(output_path, 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         sentence = re.sub(pattern, '.', sentence)
#         sentence = sentence.strip()
#         file.write(sentence + '\n')

# print("Data processing successful!")

import re

def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s\.]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\.{2,}', '.', cleaned_text)
    return cleaned_text.strip()

def split_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

def process_data(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clean_text(text)
    sentences = split_sentences(cleaned_text)

    pattern = re.compile(r'Chương\s+\d+(\s+\d+)*(?=\s*\.?$)')
    with open(output_path, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            sentence = re.sub(pattern, '.', sentence.strip())
            file.write(sentence + '\n')

    print("Data processing successful!")

if __name__ == "__main__":
    input_path = 'data/input/Raw_Data_Tom_Sawyer_VN.txt'
    output_path = 'data/output/Cleaned_Data_Tom_Sawyer_VN.txt'
    process_data(input_path, output_path)
