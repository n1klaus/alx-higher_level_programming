#!/usr/bin/python3
for num in range(0, 100):
	if num < 10:
		print("{:0>2}".format(num), end=", ")
	else:
		if str(num) == (str(num)[::-1]) or int(str(num)[::-1]) < num:
				continue
		print("{:0>2}".format(num), end=", ")
print()
