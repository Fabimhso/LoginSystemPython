import customtkinter as ctk

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Login System')
app.geometry('300x300')

# Titulo User || User Label
label_user = ctk.CTkLabel(app, text='User')
label_user.pack(pady=10)

# Input
input_user = ctk.CTkEntry(app, placeholder_text='Type Your User')
input_user.pack()

# Titulo Senha || Password Label
label_pass = ctk.CTkLabel(app, text='Password')
label_pass.pack(pady=10)

# Input
input_pass = ctk.CTkEntry(app, placeholder_text='Type Your Password')
input_pass.pack()


# Para Iniciar a Aplicacao || To Start the Application
app.mainloop()
