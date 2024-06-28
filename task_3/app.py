import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import threading
from diffusers import StableDiffusionPipeline
from diffusers import DiffusionPipeline

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Copilot")
        self['bg'] = 'purple'
        self.resizable(height=False, width=False)

        # Page du logoss
        self.logo_page = LogoPage(self)
        self.logo_page.pack(fill="both", expand=True)

        self.after(5000, self.show_page1)

    def show_page1(self):
        self.logo_page.pack_forget()
        self.page1 = Page1(self)
        self.page1.pack(fill="both", expand=True)

    def show_page2(self):
        self.page1.pack_forget()
        self.page2 = Page2(self)
        self.page2.pack(fill="both", expand=True)

class LogoPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.parent = parent

        # Afficher un logo ou un texte de bienvenue
        self.photo = PhotoImage(file='gg1.png')
        self.label = Label(self, image=self.photo)
        self.label.pack(pady=20)

class Page1(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.parent = parent

        image = Image.open('gg2.png')
        image = image.resize((300, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.label = Label(self, image=self.photo, bg="white")
        self.label.pack(pady=50)

        # Label d'instruction
        self.label = Label(self, text="Let's Generate", font=("Poppins", 15, "bold"), fg="black", bg="white")
        self.label.pack(pady=100)

        # Bouton Generate
        self.btn_generate_image = ImageTk.PhotoImage(file="generate1.png")
        self.btn_generate = Button(self, image=self.btn_generate_image, command=parent.show_page2, borderwidth=0, highlightthickness=0, fg="white")
        self.btn_generate.place(x=100, y=350)

        # Bouton Quitter
        self.photo2 = ImageTk.PhotoImage(file='exit1.png')
        self.label2 = Button(self, image=self.photo2, command=parent.quit, borderwidth=0, highlightthickness=0,fg="white")
        self.label2.place(x=300, y=350)

class Page2(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#800063")
        self.parent = parent

        # Canvas for background and border radius
        self.canvas = Canvas(self, width=450, height=450, bg="#800063", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Draw rounded rectangle
        self.create_rounded_rectangle(25, 25, 425, 425, 20, fill='white')

        image = Image.open('gg2.png')
        image = image.resize((70, 70), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.label = Label(self, image=self.photo, bg="white")
        self.label.place(x=50, y=50)

        # Input
        self.requete = StringVar()
        self.entree = Entry(self, textvariable=self.requete,  bg="#800063")
        self.canvas.create_window(160, 110, window=self.entree, width=210, height=30)
        self.canvas.pack(padx=10)
        

        # Bouton Generate
        self.btn_generate_image = ImageTk.PhotoImage(file="generate2.png")
        self.btn_generate = Button(self, image=self.btn_generate_image,borderwidth=0, highlightthickness=0, fg="white", command=self.start_generation)
        self.canvas.create_window(345,110, window=self.btn_generate)

        # Partie d'affichage
        self.image_label = Label(self, bg="#800063", font=("Poppins", 15, "bold"))
        self.canvas.create_window(225, 250, window=self.image_label, width=330, height=200)

        # Bouton Retour
        self.btn_back_image = ImageTk.PhotoImage(file="back.png")
        self.btn_back = Button(self, image=self.btn_back_image,borderwidth=0, highlightthickness=0, fg="white", command=self.start_generation)
        self.canvas.create_window(350, 390, window=self.btn_back)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        # Draw a rounded rectangle on the canvas
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        self.canvas.create_polygon(points, **kwargs, smooth=True)

    def start_generation(self):
        prompt = self.requete.get()
        threading.Thread(target=self.generate_image, args=(prompt,)).start()

    def generate_image(self, prompt):
        pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
        image = pipe(prompt).images[0]
        image.save("image.png")
        self.display_image("image.png")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img)
        self.image_label.image = img

    def go_back(self):
        self.pack_forget()
        self.parent.page1.pack(fill="both", expand=True)

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import threading
from diffusers import StableDiffusionPipeline
from diffusers import DiffusionPipeline

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Copilot")
        self['bg'] = 'purple'
        self.resizable(height=False, width=False)

        # Page du logo
        self.logo_page = LogoPage(self)
        self.logo_page.pack(fill="both", expand=True)

        self.after(5000, self.show_page1)

    def show_page1(self):
        self.logo_page.pack_forget()
        self.page1 = Page1(self)
        self.page1.pack(fill="both", expand=True)

    def show_page2(self):
        self.page1.pack_forget()
        self.page2 = Page2(self)
        self.page2.pack(fill="both", expand=True)

class LogoPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.parent = parent

        # Afficher un logo ou un texte de bienvenue
        self.photo = PhotoImage(file='gg1.png')
        self.label = Label(self, image=self.photo)
        self.label.pack(pady=20)

class Page1(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.parent = parent

        image = Image.open('gg2.png')
        image = image.resize((300, 300), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.label = Label(self, image=self.photo, bg="white")
        self.label.pack(pady=50)

        # Label d'instruction
        self.label = Label(self, text="Let's Generate", font=("Poppins", 15, "bold"), fg="black", bg="white")
        self.label.pack(pady=100)

        # Bouton Generate
        self.btn_generate_image = ImageTk.PhotoImage(file="generate1.png")
        self.btn_generate = Button(self, image=self.btn_generate_image, command=parent.show_page2, borderwidth=0, highlightthickness=0, fg="white")
        self.btn_generate.place(x=100, y=350)

        # Bouton Quitter
        self.photo2 = ImageTk.PhotoImage(file='exit1.png')
        self.label2 = Button(self, image=self.photo2, command=parent.quit, borderwidth=0, highlightthickness=0,fg="white")
        self.label2.place(x=300, y=350)

class Page2(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#800063")
        self.parent = parent

        # Canvas for background and border radius
        self.canvas = Canvas(self, width=450, height=450, bg="#800063", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Draw rounded rectangle
        self.create_rounded_rectangle(25, 25, 425, 425, 20, fill='white')

        image = Image.open('gg2.png')
        image = image.resize((70, 70), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.label = Label(self, image=self.photo, bg="white")
        self.label.place(x=50, y=50)

        # Input
        self.requete = StringVar()
        self.entree = Entry(self, textvariable=self.requete,  bg="#800063")
        self.canvas.create_window(160, 110, window=self.entree, width=210, height=30)
        self.canvas.pack(padx=10)
        

        # Bouton Generate
        self.btn_generate_image = ImageTk.PhotoImage(file="generate2.png")
        self.btn_generate = Button(self, image=self.btn_generate_image,borderwidth=0, highlightthickness=0, fg="white", command=self.start_generation)
        self.canvas.create_window(345,110, window=self.btn_generate)

        # Partie d'affichage
        self.image_label = Label(self, bg="#800063", font=("Poppins", 15, "bold"))
        self.canvas.create_window(225, 250, window=self.image_label, width=330, height=200)

        # Bouton Retour
        self.btn_back_image = ImageTk.PhotoImage(file="back.png")
        self.btn_back = Button(self, image=self.btn_back_image,borderwidth=0, highlightthickness=0, fg="white", command=self.start_generation)
        self.canvas.create_window(350, 390, window=self.btn_back)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        # Draw a rounded rectangle on the canvas
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        self.canvas.create_polygon(points, **kwargs, smooth=True)

    def start_generation(self):
        prompt = self.requete.get()
        threading.Thread(target=self.generate_image, args=(prompt,)).start()

    def generate_image(self, prompt):
        pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
        image = pipe(prompt).images[0]
        image.save("image.png")
        self.display_image("image.png")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img)
        self.image_label.image = img

    def go_back(self):
        self.pack_forget()
        self.parent.page1.pack(fill="both", expand=True)

# Lancer l'application
if __name__ == "__main__":
    app = Application()
    app.mainloop()
