import tkinter as tk
from tkinter import messagebox
import random
import os

# Nome do arquivo para salvar jogadas
SAVE_FILE = "rolagens.txt"

def rolar_dado():
    try:
        dado = int(dado_var.get().replace("d", ""))
        quantidade = int(qtd_entry.get())
        bonus = int(bonus_entry.get())
        
        resultados = [random.randint(1, dado) for _ in range(quantidade)]
        total = sum(resultados) + bonus
        
        # Formatar a saída
        resultado_str = f"{quantidade}d{dado} + {bonus} = " + " + ".join(map(str, resultados)) + f" = {total}"
        
        resultado_label.config(text=resultado_str)
        salvar_rolagem(resultado_str)
        atualizar_historico()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def salvar_rolagem(rolagem):
    with open(SAVE_FILE, "a") as file:
        file.write(rolagem + "\n")

def carregar_historico():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            return file.read()
    return "Nenhuma rolagem salva."

def atualizar_historico():
    historico_text.delete("1.0", tk.END)
    historico_text.insert(tk.END, carregar_historico())

# Configuração da janela principal
root = tk.Tk()
root.title("Rolador de Dados D&D")
root.geometry("600x300")

# Frame esquerdo (Dashboard)
dash_frame = tk.Frame(root)
dash_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Opções de dados
tk.Label(dash_frame, text="Escolha o dado:").pack()
dado_var = tk.StringVar(value="d20")
tk.OptionMenu(dash_frame, dado_var, "d4", "d6", "d8", "d10", "d12", "d20", "d100").pack()

# Entrada para quantidade de dados
tk.Label(dash_frame, text="Quantidade de dados:").pack()
qtd_entry = tk.Entry(dash_frame)
qtd_entry.pack()
qtd_entry.insert(0, "1")

# Entrada para bônus/penalidade
tk.Label(dash_frame, text="Bônus/Penalidade:").pack()
bonus_entry = tk.Entry(dash_frame)
bonus_entry.pack()
bonus_entry.insert(0, "0")

# Botão de rolagem
tk.Button(dash_frame, text="Rolar Dado", command=rolar_dado).pack()

# Exibição do resultado
resultado_label = tk.Label(dash_frame, text="")
resultado_label.pack()

# Frame direito (Histórico de rolagens)
hist_frame = tk.Frame(root)
hist_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Título do histórico
tk.Label(hist_frame, text="Histórico de Rolagens").pack()

# Caixa de texto para exibir o histórico
historico_text = tk.Text(hist_frame, height=15, width=30)
historico_text.pack()
atualizar_historico()

# Iniciar o loop da interface
tk.mainloop()
