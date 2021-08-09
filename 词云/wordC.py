# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import codecs
import jieba
from imageio import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageFont





def draw_wordcloud(wordCount):
    comment_text = open(r'C:\Users\hp\Desktop\python\kuangren.txt','r',encoding='utf-8').read()
    cut_text = "".join(jieba.cut(comment_text))
    #print(cut_text)
    d = path.dirname()
    color_mask = imread("circle.jpg")
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path= r"C:\Users\hp\Desktop\python\font1.ttf",
        # font_path=path.join(d,'simsun.ttc'),
        # 设置背景色
        background_color='white',
        # 词云形状
        mask=color_mask,
        # 允许最大词汇
        max_words=2000,
        # 最大号字体
        max_font_size=4
    )

    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file("cloud.jpg")
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_wordcloud()