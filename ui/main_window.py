import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Agencia de Viajes - Sistema")
        self.geometry("800x600")

        # Encabezado
        self.label = ctk.CTkLabel(self, text="Sistema Agencia de Viajes", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Botones de navegación
        self.btn_clientes = ctk.CTkButton(self, text="Clientes", width=200, command=lambda: print("Clientes presionado"))
        self.btn_clientes.pack(pady=10)

        self.btn_tours = ctk.CTkButton(self, text="Tours", width=200, command=lambda: print("Tours presionado"))
        self.btn_tours.pack(pady=10)

        self.btn_reportes = ctk.CTkButton(self, text="Reportes", width=200, command=lambda: print("Reportes presionado"))
        self.btn_reportes.pack(pady=10)

        # Pie de página
        self.label_footer = ctk.CTkLabel(self, text="© Agencia Viajes 2025", font=("Arial", 12))
        self.label_footer.pack(side="bottom", pady=10)
