# 백준 1541번 잃어버린 괄호 (2시간후 구글링)
# import sys
#
# working_list = list(sys.stdin.readline().rstrip().split("-"))
# num_list = []
# for i in working_list:
#     count = 0
#     a = i.split("+")
#     for j in a:
#         count += int(j)
#     num_list.append(count)
# total = int(num_list[0])
# for i in range(1, len(num_list)):
#     total -= num_list[i]
#
# print(total)
#백준 2217번
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# rope_list = []
# max_weight = 0
# for i in range(num):
#     rope_list.append(int(sys.stdin.readline().rstrip()))
# rope_list.sort()
# index = 0
# for i in range(num):
#     temp = rope_list[i] * (num - i)
#     if temp > max_weight:
#         max_weight = temp
#
# print(max_weight)
#백준 2869번 달팽이는 올라가고 싶다
#
# import sys
#
# a, b, v = map(int, sys.stdin.readline().rstrip().split())
# if (v - a) % (a - b) != 0:
#     print(((v - a) // (a - b)) + 2)
# else:
#     print(((v - a) // (a - b)) + 1)

#백준 1929번 소수 구하기
# import sys
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# prime = [False] * (b+1)
#
# for i in range(2, b+1):
#     if prime[i] == False:
#         j = i * 2
#         while j <= b:
#             prime[j] = True
#             j += i
#
# for i in range(a, b+1):
#     prime[i] = not prime[i]
#
# if a > 2:
#     for i in range(a, b+1):
#         if prime[i]:
#             print(i)
# else:
#     for i in range(2, b+1):
#         if prime[i]:
#             print(i)

#백준 2609번 최대공약수와 최소공배수
# import sys
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a,b):
#     return a*b / gcd(a, b)
#
# a, b = map(int, sys.stdin.readline().rstrip().split())
#
# print(int(gcd(a, b)))
# print(int(lcm(a, b)))

# 백준 10845번 큐
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# queue = []
# queue_size = 0
#
# def push(x):
#     global queue_size
#     global queue
#
#     queue.append(x)
#     queue_size += 1
#
#
# def pop():
#     global queue_size
#     global queue
#
#     if queue_size > 0:
#         queue_size -= 1
#         temp = queue[0]
#         queue.remove(queue[0])
#         return temp
#     else:
#         return -1
#
#
# step = ""
#
# for i in range(num):
#     step = sys.stdin.readline().rstrip()
#     if step[0:2] == "pu":
#         push(int(step[5:]))
#     elif step[0:2] == "po":
#         print(pop())
#     elif step[0:2] == "si":
#         print(queue_size)
#     elif step[0:2] == "em":
#         if queue_size == 0:
#             print(1)
#         else:
#             print(0)
#     elif step[0:2] == "fr":
#         if queue_size == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif step[0:2] == "ba":
#         if queue_size == 0:
#             print(-1)
#         else:
#             print(queue[-1])

#백준 11650번 좌표 정렬하기
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# x_y_list = []
#
# for i in range(num):
#     x_y_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# x_y_list.sort(key=lambda x:(x[0], x[1]))
#
# for x, y in x_y_list:
#     print(x, y)

#백준 11651번 좌표 정렬하기2
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# x_y_list = []
#
# for i in range(num):
#     x_y_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# x_y_list.sort(key=lambda x:(x[1], x[0]))
#
# for x, y in x_y_list:
#     print(x, y)

#백준 2164 카드2
# import sys
# from collections import deque
#
# num = int(sys.stdin.readline().rstrip())
#
# card_list = deque()
# list_num = num
# for i in range(num):
#     card_list.append(i+1)
#
# while True:
#     if list_num == 1:
#         break
#     card_list.popleft()
#     list_num -= 1
#     card_list.append(card_list[0])
#     card_list.popleft()
#
# print(card_list[0])

#백준 1920번 수찾기
# import sys
# from bisect import bisect_left, bisect_right
#
# def count_by_range(a, l, r):
#     right_index = bisect_right(a, r)
#     left_index = bisect_left(a, l)
#     return right_index - left_index
#
# size = int(sys.stdin.readline().rstrip())
#
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# find_size = int(sys.stdin.readline().rstrip())
#
# find_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# num_list.sort()
#
# for i in find_list:
#     temp = count_by_range(num_list, i, i)
#     if temp > 0:
#         print(1)
#     else:
#         print(0)

#백준 7568번 덩치 미해결 ################################################################
# import sys
#
# num = int(sys.stdin.readline().rstrip())
#
# pre_list = []
# people_list = []
# final_list = []
# for i in range(num):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     people_list.append([x, y])
#
# pre_list = people_list[:]
#
# people_list.sort(key = lambda x : x[0], reverse=True)
# i = 0
# while i < num:
#     temp = [people_list[i]]
#     for j in range(i+1, num):
#         if people_list[i][1] < people_list[j][1]:
#             temp.append(people_list[j])
#             i += 1
#     i += 1
#     final_list.append(temp)
#
#
# for i in pre_list:
#     for j in range(len(final_list)):
#         if i in final_list[j]:
#             if j == 0:
#                 print(1, end = " ")
#             else:
#                 print((j+1) + (len(final_list[j-1])-1), end=" ")

#백준 10816번 숫자카드 2

# import sys
# from bisect import bisect_left, bisect_right
#
# a_num = int(sys.stdin.readline().rstrip())
# a_list = list(map(int, sys.stdin.readline().rstrip().split()))
# a_list.sort()
# b_num = int(sys.stdin.readline().rstrip())
# b_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# def count_by_range(a_list, l, r):
#     right_index = bisect_right(a_list, r)
#     left_index = bisect_left(a_list, l)
#     return right_index - left_index
#
# for i in b_list:
#     print(count_by_range(a_list, i, i), end=" ")

#백준 1357 뒤집힌 덧셈
# import sys
#
# def reverse(a):
#     a = a[::-1]
#     return int(a)
#
# a, b = sys.stdin.readline().rstrip().split()
#
# a = reverse(a)
# b = reverse(b)
#
# final = reverse(str(a+b))
#
# print(final)

#백준 4949번 균형잡힌 세상
# import sys
#
# while True:
#     complete = True
#     stack = []
#     line = sys.stdin.readline().rstrip()
#     if line == ".":
#         break
#     for i in range(len(line)):
#         if line[i] == "(":
#             stack.append("(")
#         elif line[i] == "[":
#             stack.append("[")
#         elif line[i] == ")":
#             if len(stack) == 0:
#                 complete = False
#             elif stack.pop() != "(":
#                 complete = False
#         elif line[i] == "]":
#             if len(stack) == 0:
#                 complete = False
#             elif stack.pop() != "[":
#                 complete = False
#
#     if not complete or len(stack) != 0:
#         print("no")
#     else:
#         print("yes")