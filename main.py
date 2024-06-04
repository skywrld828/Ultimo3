from kivymd.app import *
from kivy.lang import *
from kivy.clock import Clock 
from kivy.core.clipboard import*
from kivymd.uix.label import *
from kivymd.uix.screen import *
from kivymd.uix.screenmanager import *
from kivymd.uix.card import *
from kivy.core.window import *
from kivymd.uix.dialog import*
from kivymd.uix.list import*
from kivymd.uix.button import*
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import*

from kivy.core.text import LabelBase
#LabelBase.register(name="Roboo",#fn_regular="Poppins-SemiBold (1).ttf")

LabelBase.register(name="Roboto",fn_regular="FFF Tusj.ttf")






Builder.load_file("joke.kv")

class tem(OneLineAvatarListItem):
	def __init__(self,y,**kwargs):
		super().__init__(**kwargs)
		self.text=y
		
class presplash (MDScreen):
	pass
class GER (MDScreenManager):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.add_widget(Jokes ())
	
class cards(MDCard):
	def __init__(self,y,**kwargs):
		super().__init__(**kwargs)
		self.ids.textos.text=y
class card	(MDCard):
	def __init__(self,y,**kwargs):
		super().__init__(**kwargs)
		self.ids.texto.text=y
	
			
	def dialog(self,*x):
		m=MDDialog(title="Quer Sair",buttons=[MDFlatButton(text="sim"),MDFlatButton(text="Nao")])
		m.open()
	
