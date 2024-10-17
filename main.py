import tkinter as tk
import time


class RememberNumberGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Remember number")
        self.geometry("500x500+500+150")

        self.difficulty_var = tk.StringVar(self)
        self.difficulty_var.set("Mid")

        self.frame = tk.Frame(self, width=500, height=600, background="grey")

        self.label = tk.Label(self.frame, text="Welcome to remember the number game!", font=("Helvetica", 15),
                              bg="grey")
        self.button = tk.Button(self.frame, text="Start!", command=self.select_difficulty,
                                background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

        self.frame.place(relx=0.5, rely=0.4, anchor="center")
        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.button.place(relx=0.5, rely=0.5, anchor="center", width=100, height=50)

    def select_difficulty(self):
        self.frame.place_forget()
        difficulty_frame = tk.Frame(self, width=500, height=600, background="grey")

        difficulty_label = tk.Label(difficulty_frame, text="Choose a difficulty", font=("Helvetica", 15),
                                    background="grey")

        difficulty_option = tk.OptionMenu(difficulty_frame, self.difficulty_var,
                                          "Easy", "Mid", "Hard")

        difficulty_button = tk.Button(difficulty_frame, text="Ready", command=self.start_game,
                                      background="#000000", font=("Helvetica", 15, "bold"), foreground="#FFFFFF")

        difficulty_label.place(relx=0.5, rely=0.4, anchor="center")
        difficulty_option.place(relx=0.5, rely=0.5, anchor="center")
        difficulty_frame.place(relx=0.5, rely=0.4, anchor="center")
        difficulty_button.place(relx=0.5, rely=0.6, anchor="center")

    def start_game(self):
        if self.difficulty_var == "Easy":
            time_limit = 30
        elif self.difficulty_var == "Mid":
            time_limit = 15
        else:
            time_limit = 5

        start_time = time.time()



if __name__ == "__main__":
    app = RememberNumberGame()
    app.mainloop()
