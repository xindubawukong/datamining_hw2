#!/usr/bin/env python
# coding: utf-8

# # 一、数据预处理和可视化(8分)

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('matplotlib', 'inline')


# 1) 新闻数据读入与建立数据框对象(data.frame)。每篇新闻都有多个属性，不必全部保留，但是要求数据框对象中的属性至少包括全文、类别、时间，缺失的用 NA 填充。(hint: library(xml))

# In[ ]:





# 2) 对新闻全文进行预处理，包括去除标点符号、停用词、数字、空白字符，将大写字母都转化为小写，以及词干化处理。(hint: library(tm))

# 3) 将每一篇新闻的全文表示成 BagOfWords 向量。

# 4) 考虑单词在所有新闻中的出现次数。给出出现次数最多的 100 个词并对这些词画出“云图”。(hint: library(wordcloud))

# 5) 给出单词长度的分布情况并画出直方图。(hint: library(ggplot2))

# 6) 考虑新闻全文的单词数，分别使用等深分箱和等宽分箱将所有新闻分成 10  个箱，并画出每个箱包含的新闻数量的直方图。

# 7) 给出每一个类别下的新闻数量的分布情况并画出直方图。

# 8) 给出每个月的新闻数量的分布情况并画出直方图。
