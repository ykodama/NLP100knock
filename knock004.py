import re

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = re.sub('[.]', '', sentence)
word_list = sentence.split(" ")
# print(word_list)
a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
for i, wi in enumerate(word_list):
    if i+1 in a:
        dic[wi[:1]] = i+1
        # print(wi[:1])
    else:
        dic[wi[:2]] = i+1
        # print(wi[:2])
print(dic)
