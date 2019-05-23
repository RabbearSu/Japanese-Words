# -*- coding: utf-8 -*-
"""
    File Name:      ABAB_adv.py
    Description:    整理ABAB型副词
    Author:         Rabbear Su
    creation date:  2019/5/23
"""
import pandas as pd
import os

txt_path = 'data\\ABAB.txt'

with open(txt_path, 'r') as f:
    lines = f.readlines()
    f.close()

df = pd.DataFrame(columns=['副词', '意思', '例句', '例句意思'])


for i, line in enumerate(lines):
    index = int(i / 2)
    line = line.strip('\r\n').replace(u'\u3000', u'')
    if i % 2 == 0:
        try:
            df = df.append({'副词': line.split('?')[0], '意思': line.split('?')[1], '例句': '', '例句意思': ''},
                       ignore_index=True)
        except:
            df = df.append({'副词': line.split(' ')[0], '意思': line.split(' ')[1], '例句': '', '例句意思': ''},
                           ignore_index=True)

    if i % 2 != 0:
        df.iloc[index]['例句'] = line.split('／')[0].split('：')[1]
        df.iloc[index]['例句意思'] = line.split('／')[1]
        print(df)
