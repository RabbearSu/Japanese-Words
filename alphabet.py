# -*- coding: utf-8 -*-
"""
    File Name:      alphabet.py
    Description:    所有分类字段
    Author:         Yange Cao
    creation date:  2019/4/28
"""


class Alpha(object):
    def __init__(self):
        self.kou = {'こう': []}      # こう
        self.sei = {'せい': []}      # せい
        self.situ = {'しつ': []}     # しつ
        self.sai = {'さい': []}      # さい
        self.katu = {'かつ': []}     # かつ
        self.gyo = {'ぎょ': []}      # ぎょ
        self.kyuu = {'きゅう': []}   # きゅう
        self.jyo = {'じょ': []}      # じょ
        self.bun = {'ぶん': []}      # ぶん
        self.kyou = {'きょう': []}   # きょう
        self.jyu = {'じゅ': []}      # じゅ
        self.jyou = {'じょう': []}   # じょう
        self.sou = {'そう': []}      # そう
        self.tyo = {'ちょ': []}      # ちょ
        self.zou = {'ぞう': []}      # ぞう
        self.ten = {'てん': []}      # てん
        self.toku = {'とく': []}     # とく
        self.dou = {'どう': []}      # どう
        self.ken = {'けん': []}      # けん
        self.tyuu = {'ちゅう': []}   # ちゅう
        self.jun = {'じゅん': []}    # じゅん
        self.kei = {'けい': []}      # けい
        self.haku = {'はく': []}     # はく
        self.kon = {'こん': []}      # こん
        self.ran = {'らん': []}      # らん
        self.dai = {'だい': []}      # だい
        self.tyou = {'ちょう': []}   # ちょう
        self.hai = {'はい': []}      # はい
        self.ryo = {'りょ': []}      # りょ
        self.ryou = {'りょう': []}   # りょう
        self.en = {'えん': []}       # えん
        self.kai = {'かい': []}      # かい
        self.tai = {'たい': []}      # たい
        self.syo = {'しょ': []}      # しょ
        self.syou = {'しょう': []}   # しょう
        self.tou = {'とう': []}      # とう
        self.sui = {'すい': []}      # すい
        self.gaku = {'がく': []}     # がく
        self.ketu = {'けつ': []}     # けつ
        self.hun = {'ふん': []}      # ふん
        self.hei = {'へい': []}      # へい
        self.gen = {'げん': []}      # げん
        self.riku = {'りく': []}     # りく
        self.syun = {'しゅん': []}   # しゅん
        self.jyun = {'じゅん': []}   # じゅん
        self.men = {'めん': []}      # めん
        self.mitu = {'みつ': []}     # みつ
        self.soku = {'そく': []}     # そく
        self.satu = {'さつ': []}     # さつ
        self.han = {'はん': []}      # はん
        self.zai = {'ざい': []}      # ざい
        self.maku = {'まく': []}     # まく
        self.kan = {'かん': []}      # かん
        self.zen = {'ぜん': []}      # ぜん
        self.jin = {'じん': []}      # じん
        self.gan = {'がん': []}      # がん
        self.ban = {'ばん': []}      # ばん
        self.raku = {'らく': []}     # らく
        self.dan = {'だん': []}      # だん
        self.koku = {'こく': []}     # こく
        self.san = {'さん': []}      # さん
        self.sin = {'しん': []}      # しん
        self.setu = {'せつ': []}     # せつ
        self.gou = {'ごう': []}      # ごう
        self.byou = {'びょう': []}   # びょう
        self.sen = {'せん': []}      # せん
        self.goku = {'ごく': []}     # ごく
        self.gyoku = {'ぎょく': []}  # ぎょく
        self.gyaku = {'ぎゃく': []}  # ぎゃく
        self.ryoku = {'りょく': []}  # りょく
        self.ryaku = {'りゃく': []}  # りゃく
        self.suu = {'すう': []}      # すう
        self.nou = {'のう': []}      # のう
        self.hin = {'ひん': []}      # ひん
        self.jitu = {'じつ': []}     # じつ
        self.syuku = {'しゅく': []}  # しゅく
        self.roku = {'ろく': []}     # ろく
        self.ei = {'えい': []}       # えい
        self.you = {'よう': []}      # よう
        self.zetu = {'ぜつ': []}     # ぜつ
        self.metu = {'めつ': []}     # めつ
        self.kaku = {'かく': []}     # かく
        self.hatu = {'はつ': []}     # はつ
        self.mei = {'めい': []}      # めい
        self.tei = {'てい': []}      # てい
        self.gata = {'がた': []}     # がた
        self.totu = {'とつ': []}     # とつ
        self.kin = {'きん': []}      # きん
        self.inn = {'いん': []}      # いん
        self.hen = {'へん': []}      # へん
        self.bai = {'ばい': []}      # ばい
        self.syutu = {'しゅつ': []}  # しゅつ
        self.gei = {'げい': []}      # げい
        self.yuu = {'ゆう': []}      # ゆう
        self.nen = {'ねん': []}      # ねん
        self.sya = {'しゃ': []}      # しゃ
        self.tatu = {'たつ': []}     # たつ
        self.ben = {'べん': []}      # べん
        self.betu = {'べつ': []}     # べつ
        self.tya = {'ちゃ': []}      # ちゃ
        self.ou = {'おう': []}       # おう
        self.kyoku = {'きょく': []}  # きょく
        self.kyaku = {'きゃく': []}  # きゃく
        self.minn = {'みん': []}     # みん
        self.yaku = {'やく': []}     # やく
        self.den = {'でん': []}      # でん
        self.ren = {'れん': []}      # れん
        self.ritu = {'りつ': []}     # りつ
        self.gai = {'がい': []}      # がい
        self.geki = {'げき': []}     # げき
        self.hou = {'ほう': []}      # ほう
        self.bou = {'ぼう': []}      # ぼう
        self.kuu = {'くう': []}      # くう
        self.iki = {'いき': []}      # いき
        self.kyo = {'きょ': []}      # きょ
        self.sara = {'さら': []}     # さら
        self.zara = {'ざら': []}     # ざら
        self.rou = {'ろう': []}      # ろう
        self.syoku = {'しょく': []}  # しょく
        self.gatu = {'がつ': []}     # がつ
        self.syu = {'しゅ': []}      # しゅ
        self.syuu = {'しゅう': []}   # しゅう
        self.ryu = {'りゅ': []}      # りゅ
        self.ryuu = {'りゅう': []}   # りゅう
        self.mon = {'もん': []}      # もん
        self.doku = {'どく': []}     # どく
        self.tan = {'たん': []}      # たん
        self.zei = {'ぜい': []}      # ぜい
        self.taku = {'たく': []}     # たく
        self.tetu = {'てつ': []}     # てつ
        self.seki = {'せき': []}     # せき
        self.tiku = {'ちく': []}     # ちく
        self.paku = {'ぱく': []}     # ぱく
        self.tuu = {'つう': []}      # つう
        self.zuu = {'ずう': []}      # ずう
        self.hutu = {'ふつ': []}     # ふつ
        self.butu = {'ぶつ': []}     # ぶつ
        self.nin = {'にん': []}      # にん

    def classify(self, word_list):
        """
        对word_list的词条进行分类
        :param word_list:
        :return:
        """
        for entry in word_list:
            kana = entry['假名']
            # 判断字段是否在假名中
            for i, j in vars(self).items():
                name = list(j)[0]
                if name in kana:
                    getattr(self, i)[name].append(entry)

    def list_all(self):
        for i, j in vars(self).items():
            print('字段:{}, 列表:{}'.format(i, j))

    def get_length(self):
        for i, j in vars(self).items():
            name = list(j)[0]
            entry_list = list(j.values())[0]
            print('字段:{} 包含{}个词条'.format(name, len(entry_list)))








