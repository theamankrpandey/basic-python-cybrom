l = "amman"
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)

for j in range(len(l)):
    if d[l[j]] ==1:
        print("index",(j))
        print("character",l[j])
        break
    else:
        pass  
