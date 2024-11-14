import tkinter as tk

def change_color(color):
    if color == "red":  #если нажата кнопка "красный"
        red_button.config(bg="#ff0000")  #меняем цвет кнопки на красный
        yellow_button.config(bg="#f0f0f0")  #сбрасываем цвет кнопки "жёлтый"
        green_button.config(bg="#f0f0f0")  #сбрасываем цвет кнопки "зелёный"
        label.config(text="Стой – красный свет!")  #меняем текст метки
    elif color == "yellow": 
        red_button.config(bg="#f0f0f0")  
        yellow_button.config(bg="#ffff00")  
        green_button.config(bg="#f0f0f0")  
        label.config(text="Жди – жёлтый свет!")  
    elif color == "green":  
        red_button.config(bg="#f0f0f0") 
        yellow_button.config(bg="#f0f0f0") 
        green_button.config(bg="#00ff00") 
        label.config(text="Иди – зелёный свет!") 

#создаем главное окно
window = tk.Tk()
window.title("Светофор")

#устанавливаем начальный цвет фона
window.config(bg="#f0f0f0")

#создаем метку
label = tk.Label(window, text="", font=("Arial", 16), bg="#f0f0f0")
label.pack(pady=20)

#создаем кнопки
red_button = tk.Button(window, text="Красный", command=lambda: change_color("red"), bg="#f0f0f0")
yellow_button = tk.Button(window, text="Жёлтый", command=lambda: change_color("yellow"), bg="#f0f0f0")
green_button = tk.Button(window, text="Зелёный", command=lambda: change_color("green"), bg="#f0f0f0")

#размещаем кнопки на окне
red_button.pack(pady=5)
yellow_button.pack(pady=5)
green_button.pack(pady=5)

#запускаем главный цикл приложения
window.mainloop()
