from SQLighter import SQLighter
def check_number_and_return_result(num):
	db = SQLighter("helpr_test.db")
	result = db.select_text_result(num)
	db.close()
	if result != None:
		return result
	else:
		return "We do not support this number. Try another command or a valid number from the keyboard"