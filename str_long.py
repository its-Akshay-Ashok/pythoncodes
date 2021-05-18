string1="aaadddrrzz"
result=''
first=string1[0]
count=1
i=1
while i<len(string1):
    if string1[i]==first:
        count=count+1
    else:
        result=result+str(count)+first
        first=string1[i]
        count=1
    if i==len(string1)-1:
        result = result+ str(count) +first
    i=i+1
print(result)