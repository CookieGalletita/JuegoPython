almacigo= 5

class Semilla: 
    def __init__ (self, nombre, cantidad):
        self.nombre = nombre #semilla nombre
        self.cantidad = cantidad
        self.crecimiento= 5
    
    def plantarSemilla (self):
        global almacigo
        if self.cantidad >= 1 and almacigo > 1:
            self.cantidad -=1
            almacigo -= 1
            if self.cantidad ==1:
                print (f"Has usado una {self.nombre} te queda {self.cantidad} semilla 🌱")
            elif self.cantidad == 0:
                print (f"Haz usado una {self.nombre} te quedaste sin semillas🌱")
            else:
                print (f"Haz usado una {self.nombre} te quedan {self.cantidad} semillas 🌱")
        else:
            print(f"No hay suficiente {self.nombre}")

    def info (self):
        print(f"Tienes {self.cantidad} {self.nombre} 🌱")
        print(f"Tienes {almacigo} almacigos")


semillaRosa = Semilla("Semilla Rosa",5 )
semillaTulipan= Semilla("Semilla Tulipan",5)

semillaRosa.plantarSemilla()
semillaRosa.info()

semillaTulipan.plantarSemilla()
semillaTulipan.info()

    
