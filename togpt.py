import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
msg=[]

def chat(): 
    # 更多参数参见 https://platform.openai.com/docs/guides/chat/introduction   https://platform.openai.com/docs/api-reference/chat
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # 默认模型，性价比较高
        messages=msg,  
    )
    return completion.choices[0].message.content

print('请确保已执行 pip install openai')
print('请确保本终端可以访问api.openai.com，如export https_proxy="xxx"')
print('请确保OPENAI_API_KEY已在环境变量中，如export OPENAI_API_KEY="sk-xxxx"')
print('输入"-1"结束本轮聊天并开始新聊天，输入Ctrl+C结束本程序')
print("注，默认保留一轮内所有历史，一轮聊天越长，耗费token越多")

while True:
    s=input("\nI: ")
    # a new chat
    if s=='-1':
        msg=[] # 清空历史记录
        print("\n新聊天\n")
        continue
    if s=='' or s=='\n': continue
    # current chat
    msg.append({"role": "user", "content": s}) # 添加用户历史记录
    res=chat() # 访问ChatGPT
    msg.append({"role": "assistant", "content": s}) # 添加GPT历史记录
    print('\nGPT:',res)
