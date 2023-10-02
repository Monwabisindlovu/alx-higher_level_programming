#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = sum([x[0] * x[1] for x in my_list])
        denominator = sum([x[1] for x in my_list])
        return numerator / denominator
    return 0
