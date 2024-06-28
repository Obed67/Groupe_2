import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
from customtkinter import *
import torch
from diffusers import StableDiffusionPipeline
import threading

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur d'images")
        self.root.geometry("800x450")
        self.pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
        self.is_generating = False
        self.create_widgets()

    def create_widgets(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.rowconfigure(0, weight=1)

        self.prompt_entry = CTkEntry(self.root, placeholder_text="Entrez la description ici ...", width=300, height=50, corner_radius=32, font=("Helvetica", 14), border_width=None, border_color="#4e8dda")
        self.prompt_entry.grid(row=0, column=0, padx=(40, 10), pady=(50, 10), sticky="new")

        self.generate_button = CTkButton(self.root, text="Générer", command=self.generate_image, font=("Helvetica", 14), corner_radius=32, fg_color="#4e8dda", width=150, height=50)
        self.generate_button.grid(row=0, column=1, padx=(10, 40), pady=(50, 10), sticky="nw")

        self.image_frame = CTkFrame(self.root, bg_color="transparent")
        self.image_frame.place(relx=0.1, rely=0.40, relwidth=0.8, relheight=0.4)

        self.back_button = CTkButton(self.root, text="Retour", command=self.root.quit, corner_radius=32, fg_color="#4e8dda", width=150, height=50)
        self.back_button.grid(row=0, column=1, padx=(10, 40), pady=10, sticky="sew")

        # Charger le GIF comme image animée avec PIL
        gif_path = "1490.gif"
        self.gif = Image.open(gif_path)
        self.gif_frames = []
        try:
            while True:
                self.gif_frames.append(self.gif.copy())
                self.gif.seek(len(self.gif_frames))  # Aller au prochain frame
        except EOFError:
            pass

        # Créer les images tkinter pour chaque frame du GIF
        self.gif_tk_frames = [ImageTk.PhotoImage(frame) for frame in self.gif_frames]

        # Créer un label pour afficher le GIF
        self.spinner_label = Label(self.root)

    def update_gif(self, frame_num):
        if self.is_generating:
            frame = self.gif_tk_frames[frame_num]
            self.spinner_label.configure(image=frame)
            self.root.after(60, self.update_gif, (frame_num + 1) % len(self.gif_tk_frames))

    def generate_image(self):
        prompt = self.prompt_entry.get()
        if not prompt:
            return

        self.is_generating = True
        self.image_frame.place(relx=0.1, rely=0.40, relwidth=0.8, relheight=0.4)
        self.spinner_label.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.15)
        self.update_gif(0)

        thread = threading.Thread(target=self.generate_image_from_prompt, args=(prompt,))
        thread.start()

    def generate_image_from_prompt(self, prompt):
        try:
            # Génération de l'image avec le modèle
            image = self.pipe(prompt).images[0]
            self.display_generated_image(image)
        except Exception as e:
            print(f"Erreur lors de la génération d'image : {e}")
        finally:
            self.is_generating = False
            self.spinner_label.place_forget()

    def display_generated_image(self, image):
        photo = ImageTk.PhotoImage(image)

        # Effacer le cadre précédent s'il y a une image affichée
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        label = tk.Label(self.image_frame, image=photo)
        label.image = photo  # Garder une référence pour éviter la collecte des ordures
        label.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
