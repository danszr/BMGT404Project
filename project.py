import time
from datetime import date

def names():
	trip_name = input("Enter a name for your trip: ")
	party_number = int(input("Enter the amount of people in your party: "))
	party_member = {}
	
	for i in range(party_amount):
		member_name = input(f"Enter the name of party member #{i+1}: ")
		party_member[member_name] = 0
	print(party_member)

def payment_options():
	payment_list = []
	while True:
		payment_name = input("Enter a name for your payment, or 'quit' to quit: ")
		if payment_name.lower() == 'quit':
			break
		
		payment_year = int(input("Enter the year of your payment: "))
		payment_month = int(input("Enter the month of your payment: "))
		payment_day = int(input("Enter the day of your payment: "))
		payment_date = date(payment_year, payment_month, payment_day)

		payment_data = [payment_date, payment_name, payment_amount]
		payment_list.append(payment_data)

		payers = {}
		payment_amount = 0.0
		payer_number = int(input("How many people are on the payment? "))
		for i in range(payer_number):
			payer_name = input(f"Who is person #{i+1}? ")
			payer_amount = float(input(f"How much did {payer_name} pay? $"))
			payers[payer_name] = payer_amount
			payment_amount += payer_amount

		split(payment_amount, payer_number, payer_name)

def split(payment_amount, payer_number, payer_name, payers):
	while True:
		payment_choice = input("How would you like to split the bill?\n1) Equal split\n2) Dollar split\n3) Percentage split\n")
		if payment_choice == 1:
			sum = 0
			payment_per_person = payment_amount/payer_number
			for name, amount in payers.items():
				payers[name] = amount - payment_per_person
				sum += payers[name]
			print(payers[payer_name])

#			for giver_name, giver_amount in payers.items():
#				while payers[giver_name] < 0:
#					for receiver_name, receiver_amount in #payers.items():
#						if payers[receiver_name] = 0:
#							
#					
#
#		elif payment_choice == 2:
#			
#
#		elif payment_choice == 3:
#			
#
#		else:
#			print("That is not an option. Please choose a different option.")
#			continue
