#!/usr/bin/python3
def magic_string():
	count = 0 
	def magic_print(): return ("BestSchool" + (count * ", BestSchool"))
	count += 1
	return magic_print