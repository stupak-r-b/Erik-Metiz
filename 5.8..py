users = []

for user in users:
	if users:
		if user == "admin":
			print("Hello andmin, would you like to see a status report?")
		else:
			print(f"Hello {user}, thank you for logging in again")
	else:
		print("We need to find some users!")