lVar = [1,4,2,3,4,5,4,4,3,4,31,7,4]
# count = 0
# for i in lVar:
#     if i == 4:
#         count+=1
# print("the count is ",count)

count_of_occurance = len([num for num in lVar if num == 4])
print(count_of_occurance)