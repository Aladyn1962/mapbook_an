users: list = [
    {"name": "Bernard", "location": "Ełk", "posts": 400},

]
print(users)


def add_user(users_data: list) -> None;


user_name = input('podaj imię nowego urzytkownika: ')
user_location = input('podaj lokalizację nowego znajomego: ')
user_posts = int(input('podaj liczbę postów: '))
users_data.append({"name": user_name, "location": user_location, "posts": user_posts})

add_user(users)

print(users)
