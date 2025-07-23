class EscritorDeArchivos:
    def _init_(self, archivo, agregarAlFinal = False):
        self.escritor = open(archivo, 'w')

    def cerrar(self):
        self.escritor.close()

    def escribir(self, texto):
        datos_escritos = False
        if (not self.escritor.closed):
            self.escritor.write(texto)
            datos_escritos = True
        
        return datos_escritos

def main():
    escritor = EscritorDeArchivos("Prueba.txt")
    escritor.escribir("Hola mundo")
    escritor.cerrar()

if _name_ == "_main_":
    main()
