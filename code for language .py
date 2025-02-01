import tkinter as tk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.title("Language Translator Application")
        self.geometry("600x400")
        self.resizable(False, False)

        # Translator instance
        self.translator = Translator()

        # Title label
        self.title_label = tk.Label(self, text="Language Translator", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Text input field
        self.input_label = tk.Label(self, text="Enter text to translate:", font=("Helvetica", 12))
        self.input_label.pack(pady=5)

        self.input_text = tk.Entry(self, width=50, font=("Helvetica", 12))
        self.input_text.pack(pady=5)

        # From Language Dropdown (Select language for translation)
        self.from_language_label = tk.Label(self, text="From Language", font=("Helvetica", 12))
        self.from_language_label.pack(pady=5)

        self.from_lang_var = tk.StringVar(self)
        self.from_lang_var.set("en")  # Default language set to English
        self.from_language_menu = tk.OptionMenu(self, self.from_lang_var, *LANGUAGES.values())
        self.from_language_menu.pack(pady=5)

        # To Language Dropdown (Select language for translation)
        self.to_language_label = tk.Label(self, text="To Language", font=("Helvetica", 12))
        self.to_language_label.pack(pady=5)

        self.to_lang_var = tk.StringVar(self)
        self.to_lang_var.set("es")  # Default language set to Spanish
        self.to_language_menu = tk.OptionMenu(self, self.to_lang_var, *LANGUAGES.values())
        self.to_language_menu.pack(pady=5)

        # Translate Button
        self.translate_button = tk.Button(self, text="Translate", font=("Helvetica", 12), command=self.translate)
        self.translate_button.pack(pady=20)

        # Output translation label
        self.output_label = tk.Label(self, text="Translation:", font=("Helvetica", 12))
        self.output_label.pack(pady=5)

        self.output_text = tk.Label(self, text="", font=("Helvetica", 12), width=50, height=4, relief="sunken")
        self.output_text.pack(pady=5)

    def translate(self):
        try:
            # Get the input text and languages selected
            input_text = self.input_text.get()
            from_lang = self.from_lang_var.get()
            to_lang = self.to_lang_var.get()

            # Perform translation
            translation = self.translator.translate(input_text, src=from_lang, dest=to_lang)

            # Display translated text
            self.output_text.config(text=translation.text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during translation: {str(e)}")

if __name__ == "__main__":
    app = LanguageTranslatorApp()
    app.mainloop()
