s1="play"
s2="football"
length_s2=len(s2)
#print(length_s2)
mid_s1=len(s1)//2-1
#print(mid_s1)
new_str = s1[:mid_s1+1] + str(length_s2) + s1[mid_s1+1:]
print(new_str)