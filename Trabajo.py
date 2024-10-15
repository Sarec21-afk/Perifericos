# Importamos tkinter y ttkthemes
import tkinter as tk
from tkinter import ttk, messagebox, END, Toplevel
from ttkthemes import ThemedTk
import  re
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk

# Creamos la ventana donde estará la notebook
window = ThemedTk(theme="radiance")
window.geometry("500x700")
window.title("Calculadora científica")

# Ajustamos para que los widgets internos crezcan con la ventana
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Creamos la notebook donde irán los frames
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True, fill= "both")

# Creamos los frames correspondientes
frame_areas = ttk.Frame(notebook, width="480", height="700")
frame_calculadora = ttk.Frame(notebook, width="480", height="700")
frame_funcion = ttk.Frame(notebook, width="480", height="700")
frame_nombres = ttk.Frame(notebook, width="480", height="700")

# Configuramos que los frames se expandan tanto en horizontal como en vertical
frame_areas.pack(fill="both", expand=True)
frame_calculadora.pack(fill="both", expand=True)
frame_funcion.pack(fill="both", expand=True)
frame_nombres.pack(fill="both", expand=True)

# Insertamos los frames en nuestra notebook
notebook.add(frame_areas, text="Calcular áreas")
notebook.add(frame_calculadora, text="Calculadora")
notebook.add(frame_funcion, text="CheckButton")
notebook.add(frame_nombres, text="Integrantes")

# -------------------------------------Diseño del cálculo de áreas---------------------------------------------------------------------

