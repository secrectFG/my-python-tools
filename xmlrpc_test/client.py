import xmlrpc.client
import base64

def decode_audio(encoded_string, output_file):
    """
    解码Base64编码的音频字符串，并将其保存为文件。

    :param encoded_string: Base64编码的音频字符串
    :param output_file: 输出文件的路径（带扩展名的完整路径）
    """
    # 将Base64字符串解码为二进制数据
    audio_data = base64.b64decode(encoded_string)
    
    # 将二进制数据写入文件
    with open(output_file, 'wb') as audio_file:
        audio_file.write(audio_data)

    print(f"音频文件已保存到 {output_file}")


# 连接到服务器
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    # 调用服务器上的方法
    result_add = proxy.add(5, 3)
    result_subtract = proxy.subtract(10, 4)

    print(f"5 + 3 = {result_add}")
    print(f"10 - 4 = {result_subtract}")
    encoded_string = proxy.get_mp3()
    decode_audio(encoded_string, "output.mp3")
    print("音频文件已下载")
    
    
