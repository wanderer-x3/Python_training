
def get_multiplied_digits(number):
    if number == 0:
        return 1
    else:
    #     str_number = str(number)
    #     #first = int(str_number[0])
    #
    #     return int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))
        str_number = str(number)
        #print('str_number',str_number)
        # str_number = list(str(number))
        first = int(str_number[0])
        #print('first', first)
        #len_ = len(str_number)
        #for i in range(1,len_):
        num = int(str_number[1:])
        #print(num)
        #del str_number[0]
        #str_number = str_number.pop(0)
        # if num <= 1:
            #del int(str_number[1])
        # #else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = (get_multiplied_digits(40203))
print(result)

# 24


# def get_multiplied_digits(number):
#     str_number = list(str(number))
#     first = int(str_number[0])
#     #len_ = len(str_number)
#     #for i in range(1,len_):
#     num = int(str_number[1])

#     #del str_number[0]
#     #str_number = str_number.pop(0)
#     if num <= 1:
#         del str_number[1]
#     #else:
#     return first * get_multiplied_digits(int(str_number[1:]))

#             # print(num)
#     #print(first)
#     #return str_number



# result = (get_multiplied_digits(40203))
# print(result)

# # 24
