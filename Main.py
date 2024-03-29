from Grafo import *
print("-----------------------------------------------------Construcao de Grafos----------------------------------------------------")
print('1 - Criar grafo')
print('2 - Printar grafo')
print('3 - Printar Grafo (Destino, Origem)')
print('4 - Busca em profundidade')
print('5 - Busca em largura')
print('0 - Exit')
op = int(input('Digite a opcao: '))

grafo = Grafo(False)

while op != 0:
    if op == 1:
        print('Digite a quantidade de vertices ')
        vertices = int(input())
        for i in range(vertices):
            print('Digite o identificador dos vertices: ')
            id = input('')
            vert = Vertice(id)
            grafo.lista_Vertices.append(vert)
        print('Digite a quantidade de arestas: ')
        arestas = int(input(''))
        for k in range(arestas):
            print("Digite o id do vertice de origem e o id do vertice de destino, juntamente com o peso ex:(A B 15)")
            entrada = input().split(' ')
            grafo.nova_Aresta(entrada[0],entrada[1],int(entrada[2]))
    elif op == 2:
        temp = ''
        for k in range(len(grafo.lista_Vertices)):
            print(grafo.lista_Vertices[k].getId()+' fazendo aresta com:')
            for i in range(len(grafo.lista_Arestas)):
                if grafo.lista_Vertices[k].getId() == grafo.lista_Arestas[i].getOrigem().getId():
                    print('    '+grafo.lista_Arestas[i].getDestino().getId()+' com peso: '+str(grafo.lista_Arestas[i].getPeso()))
    elif op == 3:
        origem = input('Digite o id da origem: ')
        destino = input('Digite o id do destino: ')
        grafo.imprime_Grafo_com_Destino(origem,destino)
    elif op == 4:
        grafo.Depth_first_search()
    elif op == 5:
        id = input('Digite o identificador do vertice: ')
        grafo.Breadth_first_search(id)
    print("-----------------------------------------------------Construcao de Grafos----------------------------------------------------")
    print('1 - Criar grafo')
    print('2 - Printar grafo')
    print('3 - Printar Grafo (Destino, Origem) (Necessita realizar busca em profundidade antes)')
    print('4 - Busca em profundidade')
    print('5 - Busca em largura')
    print('0 - Exit')
    op = int(input('Digite a opcao: '))