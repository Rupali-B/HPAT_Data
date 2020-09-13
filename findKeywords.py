#finding the most common keywords in the string

from collections 
import Counter
#text=''
words = text.split()
print (words)
Counter = Counter(words)
top_twenty = Counter.most_common(20)
print(top_twenty)
