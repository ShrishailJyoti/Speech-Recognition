import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="Listening... Say something!")
        root.update()  # Forces Tkinter to update the label text immediately
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        status_label.config(
            text="Recognizing...", fg="blue", font=("Arial", 12, "bold")
        )
        root.update()

    try:
        text = recognizer.recognize_google(audio_data)
        result_label.config(text=f"Recognized Text:\n{text}")

    except sr.UnknownValueError:
        messagebox.showerror(
            "Recognition Error", "Could not understand audio"
        )

    except sr.RequestError as e:
        messagebox.showerror(
            "API Error", f"Could not request results; {e}"
        )


# Setting up the GUI
root = tk.Tk()
root.title("Speech Recognition App")
root.geometry("300x300")

# Heading label
heading_label = tk.Label(
    root,
    text="Speech Recognition",
    bg="orange",
    font=("sans", 18, "bold"),
    fg="yellow",
)
heading_label.pack(pady=10, fill="x")

# Status label
status_label = tk.Label(root, text="Click below to start", font=("Arial", 12))
status_label.pack(pady=10)

# Result label
result_label = tk.Label(
    root, text="", font=("Arial", 12), wraplength=450
)  # Note: wraplength 450 is larger than geometry width (300)
result_label.pack(pady=10)

# Recognize button
recognize_button = tk.Button(
    root,
    text="Start Listening",
    fg="blue",
    bg="yellow",
    font=("sans", 14, "bold"),
    command=recognize_speech,
)
recognize_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
