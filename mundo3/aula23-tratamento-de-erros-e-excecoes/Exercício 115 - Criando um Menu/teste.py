"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from time import sleep
from ex115.uteis import interface
from ex115.uteis import verificacao
from ex115.uteis import arquivo


# Programa Principal

nome_arquivo = 'ex115-pessoas.txt'

arquivo.createF(nome_arquivo)
status = 1 # ligado
while status != 0: # enquanto status nõa for desligado
    # Print Menu Principal e Opções
    interface.titulo('MENU PRINCIPAL', '=')
    quant_opcoes = interface.menuOpcoes(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']) # quant_opcoes do menu opções

    # Loop da escolha da opção
    escolha = verificacao.vOpcao(quant_opcoes)
    match escolha:
        case 1: # Ver pessoas cadastradas
            interface.titulo(f'OPÇÃO {escolha}', '~')
            arquivo.readF(nome_arquivo)
            
        case 2: # Cadastrar nova Pessoa
            interface.titulo(f'OPÇÃO {escolha}', '~')

            
        case 3: # Sair do Sistema
            interface.titulo('Saindo do Sistema... Até logo!', '~')
            status = 0
