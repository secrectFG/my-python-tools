
import pyperclip

replaceDicList = [
    {
        "stringNeedToPeplace": "加载",
        "replaceString": """<phoneme alphabet="sapi" ph="jia 1 zai 3">加载</phoneme>"""
    },
    {
        "stringNeedToPeplace": "C#",
        "replaceString": """<sub alias="C Sharp">C#</sub>"""
    },
]

clipstr = pyperclip.paste()

for replaceDic in replaceDicList:
    stringNeedToPeplace = replaceDic["stringNeedToPeplace"]
    replaceString = replaceDic["replaceString"]
    
    clipstr = clipstr.replace(stringNeedToPeplace, replaceString)
    
pyperclip.copy(clipstr)
print(clipstr)

# stringNeedToPeplace = "加载"
# replaceString = """<phoneme alphabet="sapi" ph="jia 1 zai 3">加载</phoneme>"""

# result = pyperclip.paste().replace(stringNeedToPeplace, replaceString)

# stringNeedToPeplace = "C#"
# replaceString = """<sub alias="C Sharp">C#</sub>"""
# result = result.replace(stringNeedToPeplace, replaceString)


# pyperclip.copy(result)
# print(result)