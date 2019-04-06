__author__ = 'wgf'
__date__ = ' 上午11:29'

def ask(name='wgf'):
    print(name)

class person():
    def __init__(self):
        print("wgf1")

func = ask
func()

my_class = person
my_class()

object_list=[]
object_list.append(ask)
object_list.append(person)

for obj in object_list:
    print(obj())