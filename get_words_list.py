# -*- coding: utf-8 -*-
"""
    File Name:      get_words_list.py
    Description:    获取词条字典
    Author:         Rabbear Su
    creation date:  2019/4/28
"""
import pandas as pd
from tqdm import tqdm

# 获取所有词条并添加入列表
def get_all_words(path):
    """
    读取excel文件并获取所有word的词条，添加进list
    :param path:
    :return:
    """
    # 读取excel
    pd_frame = pd.read_excel(path)
    # 建立词条列表
    word_list = []
    print('\n---start generating word_list---')
    for i in tqdm(range(len(pd_frame))):
        # 建立该词条字典
        word_dict = {}

        jp_words = pd_frame.iloc[i]['日文']
        kana = pd_frame.iloc[i]['假名']
        meaning = pd_frame.iloc[i]['中文']
        word_type = pd_frame.iloc[i]['类型']

        # 筛选有效行
        if isinstance(kana, float) == False:
            word_dict['日文'] = jp_words
            word_dict['假名'] = kana
            word_dict['意思'] = meaning
            word_dict['类型'] = word_type
            word_list.append(word_dict)
    print('\n---finish generating word_list---')
    return word_list


if __name__ == '__main__':
    excel_path = 'jp_zhongji.xlsx'
    word_list = get_all_words(excel_path)



