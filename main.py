# -*- coding: utf-8 -*-
"""
    File Name:      main.py
    Description:    按照字段进行分类
    Author:         Rabbear Su
    creation date:  2019/4/28
"""
from get_words_list import get_all_words
from alphabet import Alpha
from get_dataframe import get_df

excel_path = 'jp_zhongji.xlsx'

# 获取所有词条
word_list = get_all_words(excel_path)

# 构建词汇表并分类
alpha = Alpha()
alpha.classify(word_list)

# 获取dataframe
df = get_df(alpha)

# 输出到excel
df.to_excel('output\\word_classified.xlsx')












