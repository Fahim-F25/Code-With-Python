s =  "a good   example"

l = list(s.split())


i = 1
for item in l:
   print(l[len(l)-i]," ",end='')
   i = i + 1
