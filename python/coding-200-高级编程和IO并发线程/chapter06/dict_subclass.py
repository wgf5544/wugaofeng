#不建议继承list和dict
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
my_dict["one"] = 1
print (my_dict)

from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
# my_dict["one"] = 1
print (my_dict)

from collections import defaultdict

def fun():
   # print(s)
    return [3,45,5]
my_dict = defaultdict(fun)
my_value = my_dict["bobby"]
print(my_value)


# set().issubset()

set([3,4],4)