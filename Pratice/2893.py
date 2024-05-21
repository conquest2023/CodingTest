
s = "MCMXCIV"
sum=0
dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for i in range(len(s)):
    if s[i] in dic.keys():
       sum+=dic[s[i]]
print(sum)