import base64
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# 限制请求路径
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/TTSRPC',)

# 创建服务器
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # 注册一个简单的函数
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y
    
    def get_mp3():
        encoded_string = None
        with open(r'E:\Downloads\一颗狼星+-+星月原野.mp3', 'rb') as audio_file:
            encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
        return encoded_string

    server.register_function(add, 'add')
    server.register_function(subtract, 'subtract')
    server.register_function(get_mp3, 'get_mp3')

    print("服务器已启动，等待请求...")
    server.serve_forever()
