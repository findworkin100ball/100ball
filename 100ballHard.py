f = open('17new.txt')
s= [int(x) for x in f]
a=[]

mntr=10**10
for i in range(len(s)):
    if s[i]<mntr:
        if s[i]>0:
            if 100<=(abs(s[i]))<=999:
                mntr=s[i]

for i in range(len(s)-2):
    if abs(s[i])%3==0 and abs(s[i+1])%3==0:
        if (s[i]+s[i+1])%2==0:
            if (abs(s[i]+s[i+1])%7)!= mntr%7:
                a.append((s[i]+s[i+1]))
print(len(a),max(a))
