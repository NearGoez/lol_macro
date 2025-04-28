class Activador:
    def __init__(self):
        self.activado = False


    def swap(self):

        if self.activado:
            self.activado = False
            print('Se desactivó la espera')
        else:
            self.activado = True
            print('esperando')

