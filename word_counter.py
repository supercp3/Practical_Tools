import re
from collections import Counter
'''
统计词频
'''
txt=open('word.txt').read()
new_txt=re.split('\W+',txt)
result=Counter(new_txt)
print(result.most_common())