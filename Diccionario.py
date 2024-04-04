#Punto 1 
Perro={}
print(Perro)

#Punto2

Perro = {  
         'nombre':'juan',
         'color':'verde',
         'raza':'chandal',
         'patas': 5,
         'edad':100
         
         }
print(Perro)

#Punto 3
Estudiante = {  
         'Nombre':'Federico',
         'Apellido':'Valverde',
         'Sexo':'Masculino',
         'Edad': 50,
         'Estado civil': 'Casado',
         'habilidades':['programacion', 'ganaderia'],
         'Pais':'Colombia',
         'Ciudad':'Cartagena',
         'direccion':'Barrio Mandela'
         
         }

#punto 4
print (Estudiante.keys())
print (Estudiante.values())
print (Estudiante.__len__())

#Punto 5

print(Estudiante['habilidades'])
print(type(Estudiante['habilidades']))


#Punto 6
hab = [Estudiante['habilidades']]
hab.append('gjgjhgjg')

print(hab)

#Punto 7
print (Estudiante.keys())

#Punto 8
print (Estudiante.values())


#Punto 9
print(Estudiante.items())

#Punto 10

Estudiante.pop('Nombre')
print( Estudiante)

#Punto 11
del Estudiante