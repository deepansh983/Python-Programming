row1={'q','w','e','r','t','y','u','i','o','p'}
row2={'a','s','d','f','g','h','j','k','l'}
row3={'z','x','c','v','b','n','m'}

n=int(input())
words=[]
for _ in range(n):
    words.append(input().strip())

for word in words:
     w=set(word)
     
     if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
        print(word)
    