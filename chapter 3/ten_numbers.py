ten_numbers = 0
largest = 0
second_largest = 0

while ten_numbers <= 10:
	ten_numbers+=1
	second_ten_numbers = int(input("Enter a number: "))
	
	largest = ten_numbers
	
	if second_ten_numbers > largest:
		largest = second_ten_numbers
print(largest)