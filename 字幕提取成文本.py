import re
import pyperclip

def srt_to_text(srt_file_path):
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    # Use regular expressions to find and remove timecodes and sequence numbers
    text = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', srt_content)
    text = re.sub(r'\d+\n', '', text)

    # Remove HTML tags like <font> and </font>
    text = re.sub(r'<.*?>', '', text)

    # Remove any remaining newline sequences that are not part of the actual text
    text = re.sub(r'\n+', '\n', text).strip()
    print(text)

    # 保存到剪贴板
    pyperclip.copy(text)

# Example usage
srt_to_text(r'E:\Downloads\字幕 1.srt')

