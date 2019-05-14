import unittest2
import json
from src import first_k_special_numbers

# Computing values for the kth special number is computationally
# expensive for large values of k. Instead of computing these values
# at the time of test execution, we compute them all first and save
# them in a json file.
PRECOMPUTED_SPECIAL_NUMBERS_FILE = "test/special_numbers.json"


def first_k_special_numbers_brute_force(k):
	'''
	Find the first k special numbers using the brute force method.
	Use this method to generate values for testing.
	'''
	n = 19
	nums = [n]
	i = 0
	while i < k:
		n += 1
		s = sum_of_digits(n)
		if s == 10:
			nums.append(n)
			if i % 1000 == 0:
				print("Found the %dth special number..." % i)
			i += 1
	return nums


def sum_of_digits(n):
	'''
	Return the sum of the digits in n. N must be an integer.
	'''
	s = 0
	while n > 0:
		ones_digit = n - n // 10 * 10
		s += ones_digit
		n = n // 10
	return s


def save_nums_to_file(nums, filename):
	with open(filename, 'w') as f:
		json.dump(nums, f)


class TestFirstKSpecialNumbers(unittest2.TestCase):

	@classmethod
	def setUpClass(cls):
		print("loading")
		with open(PRECOMPUTED_SPECIAL_NUMBERS_FILE, "r") as f:
			cls.ExpectedValues = json.load(f)

		cls.NumValues = len(cls.ExpectedValues)

	def test_first_50000_special_numbers(self):
		results = first_k_special_numbers(TestFirstKSpecialNumbers.NumValues)
		k = 0
		for result, expected in zip(results, TestFirstKSpecialNumbers.ExpectedValues):
			self.assertEqual(
				result,
				int(expected),
				"%dth special Number was incorrect" % k
			)
			k += 1

