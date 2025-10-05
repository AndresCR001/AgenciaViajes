import customtkinter as ctk
from ui.main_window import MainWindow

if __name__ == "__main__":
    ctk.set_appearance_mode("system")  # "dark" o "light"
    ctk.set_default_color_theme("blue")

    app = MainWindow()
    app.mainloop()
