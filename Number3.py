def checkprime(num):
	a = 2
	while(a < num):
		if(num % a == 0):
			return 0
		a =+ 1
	return 1
		

def main():
	number = 600851475143
	a = 2
	while(1):
		print(number/a)
		if(number%a == 0):
			test = checkprime(number/a)
			if(test == 1):
				print(number/a)
				return
		a += 1
		
main()