# Funciones para calcular el área
def calcular_area():
    figura = combobox_figura.get()
    if figura == "Seleccionar figura":
        messagebox.showwarning("Advertencia", "Por favor, seleccione una figura para calcular el área")
        return

    try:
        if figura == "Cuadrado":
            lado = float(entry1.get())
            area = lado ** 2
            resultado_label.config(text=f"El área del cuadrado es: {area}")

        elif figura == "Rectángulo":
            base = float(entry1.get())
            altura = float(entry2.get())
            area = base * altura
            resultado_label.config(text=f"El área del rectángulo es: {area}")

        elif figura == "Triángulo":
            base = float(entry1.get())
            altura = float(entry2.get())
            area = (base * altura) / 2
            resultado_label.config(text=f"El área del triángulo es: {area}")

        elif figura == "Círculo":
            radio = float(entry1.get())
            area = 3.1416 * (radio ** 2)
            resultado_label.config(text=f"El área del círculo es: {area}")

        elif figura == "Polígono regular":
            perimetro = float(entry1.get())
            apotema = float(entry2.get())
            area = (perimetro * apotema) / 2
            resultado_label.config(text=f"El área del polígono es: {area}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        return
    
    btn_calcular.pack_forget()
    btn_recalcular.pack(side=tk.LEFT, padx=20)
    btn_salir.pack(side=tk.RIGHT, padx=20)
    combobox_figura.config(state="disabled")

def reiniciar():
    combobox_figura.set("Seleccionar figura")
    combobox_figura.config(state="normal")
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry1.config(state='disabled')
    entry2.config(state='disabled')
    label1.pack_forget()
    label2.pack_forget()
    entry1.pack_forget()
    entry2.pack_forget()
    resultado_label.config(text="")
    btn_recalcular.pack_forget()
    btn_salir.pack_forget()
    btn_calcular.pack(pady=10)

def actualizar_campos(event):
    figura = combobox_figura.get()
    entry1.config(state='normal')
    entry2.config(state='normal')
    entry1.delete(0, END)
    entry2.delete(0, END)

    if figura == "Cuadrado":
        label1.config(text="Lado:")
        label2.pack_forget()
        entry2.pack_forget()
        label1.pack()
        entry1.pack()

    elif figura == "Rectángulo":
        label1.config(text="Base:")
        label2.config(text="Altura:")
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()

    elif figura == "Triángulo":
        label1.config(text="Base:")
        label2.config(text="Altura:")
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()

    elif figura == "Círculo":
        label1.config(text="Radio:")
        label2.pack_forget()
        entry2.pack_forget()
        label1.pack()
        entry1.pack()

    elif figura == "Polígono regular":
        label1.config(text="Perímetro:")
        label2.config(text="Apotema:")
        label1.pack()
        entry1.pack()
        label2.pack()
        entry2.pack()
    else:
        entry1.config(state='disabled')
        entry2.config(state='disabled')
        label1.pack_forget()
        label2.pack_forget()
        entry1.pack_forget()
        entry2.pack_forget()

def validate_entry(new_value):
    return new_value == "" or new_value.replace(".", "", 1).isdigit()

# Diseño del frame_areas
label_seleccion = ttk.Label(frame_areas, text="Seleccione la figura para calcular el área:")
label_seleccion.pack(pady=10)

figuras = ["Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Polígono regular"]
combobox_figura = ttk.Combobox(frame_areas, values=figuras, state="readonly")
combobox_figura.set("Seleccionar figura")
combobox_figura.bind("<<ComboboxSelected>>", actualizar_campos)
combobox_figura.pack(pady=10)

label1 = ttk.Label(frame_areas, text="")
label2 = ttk.Label(frame_areas, text="")

validate_numeric = frame_areas.register(validate_entry)
entry1 = ttk.Entry(frame_areas, validate="key", validatecommand=(validate_numeric, "%P"))
entry2 = ttk.Entry(frame_areas, validate="key", validatecommand=(validate_numeric, "%P"))
entry1.config(state='disabled')
entry2.config(state='disabled')

btn_calcular = ttk.Button(frame_areas, text="Calcular Área", command=calcular_area)
btn_calcular.pack(pady=10)

resultado_label = ttk.Label(frame_areas, text="", font=("Arial", 10))
resultado_label.pack(pady=20)

btn_recalcular = ttk.Button(frame_areas, text="Calcular otra área", command=reiniciar)
btn_salir = ttk.Button(frame_areas, text="Salir", command=window.destroy)

# -------------------------------------Diseño de la calculadora---------------------------------------------------------------------

# Función para evaluar operaciones de forma segura, incluyendo porcentajes
def calcular_operacion():
    try:
        expresion = entrada_calculadora.get()
        expresion_procesada = procesar_porcentaje(expresion)  # Procesamos los porcentajes en la expresión
        resultado = eval(expresion_procesada)  # Evaluamos la expresión con eval()
        etiqueta_resultado_calculadora.config(text=f"Resultado: {resultado}")
    except Exception as e:
        etiqueta_resultado_calculadora.config(text=f"Error: {e}")

# Función para procesar el operador de porcentaje en la expresión
def procesar_porcentaje(expresion):
    
    #Convierte los porcentajes en la expresión en su equivalente en fracción. 
    # Por ejemplo, 20% se convierte en 20/100.
    
    def reemplazo_porcentaje(match):
        # match.group(1) contiene el número antes del %
        numero = float(match.group(1))  # Convertimos el número a flotante
        return str(numero / 100)  # Devolvemos el valor en forma de fracción (porcentaje)

    # Utilizamos re.sub para buscar todos los números seguidos de un % y los procesamos
    expresion_sin_porcentajes = re.sub(r'(\d+(\.\d+)?)%', reemplazo_porcentaje, expresion)
    return expresion_sin_porcentajes


# Función para limpiar la entrada y ocultar el resultado
def limpiar_calculadora():
    entrada_calculadora.delete(0, END)
    etiqueta_resultado_calculadora.config(text="")  # Limpiamos la etiqueta del resultado

#Función para el botón que cambia de signo
def cambiar_signo():
    # Obtener el valor actual de la entrada de la calculadora
    valor_actual = entrada_calculadora.get()

    if valor_actual:  # Si hay un valor en la entrada
        # Si el valor comienza con "-", quitar el signo negativo
        if valor_actual.startswith("-"):
            entrada_calculadora.delete(0, tk.END)  # Borrar el valor actual
            entrada_calculadora.insert(0, valor_actual[1:])  # Insertar el número sin el signo "-"
        else:
            # Si el número es positivo, añadir el signo negativo al principio
            entrada_calculadora.insert(0, "-")


# Diseño del frame_calculadora usando exclusivamente grid()
label_calculadora = ttk.Label(frame_calculadora, text="Calculadora", font=("Arial", 16))
label_calculadora.grid(row=0, column=0, columnspan=4, pady=10)

entrada_calculadora = ttk.Entry(frame_calculadora, justify='right', font=("Arial", 18))
entrada_calculadora.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Crear los botones de la calculadora
botones = [
    ('C', 2, 0), ('+/-', 2, 1), ('%', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('0', 6, 0, 2), ('.', 6, 2), ('=', 6, 3)
]

def agregar_caracter(caracter):
    entrada_calculadora.insert(END, caracter)

# Colocar los botones en el grid
for boton in botones:
    texto = boton[0]
    fila = boton[1]
    columna = boton[2]

    # Crear los botones
    if texto == 'C':
        btn = ttk.Button(frame_calculadora, text=texto, command=limpiar_calculadora)
    elif texto == '=':
        btn = ttk.Button(frame_calculadora, text=texto, command=calcular_operacion)
    elif texto == '+/-':
        btn = ttk.Button(frame_calculadora, text=texto, command=cambiar_signo) 
    else:
        btn = ttk.Button(frame_calculadora, text=texto, command=lambda t=texto: agregar_caracter(t))
    
    
    if len(boton) == 4:
        btn.grid(row=fila, column=columna, columnspan=2, sticky="nsew", padx=5, pady=5)
    else:
        btn.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# Expandir filas y columnas para que los botones se ajusten
for i in range(7):
    frame_calculadora.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame_calculadora.grid_columnconfigure(j, weight=1)

# Etiqueta para mostrar el resultado
etiqueta_resultado_calculadora = ttk.Label(frame_calculadora, text="", font=("Arial", 16))
etiqueta_resultado_calculadora.grid(row=7, column=0, columnspan=4, pady=10)

# Botón para salir de la calculadora
btn_salir_calculadora = ttk.Button(frame_calculadora, text="Salir", command=window.destroy)
btn_salir_calculadora.grid(row=8, column=0, columnspan=4, pady=10)


# -------------------------------------Espacio para el diseño del widget CheckButton---------------------------------------------------------------------

def update_progress():
    completadas = sum(var.get() for var in tareas_var)
    total = len(tareas)
    progreso = (completadas / total) * 100
    etiqueta_progreso.config(text=f"Progreso: {progreso:.2f}%")
    
# Configuración de la ventana    
    
label_titulo = ttk.Label(frame_funcion, text="Lista de pendientes:")
tareas = ["Hacer el codigo", "Comprobar que funcione", "Hacer el video de como funciona el codigo", "Hacer el reporte del codigo", "Enviar el video y reporte a tiempo", "Pasar epicamente la materia con musica de Linkin Park de fondo"]
tareas_var = []

label_titulo.pack(pady=20)


# Crear Checkbuttons y empaquetarlos
for tarea in tareas:
    var = tk.IntVar()
    tareas_var.append(var)
    checkbutton = ttk.Checkbutton(frame_funcion, text=tarea, variable=var, command=update_progress)
    checkbutton.pack(pady=5)

# Crear etiqueta de progreso y empaquetarla
etiqueta_progreso = ttk.Label(frame_funcion, text="Progreso: 0.00%")
etiqueta_progreso.pack(pady=20)


# -------------------------------------Diseño para los nombres de los integrantes---------------------------------------------------------------------

#Cargamos la imagen usando pillow
ruta_imagen = r"C:/Perifericos/ya_es_toda.jpg" 
try:
    # Cargar la imagen
    imagen_original = Image.open(ruta_imagen)
    imagen_meme = ImageTk.PhotoImage(imagen_original)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    imagen_meme = None  # En caso de error, la imagen será None

# Datos de los integrantes
integrantes = [
    {"nombre": "Arturo Xassiel Bernal Jiménez", "matricula": "231403107", "numero_lista": "2"},
    {"nombre": "Leonardo Ortega Martínez", "matricula": "231403078", "numero_lista": "14"},
    {"nombre": "Omar Pérez Guzmán", "matricula": "231403128", "numero_lista": "17"},
    {"nombre": "Cesar Romero Toxqui", "matricula": "231403057", "numero_lista": "21"}
]

# Crear las etiquetas con la información de cada integrante
for integrante in integrantes:
    label_nombre = ttk.Label(frame_nombres, text=f"Nombre: {integrante['nombre']}")
    label_nombre.pack(pady=5)
    
    label_matricula = ttk.Label(frame_nombres, text=f"Matrícula: {integrante['matricula']}")
    label_matricula.pack(pady=5)
    
    label_numero_lista = ttk.Label(frame_nombres, text=f"Número de lista: {integrante['numero_lista']}")
    label_numero_lista.pack(pady=5)
    

# Insertar la imagen
if imagen_meme: 
 label_imagen = ttk.Label(frame_nombres, image=imagen_meme)
 label_imagen.pack(pady=10)
#Mantener la referencia de la imagen para evitar que se recolecte por el garbage collector
frame_nombres.image = imagen_meme


# ------------------- Ventana del "Adivino virtual" dentro del frame_nombres--------------------------------
def abrir_adivino_virtual():
    # Crear una nueva ventana
    ventana_adivino = Toplevel(window)
    ventana_adivino.title("Adivino Virtual")
    ventana_adivino.geometry("300x200")

    # Label para que el usuario piense un número
    label_pregunta = ttk.Label(ventana_adivino, text="Piensa un número del 1 al 10")
    label_pregunta.pack(pady=10)

    # Entry para que el usuario ingrese el número
    entry_numero = ttk.Entry(ventana_adivino)
    entry_numero.pack(pady=10)

    # Función para leer el número y mostrar el proceso de "adivinación"
    def leer_mente():
        try:
            numero = int(entry_numero.get())
            if numero < 1 or numero > 10:
                raise ValueError("Número fuera de rango")

            # Ventana con barra de progreso
            ventana_progreso = Toplevel(ventana_adivino)
            ventana_progreso.title("Leyendo la mente...")
            ventana_progreso.geometry("400x200")
            
            # Barra de progreso
            progress = Progressbar(ventana_progreso, orient="horizontal", length=300, mode="determinate")
            progress.pack(pady=20)
            
            # Label para mostrar mensajes
            label_proceso = ttk.Label(ventana_progreso, text="Analizando el pensamiento...")
            label_proceso.pack(pady=10)
            
            # Función para actualizar la barra y los mensajes con after()
            mensajes = [
                "Analizando el pensamiento...", 
                "Procesando la memoria...", 
                "Renderizando conexión cognitiva...", 
                "Proyección cerebral casi completa"
            ]
            
            def actualizar_progreso(i=0):
                if i < len(mensajes):
                    progress['value'] = (i + 1) * 25  # Incrementar el valor de la barra
                    label_proceso.config(text=mensajes[i])  # Actualizar el mensaje
                    ventana_progreso.after(1000, actualizar_progreso, i + 1)  # Llamar a esta función nuevamente después de 1 segundo
                else:
                    # Cuando el progreso esté completo, destruir ventana_progreso y mostrar el resultado
                    ventana_progreso.destroy()

                    # Mostrar una nueva ventana con el resultado
                    ventana_resultado = Toplevel(window)
                    ventana_resultado.title("Resultado")
                    ventana_resultado.geometry("300x150")
                    resultado_label_adivino = ttk.Label(ventana_resultado, text=f"Pensaste en el numero  {numero}")
                    resultado_label_adivino.pack(pady=20)
            
            ventana_progreso.after(500, actualizar_progreso)  # Iniciar la animación del progreso después de 0.5 segundos
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido entre 1 y 10")

    # Botón para activar la "lectura de la mente"
    boton_leer_mente = ttk.Button(ventana_adivino, text="Read my mind", command=leer_mente)
    boton_leer_mente.pack(pady=10)

# -------------------------------- Botón en el frame_nombres --------------------------------
# Botón para abrir el adivino virtual
boton_adivino_virtual = ttk.Button(frame_nombres, text="Adivino Virtual", command=abrir_adivino_virtual)
boton_adivino_virtual.pack(pady=20)

window.mainloop()