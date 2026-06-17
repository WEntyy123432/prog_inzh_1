import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import os

FILE_NAME = "events.json"

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Календарь событий")
        self.root.geometry("500x500")
        self.events = self.load_events()
        tk.Label(
            root,

            text="Календарь событий",

            font=("Arial", 16, "bold")

        ).pack(pady=10)

        self.calendar = Calendar(

            root,

            selectmode="day",

            date_pattern="yyyy-mm-dd"
        )
        self.calendar.pack(pady=10)
        tk.Label(root, text="Введите событие:").pack()
        self.event_entry = tk.Entry(root, width=40)
        self.event_entry.pack(pady=5)
        tk.Button(
            root,

            text="Сохранить событие",

            command=self.save_event

        ).pack(pady=5)

        tk.Button(

            root,

            text="Показать события",

            command=self.show_events

        ).pack(pady=5)

        self.events_text = tk.Text(root, height=12, width=55)

        self.events_text.pack(pady=10)

    def load_events(self):

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r", encoding="utf-8") as file:

                return json.load(file)

        return {}

    def save_events_to_file(self):

        with open(FILE_NAME, "w", encoding="utf-8") as file:

            json.dump(

                self.events,

                file,

                ensure_ascii=False,

                indent=4

            )

    def save_event(self):

        date = self.calendar.get_date()

        event = self.event_entry.get().strip()

        if not event:

            messagebox.showwarning(

                "Ошибка",

                "Введите описание события!"

            )

            return

        if date not in self.events:

            self.events[date] = []

        self.events[date].append(event)

        self.save_events_to_file()

        self.event_entry.delete(0, tk.END)

        messagebox.showinfo(

            "Успех",

            f"Событие добавлено на {date}"

        )

    def show_events(self):

        date = self.calendar.get_date()

        self.events_text.delete(1.0, tk.END)

        if date in self.events:

            self.events_text.insert(

                tk.END,

                f"События на {date}:\n\n"

            )

            for number, event in enumerate(

                    self.events[date], start=1):

                self.events_text.insert(

                    tk.END,

                    f"{number}. {event}\n"

                )

        else:

            self.events_text.insert(

                tk.END,

                f"На {date} событий нет."

            )

if __name__ == "__main__":

    root = tk.Tk()

    app = CalendarApp(root)

    root.mainloop()