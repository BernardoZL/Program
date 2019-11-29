import os
from peewee import *

arq = "Bernardo.sql"
if os.path.exists(arq):
	os.remove(arq)

db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta:
		database = db

class Midia(BaseModel):
	tipo_midia = CharField()
	copias = CharField()

class Distribuidora(BaseModel):
	nome = CharField()
	cnpj = CharField()

class Desenvolvedor(BaseModel):
	nome = CharField()
	funcao = CharField()

class Produtora(BaseModel):
	nome = CharField()
	cnpj = CharField()
	desenvolvedor = ForeignKeyField(Desenvolvedor)

class Jogo(BaseModel):
	midia = ForeignKeyField(Midia)
	distribuidora = ForeignKeyField(Distribuidora)
	produtora = ForeignKeyField(Produtora)
	nome = CharField()
	preço = CharField()
	genero = CharField()

class Locacao(BaseModel):
	dia_locado = CharField()
	dia_devolvido = CharField()
	multa = CharField()
	jogo = ForeignKeyField(Jogo)

class Endereco(BaseModel):
	rua = CharField()
	bairro = CharField()
	cidade = CharField()

class Cliente(BaseModel):
	telefone = CharField()
	nome = CharField()
	cpf = CharField()
	endereco = ForeignKeyField(Endereco)

class Funcionario(BaseModel):
	nome = CharField()
	cargo = CharField()

class Locadora(BaseModel):
	jogos = ManyToManyField(Jogo)
	endereço = ForeignKeyField(Endereco)
	cliente = ForeignKeyField(Cliente)
	funcionario = ForeignKeyField(Funcionario)
	nome = CharField()
	cnpj = CharField()

db.create_tables([Midia, Distribuidora, Desenvolvedor, Produtora, Locacao, Jogo, Cliente, Funcionario, Endereco, Locadora, Locadora.jogos.get_through_model()])

midia1 = Midia.create(tipo_midia = "CD", copias = "5")
distribuidora1 = Distribuidora.create(nome = "BrazilGames", cnpj = "090909")
desenvolvedor1 = Desenvolvedor.create(nome = "Joao", funcao = "Diretor Geral")
produtora1 = Produtora.create(nome = "BrazilGroup", cnpj = "060606", desenvolvedor = desenvolvedor1)
jogo1 = Jogo.create(midia = midia1, distribuidora = distribuidora1, produtora = produtora1, nome = "BombaPatch2020" , preço = "10 reais", genero = "Futebol")
endereco1 = Endereco.create(rua = "Kappa", bairro = "Rio", cidade = "Arakawa")
locacao1 = Locacao.create(dia_locado = "19/09/2019", dia_devolvido = "29/09/2019", multa = "5", jogo = jogo1)
endereco2 = Endereco.create(rua = "Hoshi", bairro = "Rio", cidade = "Arakawa")
cliente1 = Cliente.create(telefone = "898989", nome = "Batata", cpf = "05002020007", endereco = endereco1)
funcionario1 = Funcionario.create(nome = "Jose", cargo = "gerente")
locadora1 = Locadora.create(endereço = endereco2, cliente = cliente1, funcionario = funcionario1, nome = "LocadoraDeJogos", cnpj = "9898989")
locadora1.jogos.add(jogo1)

print(cliente1.nome)
