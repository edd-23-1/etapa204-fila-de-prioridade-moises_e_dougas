# -*- coding:UTF-8 -*-
from no import No

class FilaPrioridade:
    """
    Implementação de Fila de Prioridade com Capacidade
    A fila de prioridade a ser implementada deverá ser em ordem crescente
    Os itens com maior prioridade devem ocupar as primeiras posições
    Itens com prioridades iguais devem ser ordenados conforme ordem de inserção
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila de Prioridade com capacidade: {capacidade}")


    # Retorna True se a fila de prioridade está vazia, False caso contrário
    def is_empty(self) -> bool:
        return self.__inicio is None
        # implementação do método
        
    # retorna True se a fila de prioridade está cheia, False caso contrário
    def is_full(self) -> bool:
        return self.__qtdItens == self.__capacidade
        # implementação do método
        
    # Retorna uma referência para o primeiro item da fila de prioridade
    # Caso a lista esteja vazia, retorna None
    def first(self) -> No:
        return self.__inicio
        # implementação do método
        
    # insere um item na fila de prioridade e retorna True, se o item for inserido
    # se a fila de prioridade estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor, prioridade) -> bool:
      if self.is_full():
        raise Exception("A fila de prioridade está cheia.")
      novo_no = No(valor, prioridade)
      if self.is_empty() or prioridade <= self.__inicio.prioridade:
            novo_no.proximo = self.__inicio
            self.__inicio = novo_no
      else:
            no_atual = self.__inicio
            while no_atual.proximo is not None and no_atual.proximo.prioridade <= prioridade:
                no_atual = no_atual.proximo
            novo_no.proximo = no_atual.proximo
            no_atual.proximo = novo_no
      self.__qtdItens += 1
        
      return True
            
        # implementação do método

    # remove o primeiro item da fila de prioridade, caso não esteja vazia, e retorna o Nó
    # se a fila de prioridade estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self) -> No:
        if self.is_empty():
            raise Exception("A fila de prioridades está vazia.")
        no_removido = self.__inicio
        self.__inicio = self.__inicio.proximo
        self.__qtdItens -= 1
        return no_removido
        # implementação do método
        
    # retorna uma lista de tuplas com os itens (valor e prioridade) da fila de prioridade 
    # imprime os itens da fila de prioridade do primeiro para o último
    # caso a fila de prioridade esteja vazia, imprime uma mensagem informando
    # que a fila de prioridade está vazia e retorna uma lista vazia
    def display(self) -> list[tuple()]:
        if self.is_empty():
          if self.is_empty():
            print("A fila de prioridade está vazia.")
            return []
        items = []
        no_atual = self.__inicio
        while no_atual is not None:
            valor_str = str(no_atual.dado)  # Converter para string
            items.insert(0,(valor_str, no_atual.prioridade))
            no_atual = no_atual.proximo
           
        return items      
        # implementação do método
    
    # retorna a quantidade de elementos na fila de prioridade
    # se a fila de prioridade estiver vazia, retorna ZERO
    def size(self) -> int:
        return self.__qtdItens
        