totalMiles = 0
totalGallons = 0

trip = int(input("Enter your miles driven: "))
while trip != -1:
	gallons = float(input("Enter your gallons used(Enter -1 to end): "))
	totalMiles+=trip
	totalGallons+=gallons

	all = trip/gallons
	combined = totalMiles/totalGallons

	print("the MPG is", all)
	print("the MPG combined is", combined)
	
	trip = int(input("Enter your miles driven: "))
	

	if totalGallons == 0:
	
		print("No trips recorded.")
	else:
		print("your MPG combined is", totalMiles/totalGallons)
	
