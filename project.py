def names():
	trip = input("Enter a name for your trip: ")
	party_amount = int(input("Enter the amount of people in your party: "))
	party_member = {}
	for i in range(party_amount):
		member_name = input(f"Enter the name of party member #{i+1}: ")
		party_member[member_name] = 0
	print(party_member)

def payment_options():
	payer_amount = int(input("How many people are on this payment? "))
	payer_name = input("Who is on this payment? ")
	payment_choice = input("How would you like to split the bill?\n1) Equal split\n2) Dollar split\n3) Percentage split\n")

names()