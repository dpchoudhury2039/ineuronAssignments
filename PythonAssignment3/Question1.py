import operator


def myreduce(function, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = function(result, item)

    return result


numbers = [1, 2, 3, 4, 5]

reduced_result_add = myreduce(operator.add, numbers)
print("Result of Myreduce:", reduced_result_add)
reduced_result_mul = myreduce(operator.mul, numbers)
print("Result of Myreduce:", reduced_result_mul)
