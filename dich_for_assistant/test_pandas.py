fr = open("medium.txt", 'r', encoding='utf-8')
s = fr.read()
fw = open("b.txt", 'w', encoding='utf-8')
pos_start=pos_end=pos=0
d={}; index=0; flag=False

while pos_end!=-1:
    pos_end=s.find("\n", pos_start)
    print(s[pos_end+1])