import json
users_data={}
with open('users.json', 'w') as f:
    json.dump(users_data, f)

def reg(login, password):
    with open('users.json', 'r') as f:
        users=json.load(f)

    if login not in users:
        users[login]=password
        with open('users.json','w') as f:
            json.dump(users, f)
        print('пользователь зарегистрирован')
    else:
        print('логин занят')

def log(user_login, user_password):
    with open('users.json','r') as f:
        users=json.load(f)

    if user_login in users and users[user_login]==user_password:
        print('успешный вход')
        return True
    else:
        print('неверный логин или пароль')
        return False


while True:
    action = input("\n1-Регистрация\n2-Вход\n3-Выход\n> ")

    if action == '3': break

    if action in ('1', '2'):
        input_login = input("Логин: ")
        input_password = input("Пароль: ")

        if action =='1':
            reg(input_login, input_password)
        else:
            log(input_login,input_password)
    else:
        print("Некорректный ввод")