class Jokes(MDScreen):


	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		self.ids.py.clear_widgets()
		Clock.schedule_interval(self.verify2,1)
		Clock.schedule_interval(self.verify,1)
		self.memes_mocambique = [
    "Por que a mão do moçambicano está sempre gelada? - Porque ele vive na terra do sorvete.",
    "O que acontece quando um moçambicano encontra uma nota de 1000 meticais? - Ele faz uma festa!",
    "Qual é o esporte favorito dos moçambicanos? - Corrida de chapas!",
    "Por que o moçambicano nunca fica com frio? - Porque ele sabe como se agasalhar bem com capulanas.",
    "O que o moçambicano disse para o sapo? - Sai da estrada, camundongo!",
    "Por que o moçambicano nunca perde a esperança? - Porque sabe que a chuva de abril sempre chega.",
    "Qual é o segredo da boa comida moçambicana? - Um toque de piri-piri!",
    "Por que o moçambicano não gosta de escalada? - Porque ele prefere subir na vida de outra forma.",
    "O que o moçambicano disse para o ovo? - Anda cá que eu já te galo!",
    "Por que o moçambicano nunca está atrasado? - Porque ele segue o horário à moda africana.",
    "Qual é o esporte mais popular em Moçambique? - Futebol, é claro! É só olhar para as ruas durante uma partida importante.",
    "Por que o moçambicano é ótimo em festas? - Porque ele sabe como animar a pista com ritmos tradicionais.",
    "O que o moçambicano disse para a água? - Se juntas já causam, imagina misturadas!",
    
    "Por que o moçambicano é conhecido por sua hospitalidade? - Porque ele tem o coração tão grande quanto o Monte Namuli.",
    "O que o moçambicano disse para a girafa? - Como é lá de cima?",
    
    "Por que o Presidente Nyusi é tão bom em resolver problemas? Porque ele sempre encontra uma saída diplomática, como uma verdadeira figura de Estado!",
    "Qual é o prato favorito do Presidente Nyusi? Frango à Moçambicana, porque ele sabe como liderar com tempero e sabedoria!",
    "O que o Presidente Nyusi disse quando encontrou um buraco na estrada? 'Vamos tapar isso rapidamente e seguir em frente para um Moçambique ainda melhor!'",
    "Qual é a bebida favorita do Presidente Nyusi? Água de coco, porque ele sempre mantém a calma mesmo sob pressão!",
    "Por que o Presidente Nyusi adora histórias? Porque ele sabe que cada narrativa carrega lições valiosas para o futuro de Moçambique!",
    "Por que o Presidente Nyusi não usa óculos? Porque ele já tem uma visão clara para liderar Moçambique!",
    "O que o Presidente Nyusi disse para o mar? 'Deixe as ondas calmas guiarem o nosso país!'",
    "Qual é o animal favorito do Presidente Nyusi? O elefante, porque ele sempre leva a nação nas costas!",
    "Por que o Presidente Nyusi é bom em resolver enigmas? Porque ele sempre encontra a chave para o sucesso de Moçambique!",
    "O que o Presidente Nyusi disse para o sol? 'Brilhe forte, como a esperança que guia nosso povo!'",
    "Qual é o filme favorito do Presidente Nyusi? 'O Rei Leão', porque ele acredita no ciclo da vida e do desenvolvimento!"
]

	
		for x in self.memes_mocambique :
			self.ids.py.add_widget(card(x))
		self .memes = [
    "Por que Fred Jossias não seria um bom guardião de segredos do universo inteiro? Porque ele contaria tudo em seu show particular, revelando a galáxia de fofocas para seu público fiel!",
    "Se Fred Jossias fosse um super-herói, suas armas seriam microfones e seu superpoder seria fofocar mais rápido que a velocidade da luz!",
    "Fred Jossias seria péssimo em esportes radicais, pois em vez de segurar a adrenalina, seguraria a fofoca para espalhar depois!",
    "O que Fred Jossias faria se estivesse perdido na floresta? Ele encontraria o caminho de volta contando as fofocas das árvores e animais!",
    "Fred Jossias não conseguiria participar de um jogo de agente duplo, pois sempre entregaria os dois lados com suas fofocas!",
    "Se Fred Jossias fosse um juiz de competições culinárias, daria notas com base na quantidade de fofocas dos pratos!",
    "Por que Fred Jossias não pode ser um alpinista? Porque ele revelaria todos os segredos das montanhas antes mesmo de escalá-las!",
    "Se Fred Jossias fosse um robô, seu programa principal seria fofocar sem parar e atualizar as informações a cada segundo!",
    "Fred Jossias seria terrível em um jogo de adivinhação, pois já saberia as respostas antes e revelaria as perguntas secretas!",
    "O que Fred Jossias faria se descobrisse um portal para outra dimensão? Ele viajaria para lá para fofocar sobre as vidas paralelas!",
    "Se Fred Jossias fosse um personagem de desenho animado, seu superpoder seria transformar fofocas em realidade com sua caneta mágica!",
    "Fred Jossias seria o mestre das festas, pois animaria a todos contando fofocas divertidas e segurando o bom humor do povo!",
    "Por que Fred Jossias não seria um bom terapeuta? Porque ele revelaria os segredos dos pacientes em vez de guardar para si!",
    "Se Fred Jossias inventasse uma rede social, seria chamada de 'FofocaBook' e a senha seria 'segura meu povo moçambicano'!",
    "Fred Jossias não poderia ser um espião, pois seu disfarce seria descoberto pela fofoca que sempre o entrega!",
    "O que FredJossias faria se encontrasse um gênio da lâmpada? Pediria para realizar desejos fofocando sobre todos que conhece!",
    "Se Fred Jossias fosse um músico, todas as suas canções seriam baseadas em fofocas do dia a dia e ritmos animados!",
    "Fred Jossias seria o pior em manter uma surpresa, pois sempre entregaria o presente antes da hora fofocando sobre o que será dado!",
    "Por que Fred Jossias não pode ser um astronauta? Porque ele contaria as fofocas das estrelas e planetas para a Terra inteira!",
    "Se Fred Jossias fosse um inventor, sua criação mais famosa seria um dispositivo para transmitir fofocas instantaneamente para todos!",
    "Fred Jossias seria o rei das festas de aniversário, animando todos com suas fofocas e garantindo risadas sem parar!",
    "O que Fred Jossias faria se fosse um político? Ele revelaria os bastidores do governo e faria discursos cheios de fofocas para conquistar a audiência!"]

		for x in self.memes:
			self.ids.pys.add_widget(cards(x))
	
			
	def verify (self,interval):
		if self.ids.py.children=="":
			for x in self.memes_mocambique :
				self.ids.py.add_widget(card(x))
		else:
			print ("vvvvcccxz🇲🇿")
	def verify2(self,interval):
		if self.ids.pys.children=="":
			for x in self.memes:
				self.ids.pys.add_widget(cards(x))
		else:
			pass
	
		
	
	
	def menu(self):
		menu_item=[{"viewclass":"OneLineListItem","text":"Sair","divider_color":[1,1,1,1],"on_release":lambda x="44":MDApp().get_running_app().stop()},{"viewclass":"OneLineListItem","text":"Sobre","on_release":lambda x="44":self.conf()}]
		self.MEnu=MDDropdownMenu (items=menu_item,caller=self.ids.navi, width_mult=2,pos_hint={"x":.4,"y":.84},radius=[0,0,0,0])
		self.MEnu.open()
	def conf(self ):
		self.MEnu.dismiss()
		ls=MDDialog (title="MEMES ",text="ESTE APP FOI CRIADO COM INTUITO DE AJUDAR A SUA VIDA COMO MEMEIRO")
		ls.open()
	
class Demo(MDApp):
	def build(self):
		with open("tema.txt","r") as p:
			self.theme_cls.theme_style=p.read()
		
		return GER ()
	def copiar(self,x):
		Clipboard.copy(x)
		toast ("MEME COPIADO COM SUCESSO ")
	def Copiar(self,x):
		toast(x)
		Clipboard.copy(x)
	def conf(self):
		
		self.tema=MDDialog (title="Tema",radius=[0,0,0,0],type="confirmation",items=[tem("Light"),tem("Dark")])
		self.tema.open()
	def temas(self,x):
		if x=="Dark":
			self.theme_cls.theme_style="Dark"
		else:
			self.theme_cls.theme_style="Light"
		with open("tema.txt","w") as p:
			p.write(self.theme_cls.theme_style)
		self.tema.dismiss()
	
	
			
		
		
			
			
	
		

		

	
Demo().run()