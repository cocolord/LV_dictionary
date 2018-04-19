import os
import re
import pickle
origin_file = open("Dict_data/eywedu - 副本 (2).txt",'r')
words_file = open("Dict_data/words.txt",'a')
# output2 = open('Dict_data/danci.pkl', 'wb')
output1 = open('Dict_data/cixing.pkl', 'wb')
test1 = '''【一旦】⒈有一天。⒉一时；忽然。⒊形容时间很短。'''
test2 = '''一
  yī
  ①<数>。《狼》：“～屠晚归。”
  ②<连>一边；一面。《兰亭集序》：“～觞～咏，亦足以畅叙幽情。”
  ③<形>同一；一样。《察今》：“古今～也。”
  ④<动>看作一样。《兰亭集序》：“固知～死生为虚诞，齐彭殇为妄作。”
  ⑤<动>统一。《阿房宫赋》：“六王毕，四海～。”
  ⑥<动>专一。《劝学》：“用心～也。”
  ⑦<副>全；一概。《岳阳楼记》：“而或长烟～空，皓月千里。”
  ⑧<副>一旦。《信陵君窃符救赵》：“公子诚～开口请如姬，如姬必许诺。”
  ⑨<副>才；刚刚。《赤壁之战》：“初～交战，操军不利。”
  ⑩<副>初次。《曹刿论战》：“～鼓作气。”
  【一旦】⒈有一天。⒉一时；忽然。⒊形容时间很短。
  【一何】多么。
  【一力】⒈协力。⒉竭力。
  【一体】关系密切，如同一个整体。一样，相同。
  【一昨】前些日子。
  '''
#单词释义
res_tr1 = r'【(.*?)】(.*)。'

#扣关键字
res_tr2 = r'([\u4e00-\u9fa5])\n'
#扣解释，需要多行连在一起
res_tr3 = r'(.*)”'
res_tr4 = r'\b[a-z]*[āáǎàōóǒòêēéěèīíǐìūúǔùǖǘǚǜüńňǹɑɡ]+[a-z]*\b'
# data_1 = {}
data_2 = {}
next_word = False
for lines in origin_file:
    #temp是关键字
    temp = re.findall(res_tr2, lines, re.S | re.M)
    pinyin = re.findall(res_tr4,lines,re.S|re.M)
    #temp2是单词释义
    temp2 = re.findall(res_tr1, lines, re.S | re.M)
    explanation = re.findall(res_tr3, lines, re.S | re.M)
    if len(temp) == 1:
        single_word = temp[0]
        next_word = False
        return_str = ''
        continue
    if pinyin:
        temp = ''
        for item in pinyin:
            temp += item
        return_str = return_str+temp
    if next_word == False and len(explanation):
        #explanation是解释
        explanation = re.findall(res_tr3, lines, re.S | re.M)
        # print(explanation)
        return_str = return_str+'\n'+explanation[0]+'\n'
    if len(temp2):
        next_word = True
        data_2[single_word] = return_str
        print(data_2)
pickle.dump(data_2,output1)
    # if one_word:
    #     return_str = ''
    #     single_word = re.findall(res_tr2,lines,re.S|re.M)
    #     pinyin = False
    #     dump_flag = False
    #     shiyi = re.findall(res_tr1, lines, re.S | re.M)
    #     if(not len(single_word) and not len(shiyi)):
    #         pinyin = True
    #     elif(len(list) and pinyin == False):
    #         m_tr = re.findall(res_tr3, lines, re.S | re.M)
    #         return_str = return_str + '\n' +m_tr
    #         print(return_str)
    #     elif(len(shiyi)):
    #         pinyin = False
    #         dump_flag = True
    #     elif(dump_flag==True):
    #         dump_flag = False
    #         data_2[single_word[0]] = return_str
    #         pickle.dump(data_2,output1)

#扣释义的
# for lines in origin_file:
#     m_tr = re.findall(res_tr1, lines, re.S | re.M)
#     for words in m_tr:
#         data_1[words[0]] = words[1]
#         # print(data_1)
# pickle.dump(data_1,output2)
# output2.close()
output1.close()
