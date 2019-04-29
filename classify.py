# -*- coding: utf-8 -*-
"""
    File Name:      classify.py
    Description:    按照字段进行分类
    Author:         RabbearSu
    creation date:  2019/4/28
"""
from get_excel import get_all_words
from alphabet import Alpha
import pandas as pd
from tqdm import tqdm

excel_path = 'jp_zhongji.xlsx'

# 获取所有词条
word_list = get_all_words(excel_path)

# 遍历词条，进行分类
for entry in word_list:
    jp_words = entry['日文']
    kana = entry['假名']
    meaning = entry['意思']
    word_type = entry['类型']

alpha = Alpha()

alpha.classify(word_list)


df = pd.DataFrame(columns=['日文', '假名', '意思', '类型'])

for i, j in tqdm(vars(alpha).items()):
    name = list(j)[0]
    entry_list = list(j.values())[0]
    # 添加标识字段
    df = df.append([[name, '', '', '']], ignore_index=True)
    for entry in entry_list:
        jp_words = entry['日文']
        kana = entry['假名']
        meaning = entry['意思']
        word_type = entry['类型']

        if isinstance(word_type, str):
            df.append([[jp_words, kana, meaning, word_type]], ignore_index=True)
        else:
            df.append([[jp_words, kana, meaning, '']], ignore_index=True)

    df.append([['', '', '', '']], ignore_index=True)

print(df)





