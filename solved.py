from scipy.optimize import linprog
import tkinter as tk

# Función para resolver el problema de optimización lineal
def resolver_problema():
    # Obtener los valores ingresados por el usuario
    fo_coeffs = []
    restricciones_coeffs = []
    rhs_values = []

    # Coeficientes de la función objetivo
    for i in range(len(fo_entries)):
        fo_coeffs.append(float(fo_entries[i].get()))

    # Coeficientes de las restricciones y lado derecho
    for i in range(len(restricciones_entries)):
        restriccion_coeffs = []
        for j in range(len(restricciones_entries[i])):
            restriccion_coeffs.append(float(restricciones_entries[i][j].get()))
        restricciones_coeffs.append(restriccion_coeffs)
        rhs_values.append(float(rhs_entries[i].get()))

    # Coeficientes de las variables de la función objetivo
    c = [-coeff for coeff in fo_coeffs]

    # Coeficientes de las restricciones
    A = restricciones_coeffs
    b = rhs_values

    # Límites inferiores y superiores de las variables
    bounds = [(0, None)] * len(fo_coeffs)

    # Determinar el tipo de optimización (maximizar o minimizar)
    if var_optimizacion.get() == "Maximizar":
        c = [-coeff for coeff in c]

    # Resolver el problema de optimización lineal
    resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

    if resultado.success:
        solucion_x = resultado.x[0]
        solucion_y = resultado.x[1]
        label_resultado.config(text=f"Solución: x = {solucion_x}, y = {solucion_y}")
    else:
        label_resultado.config(text="No se encontró solución para el problema de optimización.")

# Crear la interfaz de usuario
ventana = tk.Tk()
ventana.title("Resolución de problema de optimización lineal")
ventana.geometry("400x350")

frame_fo = tk.Frame(ventana)
frame_fo.pack()

label_fo = tk.Label(frame_fo, text="Función Objetivo (FO):")
label_fo.pack(side=tk.LEFT)

fo_entries = []
while True:
    fo_entry = tk.Entry(frame_fo, width=5)
    fo_entry.pack(side=tk.LEFT)
    fo_entries.append(fo_entry)
    if len(fo_entries) == 2:
        break

frame_restricciones = tk.Frame(ventana)
frame_restricciones.pack()

label_restricciones = tk.Label(frame_restricciones, text="Restricciones:")
label_restricciones.pack()

restricciones_entries = []
rhs_entries = []
for i in range(2):
    frame_restriccion = tk.Frame(frame_restricciones)
    frame_restriccion.pack()

    restriccion_entries = []
    for j in range(2):
        restriccion_entry = tk.Entry(frame_restriccion, width=5)
        restriccion_entry.pack(side=tk.LEFT)
        restriccion_entries.append(restriccion_entry)
    restricciones_entries.append(restriccion_entries)

    rhs_entry = tk.Entry(frame_restriccion, width=5)
    rhs_entry.pack(side=tk.LEFT)
    rhs_entries.append(rhs_entry)

frame_optimizacion = tk.Frame(ventana)
frame_optimizacion.pack()

label_optimizacion = tk.Label(frame_optimizacion, text="Tipo de optimización:")
label_optimizacion.pack(side=tk.LEFT)

var_optimizacion = tk.StringVar(value="Minimizar")

radio_minimizar = tk.Radiobutton(frame_optimizacion, text="Minimizar", variable=var_optimizacion, value="Minimizar")
radio_minimizar.pack(side=tk.LEFT)

radio_maximizar = tk.Radiobutton(frame_optimizacion, text="Maximizar", variable=var_optimizacion, value="Maximizar")
radio_maximizar.pack(side=tk.LEFT)

boton_resolver = tk.Button(ventana, text="Resolver", command=resolver_problema)
boton_resolver.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()
