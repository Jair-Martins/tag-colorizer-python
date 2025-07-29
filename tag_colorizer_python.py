import tkinter as tk
from tkinter import ttk, messagebox

import re

def colorir_texto(texto, palavras, tag_abre, tag_fecha):
    if not palavras:
        return texto
    padrao = r'\b(' + '|'.join(re.escape(p) for p in palavras) + r')\b'
    
    def substituir(match):
        return f"{tag_abre}{match.group(0)}{tag_fecha}"
    
    return re.sub(padrao, substituir, texto, flags=re.IGNORECASE)


def aplicar():
    texto = txt_entrada.get("1.0", "end-1c")
    palavras_raw = entry_palavras.get()
    tag_abre = entry_abre.get()
    tag_fecha = entry_fecha.get()

    if not texto.strip():
        messagebox.showwarning("Aviso", "O texto está vazio!")
        return
    if not palavras_raw.strip():
        messagebox.showwarning("Aviso", "Informe pelo menos uma palavra para destacar.")
        return

    palavras = [p.strip() for p in palavras_raw.split(",") if p.strip()]

    resultado = colorir_texto(texto, palavras, tag_abre, tag_fecha)
    txt_saida.delete("1.0", tk.END)
    txt_saida.insert(tk.END, resultado)

# Criando janela principal
root = tk.Tk()
root.title("Colorir Texto com Tags")

# Labels e campos
ttk.Label(root, text="Texto Original:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
txt_entrada = tk.Text(root, height=8, width=60)
txt_entrada.grid(row=1, column=0, columnspan=3, padx=5)

ttk.Label(root, text="Palavras para destacar (separadas por vírgula):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_palavras = ttk.Entry(root, width=60)
entry_palavras.grid(row=3, column=0, columnspan=3, padx=5)

ttk.Label(root, text="Tag de abertura:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
entry_abre = ttk.Entry(root, width=20)
entry_abre.grid(row=5, column=0, padx=5)

ttk.Label(root, text="Tag de fechamento:").grid(row=4, column=1, sticky="w", padx=5, pady=5)
entry_fecha = ttk.Entry(root, width=20)
entry_fecha.grid(row=5, column=1, padx=5)

btn_aplicar = ttk.Button(root, text="Aplicar", command=aplicar)
btn_aplicar.grid(row=5, column=2, padx=5)

ttk.Label(root, text="Texto com tags:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
txt_saida = tk.Text(root, height=8, width=60)
txt_saida.grid(row=7, column=0, columnspan=3, padx=5, pady=(0,10))

root.mainloop()

