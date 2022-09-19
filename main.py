import os
#file reader

def adicionaBasedados(g):

    path = "Amostra Enron - 2016"
    a = os.listdir("Amostra Enron - 2016")
    path += "\\"
    for i in a:
        path2 = path+i
        b = os.listdir(path2)
        for j in b:
            path3 = path2 + "\\" + j
            c = os.listdir(path3)
            for k in c:
                pathfile = path3 + "\\" + k
                if k == "requests":
                    break
                if k == "junk_file":
                    break
                file = open(pathfile, 'r')
                x = file.readline()
                enviadopor = ""
                recebidopor = ""
                acheienviado = False
                acheirecebido = False
                print(pathfile)
                while True:
                    y = x.split()
                    if y==[]:
                        break
                    if y[0] == "From:":
                        enviadopor = y[1]
                        acheienviado = True
                    if y[0] == "To:":
                        if file.readline().split()[0] == "Subject:":
                            recebidopor = y[1]
                            if acheienviado:
                                acheirecebido = True
                            break
                    x = file.readline()
                if acheirecebido:
                    g.adiciona_vertice(enviadopor)
                    g.adiciona_vertice(recebidopor)
                    g.adiciona_aresta(enviadopor,recebidopor,1)


from collections import defaultdict


class Grafo:
    # construtor
    def __init__(self):
        self.lista_adjacencia = defaultdict(list)
        self.vertices = []

    # verifica se u e v são adjacêntes
    def tem_aresta(self, u, v):
        # verifica se u e v já são vertices adicionados
        if all(x in self.vertices for x in [u, v]):
            # verifica se u e v são adjacentes
            for adj in self.lista_adjacencia[u]:
                if adj[0] == v:
                    return True
            return False
        else:
            return False

    # adiciona um vértice u
    def adiciona_vertice(self, u):
        # se u não foi adicionado, então pode ser adicionado
        if u not in self.vertices:
            self.vertices.append(u)
            self.lista_adjacencia[u] = []

    # adiciona uma aresta entre u e v
    def adiciona_aresta(self, u, v, peso):
        nao_achou = True
        # verifica se os vertices existem
        if self.tem_aresta(u,v):
            nao_achou = False
            # se não existe, ele adiciona, caso contrário não adiciona
        if (nao_achou):
            self.lista_adjacencia[u].append((v, peso))
        else:
            print(self.lista_adjacencia)
            for i in range(len(self.lista_adjacencia[u])):
                print(u)
                print(v)
                print(i)
                print(self.lista_adjacencia[u][i][0])
                if self.lista_adjacencia[u][i][0] == v:
                    peso += self.lista_adjacencia[u][i][1]
                    self.lista_adjacencia[u].remove(self.lista_adjacencia[u][i])
            self.lista_adjacencia[u].append((v, peso))

    def remove_aresta(self, u, v):
        remover = None
        # verifica se u e v são adjacêntes
        if self.tem_aresta(u, v):
            # procura pela adjacência
            for adj in range(len(self.lista_adjacencia[u])):
                if self.lista_adjacencia[u][adj][0] == v:
                    remover = self.lista_adjacencia[u][adj]
            # remove a adjacência
            self.lista_adjacencia[u].remove(remover)
        else:
            print("Aresta não removida")

    def remove_vertice(self, u):
        # verifica se u é um vértice adicionado
        if u in self.vertices:
            # remove o vértice
            self.lista_adjacencia.pop(u)
            self.vertices.remove(u)
            # remove adjacências existentes entre outros vértices e u
            for vertice in self.lista_adjacencia:
                for adj in self.lista_adjacencia[vertice]:
                    if adj[0] == u:
                        self.lista_adjacencia[vertice].remove(adj)
        else:
            print(f"os vértice {u} não foi adicionado")

    def peso(self, u, v):
        achou = False
        # verifica se u e v são vértices
        if all(x in self.vertices for x in [u, v]):
            # procura a a adjacência
            for adj in self.lista_adjacencia[u]:
                # printa o peso entre os 2
                if adj[0] == v:
                    print(f'o peso entre {u} e {v} é {adj[1]}')
                    achou = True
            # caso não há adjacência, printa que não existe adjacência
            if not achou:
                print(f"{u} e {v} não são adjacentes")
        else:
            print(f"os vértices {u} ou {v} não foram adicionados")

    def grau(self, u):
        # verifica se u é vértice
        if u in self.vertices:
            # verifica grau de saida
            grau_saida = len(self.lista_adjacencia[u])
            print(f'{u} tem grau de saida {grau_saida}')
            grau_entrada = 0
            # verifica grau de saida
            for vertice in self.lista_adjacencia:
                for adj in self.lista_adjacencia[vertice]:
                    if adj[0] == u:
                        grau_entrada += 1
            print(f'{u} tem grau de entrada {grau_entrada}')
            print(f'{u} tem grau {grau_entrada + grau_saida}')

        else:
            print(f"os vértice {u} não foi adicionado")

    def imprime_lista_adjacencias(self):
        # imprime vertice
        print(self.lista_adjacencia)
        for vertice in self.lista_adjacencia:
            print(f'{vertice}: ', end='')
            # imprime adjacências
            for adj in self.lista_adjacencia[vertice]:
                print(f'{adj} -> ', end='')
            print(' ')

    def dfs(self, u):
        visitados = []
        pilha = []
        pilha.append(u)
        while pilha:
            s = pilha.pop()
            if s not in visitados:
                visitados.append(s)
                for x in self.lista_adjacencia[s][::-1]:
                    if x not in visitados:
                        pilha.append(x[0])
        return visitados

    def dfs_parada(self, u, destino):
        visitados = []
        pilha = []
        pilha.append(u)
        while pilha:
            s = pilha.pop()
            if s not in visitados:
                visitados.append(s)
                for x in self.lista_adjacencia[s][::-1]:
                    if x[0] not in visitados:
                        pilha.append(x[0])
                        if x[0] == destino:
                            visitados.append(destino)
                            return visitados
        return visitados

    def bfs(self, u):
        visitados = []
        lista = []
        lista.append(u)
        while lista:
            s = lista.pop(0)
            if s not in visitados:
                visitados.append(s)
                for x in self.lista_adjacencia[s]:
                    if x not in visitados:
                        lista.append(x[0])
        return visitados

g = Grafo()
adicionaBasedados(g)
g.imprime_lista_adjacencias()
