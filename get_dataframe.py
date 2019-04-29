# -*- coding: utf-8 -*-
"""
    File Name:      get_dataframe.py
    Description:    将分类好的词条输出到excel
    Author:         Rabbear Su
    creation date:  2019/4/29
"""
import pandas as pd
from tqdm import tqdm


def get_df(alpha):
    df = pd.DataFrame(columns=['假名', '日文', '意思', '类型'])
    print('\n---start generating dataframe---')
    for i, j in tqdm(vars(alpha).items()):
        name = list(j)[0]
        entry_list = list(j.values())[0]
        # 添加标识字段
        df = df.append({'假名': name, '日文': '', '意思': '', '类型': ''}, ignore_index=True)
        for entry in entry_list:
            jp_words = entry['日文']
            kana = entry['假名']
            meaning = entry['意思']
            word_type = entry['类型']

            # 判断是否有类型
            if isinstance(word_type, str):
                df = df.append({'假名': kana, '日文': jp_words, '意思': meaning, '类型': word_type}, ignore_index=True)
            else:
                df = df.append({'假名': kana, '日文': jp_words, '意思': meaning, '类型': ''}, ignore_index=True)

        df = df.append({'假名': '', '日文': '', '意思': '', '类型': ''}, ignore_index=True)
    print('\n---finish generating dataframe---')
    return df
