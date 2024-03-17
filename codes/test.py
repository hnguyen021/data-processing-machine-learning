# import re

# def clean_text(text):
#     # Loại bỏ các ký tự như {, }, [, ], -, $, %, *, (, ), @, /
#     cleaned_text = re.sub(r'[+++{}\[\]\-$%@*()@/=]', '', text)
#     cleaned_text = re.sub(r'^\s*|\s*$', '', cleaned_text)
#     cleaned_sentence = re.sub(r'\.{2,}', '.', cleaned_text)
#     return cleaned_sentence.strip()

# text = "    [ =Cuộc phiêu lưu đó rất kì thú,tôi ...rất hi vọng +++được tham gia những// hành trình như vậy ..."

# cleaned_text = clean_text(text)
# print(cleaned_text)

# import re

# def loai_bo_chuong_va_so(text):
#     # Biểu thức chính quy để tìm "Chương" và các con số ở cuối câu
#     pattern = re.compile(r'Chương\s+\d+(\s+\d+)*(?=\s*\.?$)')
    
#     # Loại bỏ từ "Chương" và những con số ở cuối câu
#     text_without_chapter = re.sub(pattern, '', text)
    
#     return text_without_chapter.strip()  # Xóa khoảng trắng dư thừa

# # Ví dụ văn bản đầu vào
# van_ban = "Chương 1 Đây là nội dung của Chương 1 2 3."

# # Áp dụng hàm và in kết quả
# ket_qua = loai_bo_chuong_va_so(van_ban)
# print(ket_qua)
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
    input_path = 'data/input/Huckleberry_finn_vn.txt'
    output_path = 'data/output/test.txt'
    process_data(input_path, output_path)
