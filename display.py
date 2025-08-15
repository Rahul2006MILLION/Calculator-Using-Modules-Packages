from Logic.code import addit,subtra,multi,divi
def choicee():
	choice=''
	while choice!=1 and choice!=2 and choice!=3 and choice!=4:
		choice=int(input("1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division:"))
		if choice==1:
			n1=int(input("1st Number: "))
			n2=int(input("2nd Number: "))
			print(f"{n1}+{n2}={addit(n1,n2)}")
			break
		elif choice==2:
			n1=int(input("1st Number: "))
			n2=int(input("2nd Number: "))
			print(f"{n1}-{n2}={subtra(n1,n2)}")
			break
		elif choice==3:
			n1=int(input("1st Number: "))
			n2=int(input("2nd Number: "))
			print(f"{n1}*{n2}={multi(n1,n2)}")
			break
		elif choice==4:
			n1=int(input("1st Number: "))
			n2=int(input("2nd Number: "))
			if n2!=0:
				print(f"{n1}/{n2}={divi(n1,n2)}")
			else:
				print("Cannot Divide by 0")
			break
		else:
			print("Invalid Input")


