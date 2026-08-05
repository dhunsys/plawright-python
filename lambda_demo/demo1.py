from functools import reduce

import pytest
# a=lambda x: x**2
# where a=function name
# lambda=keyword
# x=argument
# x**2=expression

def test_multiply():
    f1=lambda p:p*5
    print("calling lambda function f1:",f1(6))

def test_square():
    square=lambda p:p*p
    print("calling lambda function square:",square(6))

def test_add_2_no():
    add=lambda p,q:p+q
    print("calling lambda function add:",add(6,5))


def test_even_odd():
    as_even = lambda n: "Even" if n % 2 == 0 else "Odd"
    print("calling lambda function add:", as_even(5))
    print("calling lambda function add:",as_even(6))

def test_filter_even():
    number=[1,2,5,7,4]
    print("calling filter to get all even:",list(filter(lambda x: x % 2 == 0, number)))

def test_filter_name_start_with_A():
    names=["MSH","Akbar","ARA"]
    result=list(filter(lambda x: x.startswith("A"), names))
    print("calling filter to get all name starts with A:",result)
def test_filter_dic_with_sal_50000():
    employees = [
        {"name": "John", "salary": 50000},
        {"name": "Alice", "salary": 70000},
        {"name": "Bob", "salary": 45000},
        {"name": "Mohd", "salary": 50000}
        ]
    result=list(filter(lambda x:x["salary"]==50000,employees))
    print("calling filter to get all employee has sal 50000:",result)

def test_filter_on_tuple():
    numbers = (1, 2, 3, 4, 5)
    result = filter(lambda x: x > 3, numbers)
    print(tuple(result))
def test_filter_on_string():
    text = "python"
    result = filter(lambda ch: ch in "aeiou", text)
    print("".join(result)) # why join

def test_filter_on_set():
    numbers = {1, 2, 3, 4, 5}
    result = filter(lambda x: x % 2 == 1, numbers)
    print(set(result))
def test_filter_on_dic():
    marks = {
    "Math": 50,
    "English": 15,
    "Science": 70
    }
    result = filter(lambda k: marks[k] > 20, marks)
    print(list(result))
def test_filter_on_range():
    result = filter(lambda x: x % 3 == 0, range(1, 11))
    print(list(result))

def test_reduce_sum():
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    result = reduce(lambda x, y: x + y, numbers)
    print(result)# 15

def test_reduce_mul():
    from functools import reduce
    numbers = [1, 2, 3, 4]
    result = reduce(lambda x, y: x * y, numbers)
    print(result)# 24
def test_reduce_max():
    from functools import reduce
    numbers = [1, 28, 300, 4]
    result = reduce(lambda x, y: x if x>y else y, numbers)
    print(result)# 300

def test_reduce_dic_with_sum_sal():
    marks = {"Math": 30, "Sci": 50,"Eng": 55, "Geog": 20,}
    result=reduce(lambda s1,s2:s1+s2,marks.values())
    print("Sum of sal in a dictionary:",result)
def test_reduce_total_char_all_string():
    names = ["John", "Alice", "Bob"]
    total_chars = reduce(
        lambda total, name: total + len(name),
        names,
        0
    )
    print(total_chars)
def test_reduce_total_char_in_string():
    names = "John"
    total_chars = reduce(
        lambda total, name: total + len(name),
        names,
        0
    )

    print(total_chars)