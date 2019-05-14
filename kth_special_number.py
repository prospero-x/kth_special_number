import json


SPECIAL_NUMBERS_FILE = "special_numbers.json"

def kth_special_number(k):
	digits = [1,9]
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
	nums = [19]
	digits = [1,9]
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

def first_k_special_numbers_brute_force(k):
	n = 19
	nums = [n]
	i = 0
	while i < k:
		n += 1
		s = sum_of_digits(n)
		if s == 10:
			print(i)
			nums.append(n)
			i += 1
	return nums


def sum_of_digits(n):
	s = 0
	while n > 0:
		ones_digit = n - n // 10 * 10
		s += ones_digit
		n = n // 10
	return s

def save_nums_to_file(nums, filename):
	with open(filename, 'w') as f:
		json.dump(nums, f)


def test_kth_special_number(k):
	passed = True
	expected_nums = first_k_special_numbers_brute_force(k)
	for k, expected in enumerate(expected_nums):
		result = kth_special_number(k)
		if result != expected:
			passed = False
			print("For k=%d, expected %d but got %d instead" % (k, expected, result))

	if passed:
		print("Verified %d correct special numbers" % len(expected_nums))

if __name__ == '__main__':
	# nums = first_k_special_numbers_brute_force(50000)
	# save_nums_to_file(nums, SPECIAL_NUMBERS_FILE)
	test_kth_special_number(500)