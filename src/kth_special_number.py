
SPECIAL_NUMBERS_FILE = "special_numbers.json"


def kth_special_number(k):
	'''
	Find the kth special number, where a special number is defined
	as an integer whose digits add up to 10. The sequence is 0-indexed,
	so kth_special_number(0) = 19, kth_special_number(1) = 28, etc.
	'''
	digits = [1, 9]
	digit_to_reset = -1

	for _ in range(k):

		# For all X-digit integers, if a certain integer has 9 as its
		# most-significant digit is 9 and 1 as its second-most-significant,
		# then it is the greatest X-digit integer whose digits sum up to 10.
		# Time to add another digit.
		if digits[0] == 9 and digits[1] == 1:

			# The minimum-value integer that has X+1 digits, and whose digits
			# add up to 10, is a number with 1 as its most-significant digit,
			# 9 in the ones place, and 0s in between.
			digits = [1] + [0] * (len(digits) - 1) + [9]
			digit_to_reset = -1
			continue

		# Can't reset a digit whose value is 0, and can't increment a digit
		# whose value is 9. Time to move left (one more significant digit).
		digit_to_increment = digit_to_reset - 1
		if digits[digit_to_reset] == 0 or digits[digit_to_increment] == 9:
			digit_to_increment -= 1
			digit_to_reset -= 1

		# Save before resetting
		previous_value = digits[digit_to_reset]

		# Reset the digit
		digits[digit_to_reset] = 0

		# "Give" one value from this digit to the next-most-significant digit
		digits[digit_to_increment] += 1

		# "Give" the rest of the value from this digit to the one's digit
		digits[-1] = max(0, previous_value - 1)

		# If the one's digit is now non-zero, then it is the next digit to be reset.
		if digits[-1] > 0:
			digit_to_reset = -1

	return int("".join([str(digit) for digit in digits]))


def first_k_special_numbers(k):
	'''
	Return a list of the first k specials number, where a special number
	is defined as an integer whose digits add up to 10. The sequence is
	0-indexed, so kth_special_number(0) = 19, kth_special_number(1) = 28, etc.
	'''
	nums = [19]
	digits = [1, 9]
	digit_to_reset = -1

	for _ in range(k):

		# For all X-digit integers, if a certain integer has 9 as its
		# most-significant digit is 9 and 1 as its second-most-significant,
		# then it is the greatest X-digit integer whose digits sum up to 10.
		# Time to add another digit.
		if digits[0] == 9 and digits[1] == 1:

			# The minimum-value integer that has X+1 digits, and whose digits
			# add up to 10, is a number with 1 as its most-significant digit,
			# 9 in the ones place, and 0s in between.
			digits = [1] + [0] * (len(digits) - 1) + [9]
			nums.append(int("".join([str(digit) for digit in digits])))
			digit_to_reset = -1
			continue

		# Can't reset a digit whose value is 0, and can't increment a digit
		# whose value is 9. Time to move left (one more significant digit).
		digit_to_increment = digit_to_reset - 1
		if digits[digit_to_reset] == 0 or digits[digit_to_increment] == 9:
			digit_to_increment -= 1
			digit_to_reset -= 1

		# Save before resetting
		previous_value = digits[digit_to_reset]

		# Reset the digit
		digits[digit_to_reset] = 0

		# "Give" one value from this digit to the next-most-significant digit
		digits[digit_to_increment] += 1

		# "Give" the rest of the value from this digit to the one's digit
		digits[-1] = max(0, previous_value - 1)

		# If the one's digit is now non-zero, then it is the next digit to be reset.
		if digits[-1] > 0:
			digit_to_reset = -1

		nums.append(int("".join([str(digit) for digit in digits])))

	return nums
