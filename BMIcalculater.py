import tkinter

window = tkinter.Tk()
window.title("BMI calculater")
window.minsize(width=800, height=450)

my_label = tkinter.Label(text="Enter your weight", fg="black", font=("Arial", 13, "italic"))
# my_label.config(to change some of features)
my_label.pack()

my_weight = tkinter.Entry(width=20)
my_weight.pack()

my_label_2 = tkinter.Label(text="Enter your height(cm)", fg="black", font=("Arial", 13, "italic"))
my_label_2.pack()

my_height = tkinter.Entry(width=20)
my_height.pack()

result_label = tkinter.Label(text="", fg="black", font=("Arial", 13, "italic"))
result_label.pack(side="bottom")

usage_num = 0


def click_button():
    heigt = my_height.get()
    weight = my_weight.get()
    try:
        x = float(my_weight.get())
        y = float(my_height.get()) / 100
    except ValueError:
        result_label.config(text="please enter numbers!")
    BMI = x / (y * y)
    if BMI <= 18.4:
        result_label.config(text="Your weight is: underweight!")
    elif 18.4 < BMI <= 24.9:
        result_label.config(text="Your weight is: normal!")
    elif 24.9 < BMI < 40:
        result_label.config(text="Your weight is: overweight!")
    else:
        result_label.config("Your weight is: Obese!")


my_button = tkinter.Button(text="Do not click here", comman=click_button, width=20, height=3)
my_button.pack()

window.mainloop()