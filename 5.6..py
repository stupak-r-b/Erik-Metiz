users = ["big_vlad", "bobo1993", "tsapko_man", "batya", "mamkin_programmist", "admin"]

for user in users:
	if user == "admin":
		print("Hello andmin, would you like to see a status report?")
	else:
		print(f"Hello {user}, thank you for logging in again")