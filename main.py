# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:22:54 2021

@author: Márcio Bruno Dos Santos Correia

Esse algoritmo foi criado usando Python3.

Ele cria um objeto  package a partir de um código de barras, este
objeto tem como atributos as características do pacote.

Os pacotes de entrada estão organizados em um dicionário: {'Pacote 1':'código de barras',...}
Por fim o algoritmo obtém as informações pedidas pela Loggi e exibe ao usuário.
"""

class package:
    """ Input: código de barras (string)
                Atributos:
                id - código de barras (string)
                origem - região de origem (string)
                destino - região de origem (string)
                loggi - código da loggi (string)
                vendedor - código do vendedor (string)
                produto - tipo de produto (string)
                check - validade do código de barras (string) \n
        Cria um objeto package e testa sua validade considerando 
        as restrições definidas"""
        
    # RECEBE CÓDIGO DE BARRAS COMO STRING E DEFINE AS CARACTERÍSTICAS DO PACOTE
    def __init__(self,codigo):
        self.id = codigo
        self.origem = 'Inválido'
        self.destino = 'Inválido'
        self.loggi = 'Inválido'
        self.vendedor = 'Inválido'
        self.produto = 'Inválido'
        self.check = 'Código válido'
        
        try:
            self.origem = dict_regioes[codigo[:3]]           
        except KeyError:
            self.check = 'Código inválido'
            
        try:
            self.destino = dict_regioes[codigo[3:6]]           
        except KeyError:
            self.check = 'Código inválido'
            
        try:
            self.loggi = codigo[6:9]
        except KeyError:
            self.check = 'Código inválido'
            
        try:
            self.vendedor = codigo[9:12]
        except KeyError:
            self.check = 'Código inválido'
            
        try:
            self.produto = dict_produtos[codigo[12:15]]
        except KeyError:
            self.check = 'Código inválido'
            
        if self.loggi != '555' or self.vendedor in list_vendedorInvalid:
            self.check = 'Código inválido'
            
        if self.produto == 'Jóias' and self.origem == 'Centro-Oeste':
            self.check = 'Código inválido'
            
#-----------------------------------------------------------------------------#

#DEFINIÇÃO DAS REGIÕES E PRODUTOS ACEITOS PELA LOGGI E SEU CÓDIGO
dict_regioes = {'000': 'Sul','111': 'Centro-Oeste','333': 'Nordeste',\
                  '555': 'Norte','888': 'Sudeste'}
dict_produtos = {'000': 'Jóias','111': 'Livros','333': 'Eletrônicos',\
                  '555': 'Bebidas','888': 'Brinquedos'}
#DEFINIÇÃO DE VENDEDORES INVÁLIDOS
list_vendedorInvalid = ['584']

#DICIONÁRIO DOS NOMES DOS PACOTES (KEY) E O CÓDIGO DE BARRA (VALUE)
dict_pacotesID = {'Pacote 1': '888555555123888','Pacote 2': '333333555584333',\
           'Pacote 3': '222333555124000','Pacote 4': '000111555874555',\
           'Pacote 5': '111888555654777','Pacote 6': '111333555123333',\
           'Pacote 7': '555555555123888','Pacote 8': '888333555584333',\
           'Pacote 9': '111333555124000','Pacote 10': '333888555584333',\
           'Pacote 11': '555888555123000','Pacote 12': '111888555123555',\
           'Pacote 13': '888000555845333','Pacote 14': '000111555874000',\
           'Pacote 15': '111333555123555'}
    
#DICIONÁRIO DE TODOS OS CÓDIGOS DE BARRA
#NOME DO PACOTE (KEY) E OBJETO PACOTE (VALUE)
dict_packages = {}
for pacote_id,codigo in dict_pacotesID.items():
    dict_packages[pacote_id] = package(codigo)
     
#-----------------------------------------------------------------------------#
# A - IDENTIFICAR O DESTINO DE TODOS OS PACOTES
print('DESTINO DOS PACOTES')
for pacote_id,pacote in dict_packages.items():
    print('O destino do {} é a região {}'.format(pacote_id,pacote.destino))
print('\n')

#-----------------------------------------------------------------------------#
# B - IDENTIFICAR OS PACOTES VÁLIDOS E INVÁLIDOS

#DICIONÁRIOS DE PACOTES VÁLIDOS, INVÁLIDOS 
#NOME DO PACOTE (KEY) E OBJETO PACOTE (VALUE)
dict_packagesValid,dict_packagesInvalid = {},{}
for pacote_id,pacote in dict_packages.items():
    if pacote.check == 'Código válido':
        dict_packagesValid[pacote_id] = pacote
    else:
        dict_packagesInvalid[pacote_id] = pacote
        
print('PACOTES VÁLIDOS')
for pacote_id,pacote in dict_packagesValid.items():
    print(pacote_id)
print('\n')
print('PACOTES INVÁLIDOS')
for pacote_id,pacote in dict_packagesInvalid.items():
    print(pacote_id)
print('\n')

#-----------------------------------------------------------------------------#
# C - IDENTIFICAR PACOTES COM ORIGEM NO SUL COM BRINQUEDOS
print('PACOTES DO SUL COM BRINQUEDOS')
list_pacotes = []
test_regiao = 'Sul'
test_produto = 'Brinquedos'
for pacote_id,pacote in dict_packages.items():
    if pacote.origem == test_regiao and pacote.produto == test_produto:
        list_pacotes.append(pacote_id)
if list_pacotes != []:
    for pacote_id in list_pacotes:
        print(pacote_id)
else:
    print('Não existem pacotes de {} com origem na região {}'.format(test_produto,test_regiao))
print('\n')

#-----------------------------------------------------------------------------#
# D - LISTAR PACOTES POR REGIÃO DE DESTINO (PACOTES VÁLIDOS)
for regiao in dict_regioes.values():
    print('PACOTES COM DESTINO A REGIÃO {}'.format(regiao.upper()))
    for pacote_id,pacote in dict_packagesValid.items():
        if pacote.destino ==regiao:
            print(pacote_id)
    print('\n')

#-----------------------------------------------------------------------------#
# E - LISTAR OS PACOTES ENVIADOS POR CADA VENDEDOR (PACOTES VÁLIDOS)
print('NÚMERO DE PACOTES ENTREGUES POR CADA VENDEDOR')
vendedores = {}
for pacote_id,pacote in dict_packagesValid.items():
    try:
        vendedores[pacote.vendedor]
        vendedores[pacote.vendedor] += 1
    except KeyError:
        vendedores[pacote.vendedor] = 1
for vendedor, nPacotes in vendedores.items():
    print('O vendedor {} entregou {} pacotes'.format(vendedor.upper(), str(nPacotes)))
print('\n')

#-----------------------------------------------------------------------------#
# F - LISTA DE PACOTES POR DESTINO E POR TIPO (PACOTES VÁLIDOS)
print('PACOTES POR REGIÃO E TIPO DE PRODUTO')
for regiao in dict_regioes.values():
    for produto in dict_produtos.values():
        test = True
        for pacote_id,pacote in dict_packagesValid.items():
            if pacote.destino == regiao and pacote.produto==produto and test:
                print('Pacotes com {} com destino a região {}'.format(produto,regiao))
                print(pacote_id)
                test = False
            elif pacote.destino == regiao and pacote.produto==produto:
                print(pacote_id)