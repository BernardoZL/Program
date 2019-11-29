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

class Locação(BaseModel):
	dia_locado = CharField()
	dia_devolvido = CharField()
	multa = CharField()

class Jogo(BaseModel):
	midia = ForeignKeyField(Midia)
	distribuidora = ForeignKeyField(Distribuidora)
	produtora = ForeignKeyField(Produtora)
	locação = ForeignKeyField(Locação)
	nome = CharField()
	preço = CharField()
	genero = CharField()

Class Cliente(BaseModel):
	telefone = CharField()
	nome = CharField()
	cpf = CharField()
	endereco = ForeignKeyField(Endereco)

Class Funcionario(BaseModel):
	nome = CharField()
	cargo = CharField()

Class Edereco(BaseModel):
	rua = CharField()
	bairro = CharField()
	cidade = CharField()

Class Locadora(BaseModel):
	jogo = ManyToManyField(Jogo)
	endereço = ForeignKey(Endereco)
	cliente = ForeignKeyField(Cliente)
	funcionario = ForeignKeyField(Funcionario)
	nome = CharField()
	cnpj = CharField()


midia1 = Midia.create(tipo_midia = "CD", copias = "5")
distribuidora1 = Distribuidora.create(nome = "BrazilGames", cnpj = "090909")
desenvolvedor1 = Desenvolvedor.create(nome = "Joao", funcao = "Diretor Geral")
produtora1 = Produtora.create(nome = "BrazilGroup", cnpj = "060606", desenvolvedor = desenvolvedor1)
locacao1 = Locação.create(dia_locado = "19/09/2019", dia_devolvio = "29/09/2019", multa = "5")
jogo1 = Jogo.create(midia = midia1, distribuidora = distribuidora1, produtora = produtora1, nome = "BombaPatch2020" , locação = locacao1, preço = "10 reais", genero = "Futebol")
endereco1 = Endereco.create(rua = "Kappa", bairro = "Rio", cidade = "Arakawa")
endereco2 = Endereco.create(rua = "Hoshi", bairro = "Rio", cidade = "Arakawa")
cliente1 = Cliente.create(telefone = "898989", nome = "Batata", cpf = "05002020007" endereco = endereco1)
funcionario1 = Funcionario.create(nome = "Jose" funcao = "gerente")
locadora1 = Locadora.create(jogo = jogo1, endereço = endereco2, cliente = cliente1, funcionario = funcionario1, nome = "LocadoraDeJogos", cnpj = "9898989")
