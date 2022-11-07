##
def armstrong(n):

   temp=n
   result=0
   while temp!=0:
      remainder=temp%10
      result=remainder**3+result
      temp=temp//10
   if result==n:
      print(n,"is armstrong number")
   else:
      print(n,"is not an armstrong number")


def palindrome(n):
   temp(n)
   reverse=0
   while temp!=0:
      remainder=temp%10
      reverse=reverse*10+remainder
      temp=temp//10

   if n==reverse:
      print(n,"is palindrome")
   else:
      print(n,"Is not a palindrome")
n = input("enter the number:- ")
armstrong(n)
palindrome(n)