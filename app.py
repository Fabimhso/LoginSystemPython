import customtkinter as ctk

ctk.set_appearance_mode('dark')


def validate_login():
    user = input_pass.get()
    password = input_pass.get()

    # Verification: User = FabianoDev | Password: 7777
    if user == 'fabiano' and password == '777777':
        feedback_login.configure(
            text='Successfully Logged', text_color='green')
    else:
        feedback_login.configure(text='Incorrect Login', text_color='red')


app = ctk.CTk()
app.title('Login System')
app.geometry('300x300')

# Titulo User || User Label
label_user = ctk.CTkLabel(app, text='User')
label_user.pack(pady=10)

# Input User
input_user = ctk.CTkEntry(app, placeholder_text='Type Your User')
input_user.pack()

# Titulo Senha || Password Label
label_pass = ctk.CTkLabel(app, text='Password')
label_pass.pack(pady=10)

# Input Password
input_pass = ctk.CTkEntry(app, placeholder_text='Type Your Password', show='*')
input_pass.pack()

# Botao || Button
login_button = ctk.CTkButton(app, text='Login', command=validate_login)
login_button.pack(pady=10)
feedback_login = ctk.CTkLabel(app, text='')
feedback_login.pack(pady=10)

# Para Iniciar a Aplicacao || To Start the Application
app.mainloop()
