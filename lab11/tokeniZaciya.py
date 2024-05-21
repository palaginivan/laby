import nltk.tokenize
import re
from collections import Counter
with open("isxodniy.txt", encoding="utf-8") as f:
    text = f.read()
run1 = text.split()
with open("split.txt", "w", encoding="utf-8") as d:
    for i in range(len(run1)):
        d.write(run1[i] + "\n")
run2 = re.findall(r"\w+", text)
with open("regular.txt", 'w', encoding="utf-8") as dd:
    for i in range(len(run2)):
        dd.write(run2[i] + "\n")
run3 = nltk.tokenize.word_tokenize(text)
file = open("nltk.txt", "w", encoding="utf-8")
for i in range(len(run3)):
    file.write(run3[i] + '\n')
file.close()


print(len(text))
print(sum(Counter(text).values()))