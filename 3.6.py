# list with some different people
some_people = ["me", "mother", "grandmother", "Alex", "some_one_else"]
print(some_people)

del some_people[4]
some_people.append("mr.Peterson")

for people in some_people:
	print(f"Дорогой(гая) {people}, приглашаю тебя на мой день рождения. С Ув. Роман!")

print("\n\nУв. гости! С большим удовольствием сообшаю, что количество заявленных гостей увеличится на три.")


some_people.insert(0, "Alexander Makedonsky")
some_people.insert(4, "Ivanushka")
some_people.append("Jugishvili")

for people in some_people:
	print(f"Дорогой(гая) {people}, приглашаю тебя на мой день рождения. С Ув. Роман!")


print("\n\nУв. потенциальные гости! Хочу сообщить вам о том, что количество мест будет ограничено до двух. Приглашенным гостям будет заново \
	   высланы приглашения")


print(f"\nПриглашение отзывается у {some_people.pop(0)}")
print(f"\nПриглашение отзывается у {some_people.pop(3)}")
print(f"\nПриглашение отзывается у {some_people.pop(4)}")
print(f"\nПриглашение отзывается у {some_people.pop(4)}")

for people in some_people:
	print(f"\nДорогой(гая) {people}, всё так же приглашаю тебя на мой день рождения. С Ув. Роман!")
