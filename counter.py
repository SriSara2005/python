from collections import Counter
def count_good_person(s1,s2):
    freq1=Counter(s1)
    freq2=Counter(s2)
    good_person_count=0
    for char in freq1:
        if freq1[char]==2 and freq2.get(char,0)==3:
            good_person_count+=1
    return good_person_count
s1="aabbjfd"
s2="aaabbbjkg"
print(count_good_person(s1,s2))

    