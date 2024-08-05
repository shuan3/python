from collections import Counter
myList=['a','a',10,10,10]
print(Counter(myList))





from collections import defaultdict

d=defaultdict(lambda:list())
d['correct']=100
print(d['correct'])
print(d['corresct'])