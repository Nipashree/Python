import numpy as np

sen="This is English Language"
chars=np.array(list(sen))

vowels=np.array(list("aeiouAEIOU"))
is_alphs=np.char.isalpha(chars)
is_vow=np.isin(chars,vowels)
 
vowel_c=np.sum(is_alphs & is_vow)
cons_c=np.sum(is_alphs & ~is_vow)

print(sen)
print("Total no of vowels:",vowel_c)
print("Total no of consonants:",cons_c)
