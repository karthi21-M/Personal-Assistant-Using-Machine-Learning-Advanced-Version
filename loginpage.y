# Login Page Function
def login_page():
    login_window = tk.Tk()
    login_window.title("Login Page")

    login_window.geometry("400x300")
    login_window.configure(bg="#F0F0F0")

    def validate_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            login_window.destroy()  # Close the login window
            main()  # Proceed to main assistant window
        else:
            error_label.config(text="Invalid username or password.", foreground="red")

    username_label = ttk.Label(login_window, text="Username:", font=("Arial", 14))
    username_label.pack(pady=10)
    username_entry = ttk.Entry(login_window, font=("Arial", 14))
    username_entry.pack(pady=10)

    password_label = ttk.Label(login_window, text="Password:", font=("Arial", 14))
    password_label.pack(pady=10)
    password_entry = ttk.Entry(login_window, show="*", font=("Arial", 14))
    password_entry.pack(pady=10)

    login_button = ttk.Button(login_window, text="Login", command=validate_login)
    login_button.pack(pady=20)

    error_label = ttk.Label(login_window, text="", font=("Arial", 12))
    error_label.pack()

    login_window.mainloop()
