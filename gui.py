import tkinter as tk
from tkinter import scrolledtext
import sys
import io
from parser import parse_and_interpret  # Asegúrate de que esta importación sea correcta

# Función para ejecutar el código y capturar la salida
def execute_code():
    # Obtener el código del área de entrada
    code = code_input.get("1.0", tk.END)
    
    # Redirigir stdout para capturar las declaraciones print
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    # Llamar a la lógica del parser y la interpretación
    ast, symbol_table = parse_and_interpret(code)
    
    # Restablecer stdout
    sys.stdout = old_stdout
    
    # Obtener la salida y mostrarla en el área de salida
    output = new_stdout.getvalue()
    output_display.config(state=tk.NORMAL)  # Habilitar edición
    output_display.delete("1.0", tk.END)    # Limpiar salida anterior
    output_display.insert(tk.END, output)    # Insertar nueva salida
    output_display.config(state=tk.DISABLED)  # Deshabilitar edición

    # Mostrar el AST
    ast_display.config(state=tk.NORMAL)
    ast_display.delete("1.0", tk.END)  # Limpiar el área del AST
    ast_display.insert(tk.END, str(ast))  # Mostrar el AST
    ast_display.config(state=tk.DISABLED)  # Deshabilitar edición

    # Mostrar la tabla de símbolos
    symbol_display.config(state=tk.NORMAL)
    symbol_display.delete("1.0", tk.END)  # Limpiar el área de la tabla de símbolos
    for var, value in symbol_table.items():
        symbol_display.insert(tk.END, f"{var}: {value}\n")  # Mostrar cada símbolo
    symbol_display.config(state=tk.DISABLED)  # Deshabilitar edición

# Crear la ventana principal
root = tk.Tk()
root.title("Ejecutor de Código Python")

# Crear un área de texto para la entrada de código
code_input = scrolledtext.ScrolledText(root, width=80, height=20)
code_input.grid(row=0, column=0, padx=10, pady=10)

# Crear un área de texto para mostrar la salida
output_display = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
output_display.grid(row=0, column=1, padx=10, pady=10)

# Crear un botón de ejecución
execute_button = tk.Button(root, text="Ejecutar", command=execute_code)
execute_button.grid(row=0, column=2, padx=10, pady=10)

# Crear un marco para el AST
ast_frame = tk.LabelFrame(root, text="Árbol AST", padx=10, pady=10)
ast_frame.grid(row=1, column=0, padx=10, pady=10)

ast_display = scrolledtext.ScrolledText(ast_frame, width=80, height=10, state=tk.DISABLED)
ast_display.pack()

# Crear un marco para la tabla de símbolos
symbol_frame = tk.LabelFrame(root, text="Tabla de Símbolos", padx=10, pady=10)
symbol_frame.grid(row=2, column=0, padx=10, pady=10)

symbol_display = scrolledtext.ScrolledText(symbol_frame, width=40, height=10, state=tk.DISABLED)
symbol_display.pack()

# Iniciar la aplicación
root.mainloop()