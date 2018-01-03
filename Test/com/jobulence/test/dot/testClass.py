'''
Created on 2017年12月27日

@author: ll
'''
class MyClass(object):
    
    hobby="play"
    def __init__(self, age,weight,gender):
        if isinstance(age, int):
            self.age=age
        else:
            raise Exception('age must be int')
        self._weight=weight
        self.__gender=gender
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    @property
    def get_gender(self):
        return self.__gender
    def __eq__(self,other):
        if isinstance(other, MyClass):
            if self.age==other.age:
                return True
            else:
                return False
        else:
            raise Exception('the object must be MyClass')
    def __add__(self,other):
        if isinstance(other, MyClass):
            return self.age+other.age
        else:
            raise Exception('the type must be MyClass')        
        
class NewClass(MyClass):
    def __init__(self,age,weight,gender):
        super(MyClass,self).__init__(age, weight, gender)
if __name__ == '__main__':
    b = MyClass(11,120,'男')
    c = MyClass(12,110,'男')
    print(b==c)
    print(b+c)
    print(b.get_gender)
    print(MyClass.get_hobby())
    print(type(b))
    print(b.__dir__())
    print(dir(b))
    print(b.__dict__)