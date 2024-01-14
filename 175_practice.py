def fun_1(name):
    # print(name)
    company = input('Enter the name of your Company :')
    def fun_2(name,company):
        print(f'Hello Mr/Mrs/Ms {name}. Your company is {company}')
    fun_2(name,company)
nam = input("Enter the your Name :")
fun_1(nam)