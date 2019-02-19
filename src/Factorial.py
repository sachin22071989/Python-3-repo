#Factorial of a given Number
Num=input("Enter a number:");
Num=int(Num);
Fact=1;
for i in range(1,Num+1):
	Fact=Fact*i;
print("Factorial of the Number is:" , Fact);
