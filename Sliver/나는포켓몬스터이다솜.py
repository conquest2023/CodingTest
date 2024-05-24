"""내가푼코드"""
n,m=map(int,input().split())
i=0
strs=dict()

for _ in range(n):
    word=input()
    i+=1
    strs[word]=i

for _ in range(m):
    target=input()
    for key,value in strs.items():
        if target==key:
            print(value)
        elif target==value:
            print(key)
"""개선"""
import sys

n, m = map(int, input().split())

# 리스트에 포켓몬 저장
pokedic_int_key = {}
pokedic_name_key = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:
        print(pokedic_int_key[int(item)-1])
    else:
        print(pokedic_name_key[item]+1)