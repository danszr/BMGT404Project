import time
import math
import collections
from datetime import date

def party():
	# trip_name = input("Enter a name for your trip: ")
	while True:
		try:
			party_number = int(input("Enter the amount of people in your party: "))
		except:
			continue
		else:
			break
	party_member = {}

	for i in range(party_number):
		member_name = input(f"Enter the name of party member #{i+1}: ")
		party_member[member_name] = 0
	print()
	payment_split(party_member, party_number)

def payment_split(ogPayers, payer_number):

	#payment_list = []
	#while True:
	# payment_name = input("Enter a name for your payment, or 'quit' to quit: ")
	#if payment_name.l/ower() == 'quit':
		#break

	# payment_year = int(input("Enter the year of your payment: "))
	# payment_month = int(input("Enter the month of your payment: "))
	# payment_day = int(input("Enter the day of your payment: "))
	# payment_date = date(payment_year, payment_month, payment_day)

	payment_amount = 0.0
	for payer_name, amount in ogPayers.items():
		while True:
			try:
				payer_amount = float(input(f"How much did {payer_name} pay? $"))
			except:
				continue
			else:
				break
		ogPayers[payer_name] = payer_amount
		payment_amount += payer_amount
	print()
	ogPayers = sorted(ogPayers.items(), key = lambda x: x[1])
	payers = collections.OrderedDict(ogPayers)
	payersReversed = collections.OrderedDict(sorted(payers.items(), reverse=True))

	sum = 0
	owes = {}
	payment_per_person = payment_amount/payer_number
	for name, amount in payers.items():
		payers[name] = amount - payment_per_person

	for giver_name, giver_amount in payers.items():
		if payers[giver_name] < 0:
			owes[giver_name] = {}
			for receiver_name, receiver_amount in payersReversed.items():
				if payers[receiver_name] > 0:
					if math.fabs(payers[giver_name]) == payers[receiver_name]:
						owes[giver_name][receiver_name] = payers[receiver_name]
					elif math.fabs(payers[giver_name]) > payers[receiver_name]:
						owes[giver_name][receiver_name] = payers[receiver_name]
						payers[giver_name] += payers[receiver_name]
						payers[receiver_name] = 0
					else:
						owes[giver_name][receiver_name] = -1*payers[giver_name]
						payers[receiver_name] += payers[giver_name]
						payers[giver_name] = 0

	for giver, receivers in owes.items():
		print(f"{giver} owes: ")
		for receiver, amount in owes[giver].items():
			if amount > 0:
				print(f"{receiver}: ${amount}")
		print()
party()
