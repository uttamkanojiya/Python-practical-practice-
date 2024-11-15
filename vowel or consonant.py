#program to check the given letter is alphabet a vowel or consonant or not
user=(input('Enter any one letter by yourself:'))
if user in ('a','e','i','o','u'):
    print("The given letter by you is",user,'and it is a vowel')
#elif user%1==1:
#    print('The given input is not a letter')
else:
    print("The given letter by you is",user,"and it is a consonant")

