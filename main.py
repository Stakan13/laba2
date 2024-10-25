import tkinter as tk
import time
import random


class RememberNumberGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Remember number")
        self.geometry("500x500+500+150")

        self.nums = []
        self.result_nums = []
        self.time_left = 0
        self.start_time = 0

        self.result_message = tk.StringVar(self)

        self.difficulty_var = tk.StringVar(self)
        self.difficulty_var.set("Mid")

        self.option = None

        self.frame = tk.Frame(self, width=500, height=600, background="grey")
        self.entry = None

        self.label = tk.Label(self.frame, text="Welcome to remember the number game!", font=("Helvetica", 15),
                              bg="grey")
        self.button = tk.Button(self.frame, text="Start!", command=self.select_difficulty,
                                background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.button.place(relx=0.5, rely=0.5, anchor="center", width=100, height=50)

    def select_difficulty(self):
        self.frame.place_forget()
        self.frame = tk.Frame(self, width=500, height=600, background="grey")

        self.label = tk.Label(self.frame, text="Choose a difficulty", font=("Helvetica", 15),
                              background="grey")

        self.option = tk.OptionMenu(self.frame, self.difficulty_var,
                                    "Easy", "Mid", "Hard")

        self.button = tk.Button(self.frame, text="Ready", command=self.start_game,
                                background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.option.place(relx=0.5, rely=0.5, anchor="center")
        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.button.place(relx=0.5, rely=0.6, anchor="center")

    def start_game(self):
        self.frame.place_forget()
        if self.difficulty_var.get() == "Easy":
            time_limit = 30
        elif self.difficulty_var.get() == "Mid":
            time_limit = 15
        else:
            time_limit = 5

        self.start_time = time.time()
        self.time_left = time_limit

        self.frame = tk.Frame(self, width=500, height=600, background="grey")

        self.label = tk.Label(self.frame, text=f"Remember the numbers in {time_limit} seconds", font=("Helvetica", 15),
                              background="grey")

        for x in range(4, 7):
            for y in range(4, 7):
                num = tk.StringVar(value=str(random.randint(10, 99)))
                self.nums.append(num)

                numb_label = tk.Label(self.frame, textvariable=num, font=("Helvetica", 15))
                numb_label.place(relx=x/10, rely=y/10)

        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.2, anchor="n")

        self.update_timer()

    def update_timer(self):
        right_time = time.time() - self.start_time
        remaining_time = max(0, int(self.time_left - right_time))

        minutes, secs = divmod(remaining_time, 60)
        self.label.config(text=f"Remember the numbers in {int(minutes):02d}:{secs:05.2f} seconds")

        if remaining_time > 0:
            self.after(100, self.update_timer)
        else:
            self.create_entry_fields()

    def create_entry_fields(self):
        self.frame.place_forget()

        self.frame = tk.Frame(self, width=500, height=600, background="grey")

        self.label = tk.Label(self.frame, text=f"Enter the numbers separated by spaces"
                                               f"\n(from left to right, top to bottom)",
                              font=("Helvetica", 15),
                              background="grey")
        self.button = tk.Button(self.frame, text="Ok", command=self.current_numb,
                                background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

        self.entry = tk.Entry(self.frame)
        self.result_nums = self.entry.get().split()

        self.button.place(relx=0.53, rely=0.6, anchor="center")
        self.entry.place(rely=0.4, relx=0.4)
        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.53, rely=0.2, anchor="n")

    def compare_arrays(self):
        if self.result_nums == self.nums:
            self.result_message.set("You win")
        else:
            self.result_message.set("You lose")

    def current_numb(self):
        self.frame.place_forget()
        try:
            for elem in self.result_nums:
                if not elem.isdigit():
                    raise ValueError
                elif 2 > len(elem) > 2:
                    raise ValueError
                else:
                    self.compare_arrays()
        except ValueError:
            self.frame.place_forget()

            self.label = tk.Label(self.frame, text="Enter correct numbers!!",
                                  font=("Helvetica", 15),
                                  background="grey")

            self.button = tk.Button(self.frame, text="Ok", command=self.create_entry_fields,
                                    background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

            self.button.place(rely=0.4, relx=0.4)
            self.frame.place(relx=0.5, rely=0.4, anchor="center")
            self.label.place(relx=0.53, rely=0.2, anchor="n")


if __name__ == "__main__":
    app = RememberNumberGame()
    app.mainloop()
