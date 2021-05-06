from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


# Funções

def main() -> None:
    head()
    menu()

def menu() -> None:
    print('@:::::::::::::::::::::::::::::::::@')
    print('@:::::: MINI MERCADO 76 ::::::::::@')
    print('@::::::::::: SHOP ::::::::::::::::@')
    print('@:::::::::::::::::::::::::::::::::@')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('>>>>>>>> Saindo e encerrando >>>>>>>>')
        print('Até mais')
        sleep(2)
        exit(0)
    else:
        print('Digite uma opção valida!')
        menu()



def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso !!!')


def listar_produtos() -> None:
    pass

def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    pass

def pega_produto_por_codigo(codigo: int) -> None:
    pass

def head() -> None:
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@>>>>>>>>< BEM-VINDO(a) ><<<<<<<<<@')
    print('@>>>>>>>>>< WELCOME ><<<<<<<<<<<<<@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    sleep(1)

if __name__ == '__main__':
    main()


