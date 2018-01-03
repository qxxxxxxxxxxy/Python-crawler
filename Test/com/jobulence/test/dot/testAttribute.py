'''
Created on 2017年12月28日

@author: ll
'''

class MyClass(object):
    
    def __getattribute__(self, value):
        return 'aasdf'


    def __init__(self):
        return
        
if __name__ == '__main__':
    b=MyClass()
    print(b.assss)
        