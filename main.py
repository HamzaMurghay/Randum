# # name = "hamza"
# # mylist = list(name)
# # print(mylist)
# #
# #
# # list = [4,42,235,2,3,23]
# # sum = 0
# #
# # for i in list:
# #     sum += i
# #
# # print(sum)
# #
# #
# # listu = [1,2,3,4,5]
# # #
# # # steps = int(input("no of steps: "))
# # #
# # # for i in range(steps):
# # #     print(listu[-steps:] + listu[0:len(listu)-steps])
# #
# #
# # inp = "578378923"
# #
# # listu2 = sorted(inp)
# # repeating = []
# #
# # for i in listu2:
# #     if listu2.count(i) > 1:
# #         repeating.append(i)
# #
# # print("Security key is:", len(set(repeating)))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # aaj ka bs
# #
# #
# #
# #
# #
# #
# #
# # # t = ()
# # # print(t)
# # # print(type(t))
# # #
# # # t = tuple()
# # # print(t)
# # # print(type(t))
# # #
# # # t = (264, 262, 24, 6, 6995, 363, 57)
# # # print(t)
# # # print(type(t))
# # #
# # # t=234,32,51,557,221,5,9,2,121,5
# # # print(t)
# # # print(type(t))
# # #
# # # t=eval(input("Enter any tuple: "))
# # # print(t)
# # #
# # # sum = 0
# # #
# # # for element in t:
# # #     sum += element
# # #
# # # print(f"Sum of tuple is {sum}")
# # # print(f"average value of tuple is {sum/len(t)}")
# # #
# # #
# # # s = set()
# # # print(s)
# # # print(type(s))
# # #
# # # s = {23,25,1,678,2,67,26,1,46, 6}
# # # print(s)
# # # print(type(s))
# # #
# # #
# # #
# # # # Q
# # #
# # # listu4 = []
# # #
# # # for i in range(10):
# # #     listu4.append(int(input(f"Enter {i+1}th element: ")))
# # #
# # # print(set(listu4))
# # #
# # #
# # # d = dict()
# # # print(d)
# # # print(type(d))
# # #
# # # d = {}
# # # print(d)
# # # print(type(d))
# # #
# # d = {101:"ahhhhh", 102: "this is sum", 103:"ahhhhhhh"}
# # print(d)
# # print(type(d))
# #
# #
# # rec = {}
# # n = int(input("Enter number of students: "))
# # for i in range(1,n+1):
# #     name = input("Enter Student Name: ")
# #     marks = input("Enter % of Marks of Students: ")
# #     rec[name] = marks
# #
# # print(rec)
# # for x in rec:
# #     print(x, "\t", rec[x])
# #
# #
# # d = {100:"hamza", 102:"ashish", 103:"sankalp"}
# # print(d[100])
# # print(d.get(100))
# # print(d.get(400))
# # print(d.get(100,  "Guest"))
# # print(d.get(400, "Guest"))
# #
# #
# #
# #
#
# def anagram_palindrome_checker():
#     inpu = input()
#
#     tryy = list(sorted(inpu))
#
#     for i in set(tryy):
#         odd_count = 0
#         if tryy.count(i)%2 != 0 and len(tryy)%2 == 0:
#             return False
#         elif tryy.count(i)%2 != 0 and len(tryy)%2 == 1:
#             if odd_count == 0:
#                 odd_count += 1
#             else:
#                 return False
#     return True
#
# def coins_earned(player_levels, enemy_levels, coins):
#     total_coins = 0
#
#     for i in player_levels:
#         for j in range(len(enemy_levels)):
#             if i >= enemy_levels[j]:
#                 total_coins += coins[j]
#
#     return total_coins
#
# def max_sum(array, k):
#     modified_array = sorted(array)
#     summ = 0
#     i = 0
#
#     while i < k:
#         # if
#         modified_array[i] *= -1
#         i += 1
#
#
#     return summ + sum(modified_array[k:])
#
# print(max_sum([-1,-1,3,5,2], 3))
#
# inp = [-10, -5, 5, 10]
#
# common_differences = []
#
# for i in range(len(inp) - 1):
#     common_differences.append(inp[i+1] - inp[i])
#
# for i in common_differences:
#     if common_differences.count(i) == 1:
#         position_to_append = common_differences.index(i) + 1
#         if i < 0:
#             value_to_append = inp[position_to_append] - common_differences[common_differences.index(i)+1]
#         elif i >= 0:
#             value_to_append = inp[position_to_append - 1] + common_differences[common_differences.index(i)+1]
#
#         inp.insert(position_to_append, value_to_append)
#         break
#
# print(inp)
#
#
#
#
#
# x = 48
# y = 18
# l1 = []
# l2 = []
#
# for i in range(1, x+1):
#     if x%i == 0:
#         l1.append(i)
# for i in range(1, y+1):
#     if y%i == 0:
#         l2.append(i)
#
# print(l1)
# print(l2)
# res = []
#
#
# s = lambda p: p*p*p
#
# print(s(7))
#
#
# class Age():
#
#     def __init__(self, age):
#         self.age = age
#
#     def can_vote(self):
#
#         if self.age >= 18:
#             print("YOu are eligible for voting")
#         else:
#             print("YOu are not eligible for voting")
#
#
# x = Age(1)
#
# x.can_vote()
#
# f1 = open("pic/labo.jpg", "rb")
# f2 = open("pic/ionno.png", "wb")
#
# bytes = f1.read()
# f2.write(bytes)
# print(bytes)
# print("new image is available")
#
# arr = [1, 2, 3 , 4 , 5]
# temp = []
# k = int(input("rotation steps: "))
# for i in range(0, -1 -(k-1), -1):
#     temp.append(arr[i])
#
# arr = arr[k:]
#
# for i in range(0, -1, -1):
#     arr.insert(i)


from abc import ABC, abstractmethod

class Irctc(ABC):
    @abstractmethod
    def bookTicket(self):
        pass

class MakeMyTrip(Irctc):

    def bookTicket(self):
        print("===============================================")
        print("Welcome to makemytrip.com")
        self.source = input("Enter Journey Start/Source station: ")
        self.destination = input("Enter Journey Destination name: ")
        self.date = input("Enter date of travelling: ")
        print("===============================================")

class GoIbibo(Irctc):

    def bookTicket(self):
        print("      Welcome to GoIbibo!\n\n")
        self.source = input("Enter Journey Start/Source station: ")
        self.destination = input("Enter Journey Destination name: ")
        self.date = input("Enter date of travelling: ")


class Yatra(Irctc):

    def bookTicket(self):
        print("\t Welcome oo Yatra.com \t")
        self.source = input("Enter Journey Start/Source station: ")
        self.destination = input("Enter Journey Destination name: ")
        self.date = input("Enter date of travelling: ")

m = MakeMyTrip()
m.bookTicket()


g = GoIbibo()
g.bookTicket()

y = Yatra()
y.bookTicket()