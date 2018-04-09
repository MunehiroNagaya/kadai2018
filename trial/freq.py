import re,sys
from collections import Counter

args = sys.argv
f = open(args[1],'r',encoding='utf-8')
fall = f.read()
falla = fall.rstrip()
words = re.split('[\n ]+',falla)
count = Counter(words)
for word, cnt in count.most_common():
    print(cnt, word)
f.close
