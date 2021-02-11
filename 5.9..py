current_users = ["Alexander", "Roman", "Vlad", "Viktoriia", "Pavel"]

new_users = ["Matvey", "Garik", "Barbos", "Jessey", "Alexander"]

for name in new_users:
	if name in current_users:
		print("\nДанное имя было использовано ранее. Пожалуйста выберите другое имя пользователя.")
	else:
		print("\nДанное имя пользователя свободно! Вы можете продолжить регистрацию.")