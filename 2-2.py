import tkinter as tk
import random
import json
from tkinter import messagebox
from PIL import Image, ImageTk


#подсчет статистики
statistics = {
    "user_wins": 0,
    "computer_wins": 0,
    "ties": 0,
    "user_choices": {"камень": 0, "ножницы": 0, "бумага": 0},
    "computer_choices": {"камень": 0, "ножницы": 0, "бумага": 0},
    "total_games": 0
}

#функция для сохранения статистики в файл
def save_statistics():
    with open("statistics.json", "w") as file:
        json.dump(statistics, file)
    messagebox.showinfo("Статистика сохранена", "Статистика была сохранена в файл statistics.json")

#функция для просмотра статистики
def view_statistics():
    stats_text = (
        f"Победы пользователя: {statistics['user_wins']}\n"
        f"Победы компьютера: {statistics['computer_wins']}\n"
        f"Ничьи: {statistics['ties']}\n"
        f"Выборы пользователя: {statistics['user_choices']}\n"
        f"Выборы компьютера: {statistics['computer_choices']}\n"
        f"Всего игр: {statistics['total_games']}"
    )
    messagebox.showinfo("Статистика", stats_text)

#функция для сброса игры
def reset_game():
    global statistics
    statistics = {
        "user_wins": 0,
        "computer_wins": 0,
        "ties": 0,
        "user_choices": {"камень": 0, "ножницы": 0, "бумага": 0},
        "computer_choices": {"камень": 0, "ножницы": 0, "бумага": 0},
        "total_games": 0
    }
    user_choice_label.config(text="Вы выбрали: ")
    computer_choice_label.config(text="Компьютер выбрал: ")
    score_label.config(text="Счет: 0 - 0")

#функция для выполнения хода
def make_move(user_choice):
    global statistics
    statistics["user_choices"][user_choice] += 1
    statistics["total_games"] += 1

    #логика компьютера после третьего хода
    if statistics["total_games"] > 2:
        comp_choice = smart_computer_choice()
    else:
        comp_choice = random.choice(["камень", "ножницы", "бумага"])

    statistics["computer_choices"][comp_choice] += 1

    #обновляем интерфейс
    user_choice_label.config(text=f"Вы выбрали: {user_choice}")
    computer_choice_label.config(text=f"Компьютер выбрал: {comp_choice}")

    #определяем победителя
    if user_choice == comp_choice:
        result = "tie"
        statistics["ties"] += 1
    elif (user_choice == "камень" and comp_choice == "ножницы") or \
         (user_choice == "ножницы" and comp_choice == "бумага") or \
         (user_choice == "бумага" and comp_choice == "камень"):
        result = "user"
        statistics["user_wins"] += 1
    else:
        result = "computer"
        statistics["computer_wins"] += 1

    #обновляем счет
    score_label.config(text=f"Счет: {statistics['user_wins']} - {statistics['computer_wins']}")

#простая логика для выбора компьютера после третьего хода
def smart_computer_choice():
    user_most_chosen = max(statistics["user_choices"], key=statistics["user_choices"].get)
    if user_most_chosen == "камень":
        return "бумага"
    elif user_most_chosen == "ножницы":
        return "камень"
    else:
        return "ножницы"

#функция для выхода из игры
def exit_game():
    root.destroy()  #закрыть окно

#создание главного окна
root = tk.Tk()
root.title("Камень, ножницы, бумага")
root.geometry("628x280")
background_image = ImageTk.PhotoImage(file="D8B8F1.jpeg")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  #размеры на все окно

#левая панель для кнопок управления
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

start_button = tk.Button(left_frame, text="Начать игру", command=reset_game, width=20, height=2)
start_button.grid(row=0, column=0, padx=5, pady=5)

save_button = tk.Button(left_frame, text="Сохранить статистику", command=save_statistics, width=20, height=2)
save_button.grid(row=1, column=0, padx=5, pady=5)

view_button = tk.Button(left_frame, text="Просмотр статистики", command=view_statistics, width=20, height=2)
view_button.grid(row=2, column=0, padx=5, pady=5)

exit_button = tk.Button(left_frame, text="Выход из игры", command=exit_game, width=20, height=2)
exit_button.grid(row=3, column=0, padx=5, pady=5)

#правая панель для игры и отображения результатов
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10)
score_label = tk.Label(right_frame, text="Счет: 0 - 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3)

computer_choice_label = tk.Label(right_frame, text="Компьютер выбрал:", font=("Arial", 12))
computer_choice_label.grid(row=1, column=0, columnspan=3)

user_choice_label = tk.Label(right_frame, text="Вы выбрали:", font=("Arial", 12))
user_choice_label.grid(row=2, column=0, columnspan=3)

#кнопки для выбора пользователя

image_path1 = "rock.jpg"  
image = Image.open(image_path1)
photo1 = ImageTk.PhotoImage(image)

image_path2 = "scissors.jpg" 
image = Image.open(image_path2)
photo2 = ImageTk.PhotoImage(image)

image_path3 = "paper.jpg"  
image = Image.open(image_path3)
photo3 = ImageTk.PhotoImage(image)

rock_button = tk.Button(right_frame, image=photo1, command=lambda: make_move("камень"), width=10, height=2)
rock_button.grid(row=3, column=0, padx=5, pady=5)
rock_button.config(width=100, height=100)


scissors_button = tk.Button(right_frame, image=photo2, command=lambda: make_move("ножницы"), width=10, height=2)
scissors_button.grid(row=3, column=1, padx=5, pady=5)
scissors_button.config(width=100, height=100)

paper_button = tk.Button(right_frame, image=photo3, command=lambda: make_move("бумага"), width=10, height=2)
paper_button.grid(row=3, column=2, padx=5, pady=5)
paper_button.config(width=100, height=100)


#запуск приложения
root.mainloop()
