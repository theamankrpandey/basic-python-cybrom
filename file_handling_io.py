import keyword
#print(keyword.kwlist,keyword.softkwlist)
for i in range(len(keyword.kwlist)):
    if i == (len(keyword.kwlist)-1):
        print (keyword.kwlist[i])