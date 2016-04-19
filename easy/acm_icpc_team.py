#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
people = []
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)
    
    s = set()
    for idx, i in enumerate(topic_t):
        if i == '1':
            s.add(idx)
    people.append(s)
    
mv = 0
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        lv = len(people[i]|people[j])
        if lv > mv:
            mv = lv
            cnt = 1
        elif lv == mv:
            cnt += 1
print(mv)
print(cnt)
