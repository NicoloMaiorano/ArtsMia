import networkx as nx

from database.DAO import DAO

class Model:
    def __init__(self):
        self._objects = DAO.getAllObjects()
        self._artists = DAO.getAllArtists()
        self._exhibitions = DAO.getAllExhibitions()
        self._grafo = nx.Graph()
        self.idMap = {}

        for o in self._objects:
            self.idMap[o.object_id] = o

    def allObjects(self):
        return self._objects

    def allArtist(self):
        return self._artists

    def allExhibitions(self):
        return self._exhibitions

    def buildGraph(self):
        self._grafo.add_nodes_from(self._objects)
        self.addAllEdges()

    def addEdgesV1(self):
        for u in self._objects:
            for v in self._objects:
                peso = DAO.getPeso(u,v)
                if (peso != None):
                    self._grafo.add_edge(u,v, weight= peso)

    def addAllEdges(self):
        allEdges = DAO.getAllArchi(self.idMap)

        for e in allEdges:
            self._grafo.add_edge(e.o1, e.o2, weight= e.peso)

    def getIdMap(self):
        return self.idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getInfoConnessa(self, idInput):
        """"Identifica la componente connessa che contiene idInput e ne restituisce la dimensione"""

        source = self.idMap[idInput]

        #modo 1: conto i successori
        succ = nx.dfs_successors(self._grafo, source).values()

        res = []
        #perchè nx.dfs_successors() contiene solo le key del dizionario e non considera le cose dentro alla lista corrispondente a quella key
        #quindi devo fare una lista nuova e inserire anche tutti i valori che trovo per ogni key
        for s in succ:
            res.extend(s)

        #is_connected(grafo) restituisce True se il grafo è connesso
        #number_connected_components(grafo) restituisce il numero di componenti connesse
        #connected_components(grafo) restituisce le componenti connesse
        #node_connected_components(grafo, nodo) restituisce il set di nodi della componente connessa che contiene il nodo

        print("Size connessa con modo 1: ", len(res))

        #modo 2: conto i predecessori
        pred = nx.dfs_predecessors(self._grafo, source)
        print("Size connessa con modo 2: ", len(pred.values()))

        #modo 3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, source)
        print("Modo 3: ", len(tree.nodes()))

        #modo 4: uso il metodo di networkx

        conn = nx.node_connected_component(self._grafo, source)
        print("Modo 4: ", len(conn))

        return len(conn)

    def getObjectById(self, idInput):
        return self.idMap[idInput]
    def hasNode(self, idInput):
        return idInput in self.idMap