import json


def convert_to_unicode_escape(json_str):
    try:
        # 解析 JSON 字符串为 Python 对象
        data = json.loads(json_str)
        # 将 Python 对象转换回 JSON 字符串，确保非 ASCII 字符被转义为 \u 格式
        escaped_json_str = json.dumps(data, ensure_ascii=True, separators=(',', ':'))
        return escaped_json_str
    except json.JSONDecodeError:
        print("输入的不是有效的 JSON 字符串。")
        return None


# 示例用法
if __name__ == "__main__":
    # 普通的 JSON 字符串
    normal_json_str = '{"message": "你好，世界！"}'
    # 转换为 \u 格式
    escaped_json_str = convert_to_unicode_escape(normal_json_str)
    if escaped_json_str:
        print(escaped_json_str)
    