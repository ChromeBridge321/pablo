import tkinter as tk
from tkinter import scrolledtext
import sys
import io
from parser import parse_and_interpret  # Importar la nueva función

# Función para ejecutar el código y capturar la salida
def execute_code():
    # Obtener el código del área de entrada
    code = code_input.get("1.0", tk.END)
    
    # Redirigir stdout para capturar las declaraciones print
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    # Llamar a la lógica del parser y la interpretación
    result = parse_and_interpret(code)
    
    # Restablecer stdout
    sys.stdout = old_stdout
    
    # Obtener la salida y mostrarla en el área de salida
    output = new_stdout.getvalue()
    output_display.config(state=tk.NORMAL)  # Habilitar edición
    output_display.delete("1.0", tk.END)    # Limpiar salida anterior
    output_display.insert(tk.END, output)    # Insertar nueva salida
    output_display.insert(tk.END, f"\nResultado: {result}")  # Mostrar resultado de la interpretación
    output_display.config(state=tk.DISABLED) # Deshabilitar edición

# Crear la ventana principal
root = tk.Tk()
root.title("Ejecutor de Código Python")

# Crear un área de texto para la entrada de código
code_input = scrolledtext.ScrolledText(root, width=120, height=20)
code_input.pack(pady=10)

# Crear un botón de ejecución
execute_button = tk.Button(root, text="Ejecutar", command=execute_code)
execute_button.pack(pady=10)

# Crear un área de texto para mostrar la salida
output_display = scrolledtext.ScrolledText(root, width=120, height=20, state=tk.DISABLED)
output_display.pack(pady=10)

# Iniciar la aplicación
root.mainloop()