# -*- coding: utf-8 -*-
"""
    File Name:      classify.py
    Description:    按照字段进行分类
    Author:         Yange Cao
    creation date:  2019/4/28
"""
import os
from get_excel import get_all_words
from alphabet import Alpha

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

alpha.get_length()

