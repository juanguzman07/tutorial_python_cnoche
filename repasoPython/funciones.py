#Funciones

def miFuncion():
    print("Hola Mundo")


miFuncion()

def mostrarNombre(nombre, apellido):
    print("Su nombre es: "+nombre + " " + apellido)


mostrarNombre("Nathalia", "Franco") #Invocar la funcion

#Area triangulo
#Entradas
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area
#Salida
resultado = calcularAreaTriangulo(base, altura)
print("El area del triangulo es: ", resultado)

def mostrarMensaje(pais="Colombia"):
    print("Yo soy de: "+pais)


mostrarMensaje("Suiza")
mostrarMensaje("Ecuador")
mostrarMensaje()
mostrarMensaje("Bolivia")