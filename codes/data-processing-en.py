# import re

# alphabets = "([A-Za-z])"
# prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
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
#         ("Ph.D", "Ph<prd>D<prd>"),
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


# #file_paths = ["data\Raw-Data-Huckleberry-Finn.txt",
# file_paths = [ "data/input/Raw-Data-Tom-Sawyer.txt",
#               "data/input/Raw-Data-Huckleberry-Finn.txt",
#              ]

# output_file_path = 'data/output/Craw_data_eng.txt'

# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for file_path in file_paths:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()

#         sentences = split_into_sentences(text)

#         for idx, sentence in enumerate(sentences, start=1):
#             output_file.write(sentence + "\n")
#         output_file.write("\n")


# import re

# alphabets = "([A-Za-z])"
# prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
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
#         ("Ph.D", "Ph<prd>D<prd>"),
#         ("\s" + alphabets + "[.] ", " \\1<prd> "),
#         (acronyms + " " + starters, "\\1<stop> \\2"),
#         (alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>"),
#         (alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>"),
#         (" " + suffixes + "[.] " + starters, " \\1<stop> \\2"),
#         (" " + suffixes + "[.]", " \\1<prd>"),
#         (" " + alphabets + "[.]", " \\1<prd>"),
#         # Adding rule to remove hyphens and quotes
#         ('-', ''),
#         ('"', ''),
#         ('—', '')
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


# file_paths = [
#     "data/input/Raw_Data_Tom_Sawyer_EN.txt",
#     "data/input/Raw_Data_Huckleberry_Finn_EN.txt",
# ]

# output_file_path = 'data/output/cleaned_data_eng.txt'

# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for file_path in file_paths:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()

#         sentences = split_into_sentences(text)

#         for idx, sentence in enumerate(sentences, start=1):
#             output_file.write(sentence + "\n")
#         output_file.write("\n")


import re

alphabets = "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"
multiple_dots = r'\.{2,}'

def split_into_sentences(text: str) -> list[str]:
    """
    Split the text into sentences.

    If the text contains substrings "<prd>" or "<stop>", they would lead 
    to incorrect splitting because they are used as markers for splitting.

    :param text: text to be split into sentences
    :type text: str

    :return: list of sentences
    :rtype: list[str]
    """
    text = " " + text + "  "
    text = text.replace("\n", " ")

    # Combine multiple patterns into a single call
    patterns = [
        (prefixes, "\\1<prd>"),
        (websites, "<prd>\\1"),
        (digits + "[.]" + digits, "\\1<prd>\\2"),
        (multiple_dots, lambda match: "<prd>" * len(match.group(0)) + "<stop>"),
        ("Ph.D", "Ph<prd>D<prd>"),
        ("\s" + alphabets + "[.] ", " \\1<prd> "),
        (acronyms + " " + starters, "\\1<stop> \\2"),
        (alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>"),
        (alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>"),
        (" " + suffixes + "[.] " + starters, " \\1<stop> \\2"),
        (" " + suffixes + "[.]", " \\1<prd>"),
        (" " + alphabets + "[.]", " \\1<prd>"),
        # Adding rule to remove hyphens and quotes
        ('-', ''),
        ('"', ''),
        ('—', '')
    ]

    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")

    sentences = text.split("<stop>")
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


file_paths = [
    "data/input/Raw_Data_Tom_Sawyer_EN.txt",
    "data/input/Raw_Data_Huckleberry_Finn_EN.txt",
]

output_file_paths = [
    'data/output/cleaned_data_tom_sawyer_eng.txt',
    'data/output/cleaned_data_huckleberry_finn_eng.txt'
]

for input_file, output_file in zip(file_paths, output_file_paths):
    with open(output_file, 'w', encoding='utf-8') as output_file:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        sentences = split_into_sentences(text)

        for idx, sentence in enumerate(sentences, start=1):
            output_file.write(sentence + "\n")
        output_file.write("\n")
