import uuid
import base64

def generate_unique_id():
    # 生成 UUID
    u = uuid.uuid4()
    # 将 UUID 转换为字节
    u_bytes = u.bytes
    # 使用 Base64 编码并替换字符
    base62_id = base64.urlsafe_b64encode(u_bytes).decode('utf-8').rstrip('=')
    return base62_id

print(generate_unique_id())
