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


def pallindrome(n):
   temp(n)
   reverse=0
   while temp!=0:
      remainder=temp%10
      reverse=reverse*10+remain
n = input("enter the number")
armstrong(n)