def fg(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    for i in range(1, int(n**0.5) + 1): 
        if i * i == n:
            return True
    return False

with open('17new.txt') as f:
    s = [int(x) for x in f]

mp = -10**10
for i in range(len(s)):
    if fg(s[i]):
        if s[i]>mp:
            mp=s[i]
a = []
for i in range(len(s) - 1):
    if fg(s[i]) + fg(s[i + 1])==1: 
        if (s[i]+s[i+1])>mp:
            a.append(s[i] + s[i + 1])

print(len(a),max(a))


