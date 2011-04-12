from payflowpro.classes import (CreditCard, Amount, Profile, Address, Tracking, Response, CustomerInfo, AchPayment)
from payflowpro.client import PayflowProClient, find_classes_in_list, find_class_in_list

#PARTNER_ID = 'Paypal'
#VENDOR_ID = 'wiremine'
#USERNAME = 'wiremine'
#PASSWORD = 'twhtalmh2'



client = PayflowProClient(partner=PARTNER_ID, vendor=VENDOR_ID, username=USERNAME, password=PASSWORD, url_base='https://pilot-payflowpro.paypal.com')
credit_card = CreditCard(acct=5555555555554444, expdate="1212")
responses, unconsumed_data = client.sale(credit_card, Amount(amt=15, currency="USD"), extras=[Address(street="82 E 38th Street", zip="49423")])

#arc_payment = AchPayment(aba='111111118', acct='1111111111', accttype='S')
#customer = CustomerInfo(firstname='Bob Smith')
#responses, unconsumed_data = client.sale(arc_payment, Amount(amt=15, currency="USD"), extras=[customer])

print responses[0]