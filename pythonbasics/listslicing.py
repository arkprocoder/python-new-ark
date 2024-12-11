
myslice=[1,2,4,6,7,9,10]
'''
val        +index    -index
1           0          -7      
2           1          -6
4           2          -5
6           3          -4
7           4          -3
9           5          -2
10          6          -1
'''



# syntax
# myslice[start:end-1]
# print(len(myslice))
# print(myslice[:])
# print(myslice[1:])
# print(myslice[:5])
# print(myslice[1:3])
# print(myslice[3:10])
# print(myslice[3:7])

# 3+1=4
# -2-2=-4
# -10+2=-8


# print("negative slicing")
# # print(myslice[-1])
# # print(myslice[-5])
# myslice=[1,2,4,6,7,9,10]
# # myslice[start:end-1]
# print(myslice[-5:])
# print(myslice[1:-3]) #(2,4,6)  [start:end-1] [1:-3-1] [1:-4]
# print(myslice[:-1])
# print(myslice[-5:-2])

myslice=[1,2,4,6,7,9,10]
print(myslice[::2])  #[start,end-1,step-size-1]
print(myslice[::3])  #[start,end-1,step-size-1]
print(myslice[::4])  #[start,end-1,step-size-1]
# # print(myslice[1:4:2])
# # print(myslice[::4])
print(myslice[::-1])
print(myslice[::1])
print(myslice[::-2])
print(myslice[::2])