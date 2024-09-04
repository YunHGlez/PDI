import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Imágenes")

        # Tamaño deseado para las imágenes
        self.image_size = (300, 300)
        
        # Crear un marco para organizar las imágenes en horizontal
        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        # Cuadro para mostrar la imagen original (lado izquierdo)
        self.original_canvas = tk.Label(self.image_frame, text="Imagen Original")
        self.original_canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Cuadro para mostrar la imagen modificada (lado derecho)
        self.modified_canvas = tk.Label(self.image_frame, text="Imagen Modificada")
        self.modified_canvas.pack(side=tk.RIGHT, padx=10, pady=10)

        # Crear un marco para organizar los botones en horizontal
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Botones de carga y filtros
        self.upload_button = tk.Button(self.button_frame, text="Cargar Imagen", command=self.load_image)
        self.upload_button.pack(side=tk.LEFT, padx=5)

        self.bw_button = tk.Button(self.button_frame, text="Blanco y Negro", command=self.apply_bw)
        self.bw_button.pack(side=tk.LEFT, padx=5)

        self.color_tint_button = tk.Button(self.button_frame, text="Aplicar Mica de Color", command=self.apply_color_tint)
        self.color_tint_button.pack(side=tk.LEFT, padx=5)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.original_image = self.resize_image(self.original_image, self.image_size)
            self.show_image(self.original_image, self.original_canvas)
            self.modified_image = self.original_image

    def resize_image(self, image, target_size):
        """Redimensiona la imagen manteniendo la proporción de aspecto."""
        image.thumbnail(target_size, Image.Resampling.LANCZOS)
        return image

    def show_image(self, image, canvas):
        tk_image = ImageTk.PhotoImage(image)
        canvas.config(image=tk_image)
        canvas.image = tk_image

    def apply_bw(self):
        if hasattr(self, 'original_image'):
            self.modified_image = ImageOps.grayscale(self.original_image)
            self.show_image(self.modified_image, self.modified_canvas)

    def apply_color_tint(self):
        if hasattr(self, 'original_image'):
            # Aquí puedes cambiar el color de la mica
            self.modified_image = ImageOps.colorize(ImageOps.grayscale(self.original_image), black="black", white="blue")
            self.show_image(self.modified_image, self.modified_canvas)

if __name__ == "__main__":
    root = tk.Tk()
    editor = ImageEditor(root)
    root.mainloop()
