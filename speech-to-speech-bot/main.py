import tkinter as tk 
from tkinter import messagebox 
from src.speech_recognition import recognize_speech
from src.response_generator import generate_response
from src.text_to_speech import speak_text
from src.utils import log_info, log_error

def on_speak_button_click():
    try:
        log_info("Initializing Speech-to-Speech Bot...")
        status_label.config(text="Listening...")
        
        
        user_input = recognize_speech()
        if not user_input:
            status_label.config(text="No input detected. Please try again.")
            log_error("No input detected during speech recognition.")
            return
        
        
        user_input_label.config(text=f"User Input: {user_input}")
        
        
        response = generate_response(user_input)
        if not response:
            response = "I couldn't understand that. Could you please try again?"
        response_label.config(text=f"Bot Response: {response}")
        
        
        speak_text(response)

    except Exception as e:
        log_error(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="Error occurred, please try again.")


window = tk.Tk()
window.title("Speech-to-Speech Bot")
window.geometry("500x400")
window.configure(bg="#F0F8FF")  


frame = tk.Frame(window, bg="#F0F8FF")
frame.pack(pady=20)


title_label = tk.Label(frame, text="Speech-to-Speech Bot", font=("Helvetica", 18, "bold"), bg="#F0F8FF", fg="#333333")
title_label.grid(row=0, column=0, columnspan=2, pady=10)


user_input_label = tk.Label(frame, text="User Input: ", font=("Helvetica", 12), bg="#F0F8FF", fg="#333333")
user_input_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)


response_label = tk.Label(frame, text="Bot Response: ", font=("Helvetica", 12), bg="#F0F8FF", fg="#333333")
response_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)


status_label = tk.Label(frame, text="Press the button to start speaking", font=("Helvetica", 12), bg="#F0F8FF", fg="#333333")
status_label.grid(row=3, column=0, columnspan=2, pady=20)


speak_button = tk.Button(frame, text="Speak", font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="flat", width=20,
                          activebackground="#45a049", command=on_speak_button_click)
speak_button.grid(row=4, column=0, columnspan=2, pady=20)


def on_enter(e):
    speak_button['background'] = '#45a049'

def on_leave(e):
    speak_button['background'] = '#4CAF50'

speak_button.bind("<Enter>", on_enter)
speak_button.bind("<Leave>", on_leave)


window.mainloop()
