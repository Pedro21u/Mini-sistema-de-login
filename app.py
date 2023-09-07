import customtkinter 

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
        

janela = customtkinter.CTk()
janela.title('Sistema de login')
janela.geometry('300x250')

#Botao clique
def clique():
    print('Fazer login')
    

#Texto

texto = customtkinter.CTkLabel(janela, text='Fazer login')
texto.pack(padx=10, pady=10)

#Senha 

email = customtkinter.CTkEntry(janela, placeholder_text='Seu email')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show="*")
senha.pack(padx=10, pady=10)


checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Login',command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()

