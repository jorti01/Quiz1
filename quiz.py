from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class EncenderComando(Command):
	def __init__(self):
		pass
	def excecute(self):
		print("Comando de encendido recibido.")

class ApagarComando(Command):
	def __init__(self):
		pass
	def execute(self):
		print("Comando de apagado recibido.")

class HablarComando(Command):
	def __init__(self,message):
		self.message = messsage
	def execute(self) -> None:
		print("El robot dice {0}".format(message))

class DormirComando(Command):

	def __init__(self):
		pass

	def execute(self):
		print("Comando de dormir recibido.")

class Bot:
	def __init__(self,command):
		self.command = command

	def command(self, command):
		self.command = command

	def ejecutar_comando(self):
		self.command.execute()
