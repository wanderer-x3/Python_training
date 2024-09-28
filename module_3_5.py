from Lesson.module_2_4 import numbers


def get_multiplied_digits(number):
    str_number = list(str(number))
    first = int(str_number[0])
    #len_ = len(str_number)
    #for i in range(1,len_):
    num = int(str_number[1])

    #del str_number[0]
    #str_number = str_number.pop(0)
    if num <= 1:
        del str_number[1]
    #else:
    return first * get_multiplied_digits(int(str_number[1:]))

            # print(num)
    #print(first)
    #return str_number



result = (get_multiplied_digits(40203))
print(result)

# 24