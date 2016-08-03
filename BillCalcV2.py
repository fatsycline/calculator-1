tip_amount = 0
total_bill = 0
split_amount = 0
def calculate_bill(original_bill_amount, tip_percentage = 18, split_number = 1):
	global tip_amount
	global total_bill
	global split_amount
	tip_amount = original_bill_amount * tip_percentage/100.0
	total_bill = original_bill_amount + tip_amount
	split_amount = total_bill / split_number
	print "Original bill is %f" %  (original_bill_amount,)
	print "tip amount %f" %  (tip_amount,)
	print "total bill %f" %  (total_bill,)
	print "split amount %f" %  (split_amount,)

#calculate_bill(100)
#calculate_bill(100, tip_percentage = 18, split_number = 1)
#calculate_bill(100, tip_percentage = 20)
#calculate_bill(100, tip_percentage = 25, split_number = 3)
calculate_bill(100, split_number=2)
