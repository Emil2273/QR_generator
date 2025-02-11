import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode 
import io

root = tk.Tk()
root.geometry('900x800')
root.title("QR generator")

def generuj_qr():
    # pobieranie danych
    data = entry.get()
    if not data:
        return

    # generowanie kodu
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # tworzenie zdjęcia, bez zapisywania
    qr_image = qr.make_image(fill="black", back_color="white")

    # zmiana formatu
    img_bytes = io.BytesIO()
    qr_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    qr_tk = ImageTk.PhotoImage(Image.open(img_bytes))

    # odświeżenie imglbl z zdjęciem
    imglbl.config(image=qr_tk)
    imglbl.image = qr_tk


# pozycjonowanie wszysktich elementów 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

imglbl = ttk.Label(frame)
imglbl.grid(row=0, column=0)

entry = ttk.Entry(frame)
entry.grid(row=2, column=0, sticky="ew")
entry.bind('<Return>', lambda event:generuj_qr())

btn = ttk.Button(frame, text="Generuj", command=generuj_qr)
btn.grid(row=2, column=1)


lbl = ttk.Label(frame, text="Wprowadź adres URL, by wygenerować")
lbl.grid(row=3, column=0)



root.mainloop()