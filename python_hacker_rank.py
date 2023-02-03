# -*- coding: utf-8 -*-
"""Python-hacker-rank.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q_JJwppZrArwig-KsMpZYxud0SjStpcu
"""

import math
import os
import random
import re
import sys
    
n = int(input().strip())
if n%2 != 0:
  print("Weird")
elif (n%2 == 0 and (n in range(1,5))):
  print("Not Weird")
elif (n%2 == 0 and (n in range(5,21))):
  print("Weird")
elif (n%2 == 0 and n>20):
  print("Not Weird")
else: print("Hello")

grades=[]
for _ in range(int(input())):
  name = input()
  score = float(input())
  grades.append([name,score])

sorted_list=sorted(grades,key=lambda x: x[1])
length=len(sorted_list)
s_l_grades=[]
index=1
for i in range(0,length-1):
  if(sorted_list[i][1]==sorted_list[i+1][1]):
    index=index+1
    length=length-1
  else:
    break
s_l_grades.append(sorted_list[index])
for i in range(index,length-1):
  if(sorted_list[i][1]==sorted_list[i+1][1]):
    s_l_grades.append(sorted_list[i+1])
  else:
    break
final_lst=sorted(s_l_grades)
for i in range(0,len(final_lst)):
  print(final_lst[i][0])

n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
#print(student_marks[name] for name in stu)
query_name = input()
print(format(sum(m for m in student_marks[query_name])/len(student_marks[query_name]),'.2f'))

def count_substring(string, sub_string):
  #count=string.find(sub_string)
  count=0
  for i in range(len(string)):
    if string[i :i+len(sub_string)]== sub_string :
        count+=1
  return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

s = input()
print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))

N = int(input())
listops=[]
i=1
while i<=N:
  cmd=list(input().split())
  if cmd[0]=='insert':
    listops.insert(int(cmd[1]),int(cmd[2]))
  if cmd[0]=='remove':
    listops.remove(int(cmd[1]))
  if cmd[0]=='append':
    listops.append(int(cmd[1]))
  if cmd[0]=='sort':
    listops.sort()
  if cmd[0]=='pop':
    listops.pop()
  if cmd[0]=='reverse':
    listops.reverse()     
  if cmd[0]=='print':
    print(listops)
  i+=1

def swap_case(s):
    swapped=s.swapcase()
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

N = int(input())
arr=map(int,input().split())
mytuple=tuple(arr)
print(hash(mytuple))

def split_and_join(line):
    # write your code here
    s = (line.split(" "))
    s="-".join(s)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

def print_full_name(first, last):
    # Write your code here
    full_name="Hello " + first + " " + last + "! You just delved into python."
    print(full_name)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    s_new="".join(l)
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

n = int(input())
for i in range(1,n+1):
  print(i,end="")

a, *b = 10, 20, 30
print(type(b))

s = "python"
print(s[1:-3])

s = "code"
print(s.center(6, '%'))

from typing_extensions import TypeVarTuple
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
          if year%400==0:
            leap=True
          else:
            leap=False
        else:
          leap=True
    else:
        leap=False
    
    return leap

year = int(input())
print(is_leap(year))

x = int(input())
y = int(input())
z = int(input())
n = int(input())
final_list=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n] 
print(final_list)

#n = int(input())
arr = map(int, input().split())
scores=list(arr)
print(scores[0])
scores.sort()
print(scores)