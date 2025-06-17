import time

almacigo= 5
almacigo_usado = []

class Semilla: 
    def __init__ (self, nombre, cantidad):
        self.nombre = nombre #semilla nombre
        self.cantidad = cantidad
        self.semillaPlantada = None
        
    
    def plantarSemilla (self):
        global almacigo
        if self.cantidad >= 1 and almacigo >= 1:
            self.cantidad -=1
            almacigo -= 1
            self.semillaPlantada= SemillaPlantada(self.nombre, "Plantada", 5)

            almacigo_usado.append(self.semillaPlantada)

            if self.cantidad ==1:
                print (f"Has usado una {self.nombre} te queda {self.cantidad} semilla 🌱")
            elif self.cantidad == 0:
                print (f"Haz usado una {self.nombre} te quedaste sin semillas🌱")
            else:
                print (f"Haz usado una {self.nombre} te quedan {self.cantidad} semillas 🌱")
        else:
            print(f"No hay suficiente {self.nombre}")

        if almacigo_usado:
            print(f"\nTienes {len(almacigo_usado)} semillas plantadas:")
            for semilla in almacigo_usado:
                print(f"- {semilla.nombre}, estado: {semilla.estado}")
                print(f"Tienes {almacigo} almácigos libres.")
        else:
            print("\nNo hay semillas plantadas aún.")
            print(f"Tienes {almacigo} almácigos libres.")
        
        self.semillaPlantada.tiempoCrecimiento()
    

    def info (self):
        print(f"Tienes {self.cantidad} {self.nombre} 🌱")
        print(f"Tienes {almacigo} almacigos")


semillaRosa = Semilla("Semilla Rosa",5 )
semillaTulipan= Semilla("Semilla Tulipan",5)

class Flor:
    def __init__ (self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

        

   
class SemillaPlantada:
    global almacigo
    def __init__(self, nombre, estado, crecimiento):
        self.nombre= nombre
        self.estado= estado #creciendo lista 
        self.crecimiento= crecimiento


    
    def tiempoCrecimiento(self):

        tiempoInicial = time.time()
        plantaCrecida = tiempoInicial + self.crecimiento
        
        while time.time() <= plantaCrecida:
            tiempoRestante = int(plantaCrecida - time.time())
            print(f"Tiempo restante", tiempoRestante, " segundos" )
            time.sleep(1)
        
        if tiempoRestante  == 0:
             print(f"{self.nombre} Ha Crecido 🌺")


  

semillaRosa.plantarSemilla()
semillaRosa.info()



    
