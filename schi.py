import tkinter as tk
from tkinter import messagebox

def evaluar_esquizofrenia_esquizo_q():
    def evaluar():
        respuesta1 = respuesta1_var.get()
        respuesta2 = respuesta2_var.get()
        respuesta3 = respuesta3_var.get()
        respuesta4 = respuesta4_var.get()
        respuesta5 = respuesta5_var.get()

        puntaje = 0
        if respuesta1 == "Sí":
            puntaje += 1
        if respuesta2 == "Sí":
            puntaje += 1
        if respuesta3 == "Sí":
            puntaje += 1
        if respuesta4 == "Sí":
            puntaje += 1
        if respuesta5 == "Sí":
            puntaje += 1

        if puntaje >= 3:
            messagebox.showinfo("Resultado", "Su puntaje sugiere que podría estar en riesgo de esquizofrenia. Consulte a un profesional de la salud para una evaluación más detallada.")
        else:
            messagebox.showinfo("Resultado", "Su puntaje no indica necesariamente esquizofrenia, pero siempre es mejor buscar orientación médica si tiene preocupaciones.")

    ventana = tk.Tk()
    ventana.title("Evaluación ESQUIZO-Q")

    # Preguntas y opciones
    tk.Label(ventana, text="Por favor, responda las siguientes preguntas con 'Sí' o 'No':").pack()

    opciones = ["Sí", "No"]
    respuesta1_var = tk.StringVar(value="No")
    respuesta2_var = tk.StringVar(value="No")
    respuesta3_var = tk.StringVar(value="No")
    respuesta4_var = tk.StringVar(value="No")
    respuesta5_var = tk.StringVar(value="No")

    for i, pregunta in enumerate(["¿Ha experimentado alucinaciones?", "¿Ha tenido ideas delirantes o creencias extrañas?",
                                  "¿Ha notado cambios significativos en su pensamiento o comportamiento?",
                                  "¿Ha tenido dificultades para concentrarse o mantener la atención?",
                                  "¿Ha experimentado aislamiento social o dificultades para relacionarse con los demás?"]):
        tk.Label(ventana, text=pregunta).pack()
        tk.Radiobutton(ventana, text="Sí", variable=eval(f"respuesta{i+1}_var"), value="Sí").pack()
        tk.Radiobutton(ventana, text="No", variable=eval(f"respuesta{i+1}_var"), value="No").pack()

    tk.Button(ventana, text="Evaluar", command=evaluar).pack()

    ventana.mainloop()

# Ejecutar la función
evaluar_esquizofrenia_esquizo_q()


