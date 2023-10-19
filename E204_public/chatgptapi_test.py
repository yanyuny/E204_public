# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 10:30:10 2023

@author: 2021
"""




# %% [1]
pip openai
import os
import openai 


openai.api_key = "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" 

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "什么是飞机"}]
)
text = completion.choices[0].message.get("content",'')
print(text)

# %% [2]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "您是一个助手，可以提供帮助。"},
        {"role": "user", "content": "请判断以下两个商品的优劣："},
        {"role": "user", "content": "商品A：价格低廉，但质量较差。"},
        {"role": "user", "content": "商品B：价格高昂，但质量非常好。您认为哪个更值得购买？"}
    ]
)

assistant_reply = response['choices'][0]['message']['content']
print(assistant_reply)

# %% [3]


import pandas as pd

# 创建一个示例DataFrame
data = {'产品名称': ['商品A', '商品B', '商品C'],
        '价格': [25, 30, 22],
        '库存': ['50', '30', '60']}

df = pd.DataFrame(data)

# 使用to_string()方法将DataFrame转换为文本
table_data = df.to_string(index=False)

# 打印文本
# print(text)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "您是一个助手，可以提供帮助。"},
        {"role": "user", "content": "请分析以下产品表格，给出每种商品的优势和不足。"},
        {"role": "user", "content": table_data}
    ]
)

assistant_reply = response['choices'][0]['message']['content']
print(assistant_reply)

# %%[4]









