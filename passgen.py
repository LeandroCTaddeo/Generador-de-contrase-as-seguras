import string
import random

""" /*genero variable con su input para el usuario*/ """

logitud = int(input("Ingrese el tamaño de la contraseña: "))

""" /*genero variable caracteres y llamo a import string y lo uso para traer caracteres*/ """
caracteres = string.ascii_letters + string.digits + string.punctuation


""" /*genero variable y llamo a join para juntar los caracteres de antes*/ """
""" /*coloco dentro random y choice para que seleccione de manera aleatoria estos caracteres*/ """
""" /*por ultimo le establezco la longitud que el usuario queria*/ """
contrasena = "".join(random.choice(caracteres) for i in range(logitud))

""" /*muestro la contraseña generada*/ """
print("La contraseña generada es: " + contrasena)