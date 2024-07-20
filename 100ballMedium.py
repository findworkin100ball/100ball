def dv(n):
    if bin(abs(n))[2:].count('1')%2==0:
        return True
    else:
        return False


f = open('17new.txt')
s=[int(x) for x in f]
a=[]
mn=10**10
for i in range(len(s)):
    if s[i]<mn and s[i]>0:
        mn=s[i]
        
for i in range(len(s)-1):
    if dv(s[i])+dv(s[i+1])==1:
        if s[i]+s[i+1]>mn:
            a.append(s[i]+s[i+1])
            
print(len(a),bin(min(a))[2:].count('1'))


        
    
