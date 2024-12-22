import requests as r
from getpass import getpass
import numpy as np

if __name__ == "__main__":
      while True:
            print(f"==============МЕНЮ==============\n"
                  f"1. Вывод репозиторий организации\n"
                  f"2. Вывод репозиторий пользователя\n"
                  f"3. Вывод репозитория пользователя\n"
                  f"4. Создание репозитория\n"
                  f"5. Удаление репозитория\n")
            inp = int(input("Выберите действие: "))

            with open("token.txt", "r", encoding="utf-8") as file:
                  token = file.read()
            user = "Nick271618"
            repo = "laba6-API"
            org = "freeCodeCamp"

            if inp == 1:
                  check_repos = r.get(f"https://api.github.com/orgs/{org}/repos").json()
                  for obj in check_repos:
                        name = obj['name']
                        id = obj['id']
                        print(f"Репозитория: {name}\nid: {id}")

            elif inp == 2:
                  check_repos_user = r.get(f"https://api.github.com/users/{user}/repos").json()
                  for obj in check_repos_user:
                        name = obj['name']
                        id = obj['id']
                        print(f"Репозитория: {name}\nid: {id}")
                  print()

            elif inp == 3:
                  check_repo = r.get(f"https://api.github.com/repos/{user}/{repo}", auth=(user, token)).json()
                  print(f"Репозитория: {check_repo['name']} и id: {check_repo['id']}\n")

            elif inp == 4:
                  descr = "Создание репозитория через python"
                  data = {
                        "name": repo,
                        "description": descr,
                  }
                  create_repo = r.post("https://api.github.com/user/repos", auth=(user, token), json=data)
                  print(create_repo.status_code)
                  if create_repo.status_code == 201:
                        print("Репозиторий успешно создан!\n")
                  else:
                        print("Не получилось создать репозиторий!\n")

            elif inp == 5:
                  delete_repo = r.delete(f"https://api.github.com/repos/{user}/{repo}", auth=(user, token))
                  if delete_repo.status_code == 204:
                        print("Удаление прошло успешно!\n")
                  else:
                        print("Репозиторий не удалён!\n")

            else:
                  print("Некорректный ввод. Попробуйте ещё раз")
