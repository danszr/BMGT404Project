import time
import math
import collections
from datetime import date

def party():
	#Get the number of people in the party, catching input errors
	while True:
		try:
			party_number = int(input("Enter the amount of people in your party: "))
		except:
			print("Enter an integer!")
			continue
		else:
			break
	party_member = {}

	#collect names of each party member, and set their payment to 0 in the dictionary
	for i in range(party_number):
		member_name = input(f"Enter the name of party member #{i+1}: ")
		party_member[member_name] = 0
	print()
	payment_split(party_member, party_number)


def payment_split(ogPayers, payer_number):
	#set the total payment amount
	payment_amount = 0.0

	#Go through each payer's amount and set their amount to the appropriate amount, while keeping track of the
	#total payment amount
	for payer_name, amount in ogPayers.items():
		while True:
			try:
				payer_amount = float(input(f"How much did {payer_name} pay? $"))
			except:
				print("Enter a number!")
				continue
			else:
				break
		ogPayers[payer_name] = payer_amount
		payment_amount += payer_amount
	print()

	#Convert to ordereddict and Sort the dictionary by each user's payer_amount
	ogPayers = sorted(ogPayers.items(), key = lambda x: x[1])
	payers = collections.OrderedDict(ogPayers)
	#Get a reversed copy of the ordereddict so we can iterate through and settle the largest to the smallest payments
	payersReversed = collections.OrderedDict(sorted(payers.items(), reverse=True))

	sum = 0
	owes = {}
	#Get amount each person should pay and substract from actual payment to get how much they owe (negative) or should
	#be owed (positive)
	payment_per_person = payment_amount/payer_number
	for name, amount in payers.items():
		payers[name] = amount - payment_per_person

	#Go through each payer and for each one go through the reversed ordereddict and find an appropriate reveiver
	for giver_name, giver_amount in payers.items():
		if payers[giver_name] < 0:
			#Dictionary of dictionaries to track who owes money to which people
			owes[giver_name] = {}
			for receiver_name, receiver_amount in payersReversed.items():
				#First settles givers who owe the same amount as receivers should get paid and then settles the
				#largest giver and largest receivers
				if payers[receiver_name] > 0:
					if math.fabs(payers[giver_name]) == payers[receiver_name]:
						owes[giver_name][receiver_name] = payers[receiver_name]
					#If the giver owes more than the receiver should receive then the giver will give money until
					#The receiver's amount hits 0
					elif math.fabs(payers[giver_name]) > payers[receiver_name]:
						owes[giver_name][receiver_name] = payers[receiver_name]
						payers[giver_name] += payers[receiver_name]
						payers[receiver_name] = 0
					#Else if the receiver should receive more than the giver owes then the giver will give all of their
					#money to the receiver
					else:
						owes[giver_name][receiver_name] = -1*payers[giver_name]
						payers[receiver_name] += payers[giver_name]
						payers[giver_name] = 0

	#Print results
	for giver, receivers in owes.items():
		print(f"{giver} owes: ")
		for receiver, amount in owes[giver].items():
			if amount > 0:
				print(f"{receiver}: ${amount}")
		print()
party()
