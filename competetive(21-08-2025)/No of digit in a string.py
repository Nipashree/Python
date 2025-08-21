import numpy as np

sen="I am Nipashree and I am 20 years old"
char=np.array(list(sen))

num=(list("01234567890"))

is_num=np.isin(char,num)

numeric=np.sum(is_num)
print(numeric)

