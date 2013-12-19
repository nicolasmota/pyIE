#REFATORAR
#RETIRA ESSE METODO algoritm_df de dentro do check. Assim ele pode ser reaproveitado
def check(st_reg_number):
	"""Checks the number valiaty for the Distrito Federal state"""
	
	if st_reg_number[0:2] != '07':

		return False

	if len(st_reg_number) !=  13:

		return False

	def algoritm_df(st_reg_number): 
		st_reg_number = str(st_reg_number)
		weights = [4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
		digits = st_reg_number[:len(st_reg_number) - 2]
		check_digits = st_reg_number[-2:]
		DIVISOR = 11
		
		sum = 0
		for i in range(len(digits)):
			sum = sum + int(digits[i]) * weights[i]

		rest_division = sum % DIVISOR
		first_digit = DIVISOR - rest_division
		
		if first_digit == 10 or first_digit == 11:
			first_digit = 0

		if str(first_digit) != check_digits[0]:

			return False

		digits = digits + str(first_digit)
		weights = [5] + weights

		sum = 0
		for i in range(len(digits)):
			sum = sum + int(digits[i]) * weights[i]

		rest_division = sum % DIVISOR
		second_digit = DIVISOR - rest_division

		if second_digit == 10 or second_digit == 11:
			second_digit = 0
		
		return str(first_digit) + str(second_digit) == check_digits    
	
	return algoritm_df(st_reg_number)
	

