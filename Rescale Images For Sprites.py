from PIL import Image
import os

# Carpeta donde están las imágenes
INPUT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta si no existe
os.makedirs(INPUT_FOLDER, exist_ok=True)

# Extensiones permitidas
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".webp")

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(VALID_EXTENSIONS):
        path = os.path.join(INPUT_FOLDER, filename)

        with Image.open(path) as img:
            width, height = img.size

            # Reducir a la mitad
            new_size = (width // 2, height // 2)

            resized_img = img.resize(new_size, Image.LANCZOS)

            # Nuevo nombre: element_ANCHOxALTO
            extension = os.path.splitext(filename)[1].lower()
            new_filename = f"element_{new_size[0]}x{new_size[1]}{extension}"
            new_path = os.path.join(INPUT_FOLDER, new_filename)

            # Guardar con el nuevo nombre
            resized_img.save(new_path)

            # Eliminar el archivo original si tiene otro nombre
            if os.path.abspath(path) != os.path.abspath(new_path):
                os.remove(path)

            input(
                f"{filename}: "
                f"{width}x{height} → "
                f"{new_filename}"
            )

input("Resclaing Successful!")