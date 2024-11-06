import tkinter as tk
from tkinter import messagebox

from main import WebAutomation


class App:
    def __init__(self, root):
        self.web_automation = None
        self.root = root
        self.root.title("Web Automation GUI")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.entry_full_name = tk.Entry(self.form_frame)
        self.entry_full_name.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address").grid(row=2, column=0, sticky="w")
        self.entry_current_address = tk.Entry(self.form_frame)
        self.entry_current_address.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address").grid(row=3, column=0, sticky="w")
        self.entry_perm_address = tk.Entry(self.form_frame)
        self.entry_perm_address.grid(row=3, column=1, sticky="ew")

        # Form button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Download", command=self.download).grid(row=0, column=2, padx=5)

    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        full_name = self.entry_full_name.get()
        email = self.entry_email.get()
        current_address = self.entry_current_address.get()
        perm_address = self.entry_perm_address.get()

        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(full_name, email, current_address, perm_address)

    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Browser Closed", "Submitted Successfully")

    def download(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.download()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
