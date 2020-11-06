

# Rule for changing a lead status
def is_valid_status_change(old_status, new_status):
	if (old_status.id == 1 and new_status.id == 2) or (old_status.id == 2 and new_status.id == 3):
		return True
	return False

def need_new_customer(new_status):
	if(new_status.id == 2): return True
	return False

def need_to_book_meeting(new_status):
	if(new_status.id == 3): return True
	return False
