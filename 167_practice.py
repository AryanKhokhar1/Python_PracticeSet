def check_palindrome(num , num2):
    if(num == num2):
        print(num,'is a Palindrome Number')
    else:
        print(num,'is not a Palindrome Number')
        return
num = input('Enter the Number(to palindrome condition) :')
num2 = num[::-1]
check_palindrome(num , num2)