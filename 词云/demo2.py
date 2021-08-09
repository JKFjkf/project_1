# -*- coding: utf-8 -*-
__author__ = 'leilu'
#wordcloud生成中文词云

import codecs
import os
from os import path

import jieba
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
# import jieba.analyse as analyse
from imageio import imread
from wordcloud import WordCloud


# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    comment_text = open(r'C:\Users\hp\Desktop\python\kuangren.txt','r',encoding='utf-8').read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(comment_text,cut_all=True))
    d = path.dirname(__file__) # 当前文件文件夹所在目录
    color_mask = imread("lu.png") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="font1.TTF",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=20000,
        #最大号字体
        max_font_size=100
    )
    word_cloud = cloud.generate(cut_text) # 产生词云
    word_cloud.to_file("pjl_cloud4.jpg") #保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()



if __name__ == '__main__':

    draw_wordcloud()