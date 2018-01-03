import re


if __name__ == '__main__':
    p = re.compile(r'imoo')
    print(p.__dir__())
    #help(p.match)
    #print(type(p))
    a='imooc'
    #print(a.find('i'))
    #print(a.startswith('m'))
    #print(p.match(a))
    str1=p.match(a)
    #print(str1.__dir__())
    print(str1.group())
    #help(str1.group)
    print(str1.span())
    def is_valid_email(addr):
        if re.match(r'^[\w\.\-]*\@\w+\.com$',addr):
            print(re.match(r'(^[\w\.\-]*)(@\w+\.com$)',addr).groups())
            return True
        else:
            return False
    print(is_valid_email('someone@gmail.com'))
    print(is_valid_email('bill.gates@microsoft.com'))
    print(is_valid_email('bob#example.com'))
    print(is_valid_email('mr-bob@example.com'))    
