import copy
from random import uniform, randint
from itertools import permutations

import numpy as np


class Vertex:
    def __init__(self, id):
        self._id = id
        self._x = uniform(-10.0, 10.0)
        self._y = uniform(-10.0, 10.0)


class Edge:
    def __init__(self, s, f, w=1):
        self._s = s
        self._f = f
        self._w = w #weight of edge
        self._char = None


class MetaGraph:
    def __init__(self, list_v, list_e, _type):

        #main abilities of vertexes
        self._v_ids = self.__get_ids(list_v)
        self._v_x = self.__get_cord_x(list_v)
        self._v_y = self.__get_cord_y(list_v)

        #main abilities of edges
        a, b, c = self.__get_edge_list_and_weight_list_and_Dedge_list(list_v, list_e, _type)
        self._edge_list = copy.deepcopy(a)
        self._weight_list = copy.deepcopy(b)
        self._dedge_list = copy.deepcopy(c)
        self._gen_weight = self.__get_gen_weight(list_e)
        self.__set_char(list_v, list_e, _type)


    def __get_ids(self, list_v):
        n = len(list_v)
        res = np.zeros(n+1, dtype=int)
        i = 1
        for v in list_v:
            res[i]=v._id
            i+=1
        return res


    def __get_cord_x(self, list_v):
        n = len(list_v)
        res = np.zeros(n + 1)
        i = 1
        for v in list_v:
            res[i] = v._x
            i+=1
        return res


    def __get_cord_y(self, list_v):
        n = len(list_v)
        res = np.zeros(n + 1)
        i = 1
        for v in list_v:
            res[i] = v._y
            i += 1
        return res


    def __get_edge_list_and_weight_list_and_Dedge_list(self, list_v, list_e, _type):
        nv = len(list_v)
        res=[]
        res_weight=[]
        res_dedge=[]
        for i in range(nv+1):
            res.append([])
            res_weight.append([])
            res_dedge.append([])
        for e in list_e:
            res[e._s].append(e._f)
            res_weight[e._s].append(e._w)
            res_dedge[e._s].append(e)
            if _type!='orgraph':
                res[e._f].append(e._s)
                res_weight[e._f].append(e._w)
                res_dedge[e._f].append(e)
        return res, res_weight, res_dedge


    def __get_gen_weight(self, list_e):
        res = 2
        for e in list_e:
            res = max(e._w+1, res)
        return res


    def __set_char(self, list_v, list_e, _type):
        n = len(list_v)
        for e in list_e:
            res = np.zeros(n+1)
            if _type=='weight':
                res[e._s] = e._w
                res[e._f] = e._w
            elif _type=='orgraph':
                res[e._s] = -1
                res[e._f] = 1
            else:
                res[e._s] = 1
                res[e._f] = 1
            e._char = res
        return


class Graph(MetaGraph):
    def __init__(self, list_v, list_e, _type):
        super().__init__(list_v, list_e, _type)
        self.list_v=list_v
        self.list_e=list_e
        self.type=_type

    #повертає матрицю інцидентності
    def get_inc_matr(self):
        sub_res=[]
        for e in self.list_e:
            sub_res.append(e._char)
        res=np.array(sub_res)
        return res[:, 1:]


    def DFS(self, v, use):
        use[v] = True
        print(use)
        for i in self._edge_list[v]:
            for i in self._edge_list[v]:
                if use[i] == False:
                    self.DFS(i, use)
                    return
        return


    def Dijkstra(self, s, f):
        ways = dict()
        for v in self._v_ids:
            ways[v]=[v]
        use = [False for i in range(len(self.list_v) + 1)]
        d = [self._gen_weight] * (len(self.list_v) + 1)
        d[s] = 0
        for j in self._v_ids[1:]:
            corect_v = 0
            for v in self._v_ids[1:]:
                if d[v] < d[corect_v]:
                    if use[v] == False:
                        corect_v = v
            use[corect_v] = True
            for i in range(len(self._edge_list[corect_v])):
                if d[self._edge_list[corect_v][i]]>=d[corect_v] + self._weight_list[corect_v][i]:
                    d[self._edge_list[corect_v][i]]=d[corect_v] + self._weight_list[corect_v][i]
                    ways[self._edge_list[corect_v][i]]=copy.deepcopy(ways[corect_v])
                    ways[self._edge_list[corect_v][i]].append((corect_v, i))
                    ways[self._edge_list[corect_v][i]].append(self._edge_list[corect_v][i])
        return d[f], ways.get(f)


    def is_conected(self):
        use = [False for i in range(len(self.list_v) + 1)]
        self.DFS(1, use)
        for i in range(1, len(self.list_v) + 1):
            if not use[i]:
                return False
        return True


    def print_graph(self, way=None):
        if way!=None:
            f=open(way, 'wt')
            print(len(self.list_v), len(self.list_e), self.type, file=f)
            for e in self.list_e:
                if self.type=='weight':
                    print(e._s, e._f, e._w, file=f)
                else:
                    print(e._s, e._f, file=f)
            f.close()
        else:
            print(len(self.list_v), len(self.list_e), self.type)
            for e in self.list_e:
                if self.type == 'weight':
                    print(e._s, e._f, e._w)
                else:
                    print(e._s, e._f)


    @staticmethod
    def input_graph(way):
        f = open(way)
        list_v = []
        list_e = []
        nv, ne, type_ = f.readline().split()
        nv = int(nv)
        ne = int(ne)
        for i in range(nv):
            list_v.append(Vertex(i+1))
        for i in range(ne):
            if type_ == 'weight':
                st, fn, weight = map(float, f.readline().split())
                st, fn = int(st), int(fn)
                e = Edge(st, fn, w=weight)
                list_e.append(e)
            else:
                st, fn = map(int, f.readline().split())
                e = Edge(st, fn)
                list_e.append(e)
        f.close()
        result_graph=Graph(list_v, list_e, type_)
        return result_graph


    def has_subgraph(self, g):
        if g.type != self.type:
            return False
        if len(g.list_v)>len(self.list_v):
            return False
        if len(g.list_e)>len(self.list_e):
            return False

        self_matr = self.get_inc_matr()
        g_matr = g.get_inc_matr()

        el = list(range(self_matr[:, 0].size))
        vl = list(range(self_matr[0].size))
        for ind_e in permutations(el):
            for ind_v in permutations(vl):
                np_ind_e = np.array(ind_e)
                np_ind_v = np.array(ind_v)

                new_matr = self_matr[np_ind_e]
                new_matr = new_matr[np.array(range(len(g.list_e)))]
                new_matr = new_matr.T
                new_matr = new_matr[np_ind_v]
                new_matr = new_matr[np.array(range(len(g.list_v)))]
                new_matr = new_matr.T
                try:
                    #print(type(new_matr), type(g_matr))
                    A=np.array(new_matr)
                    B=np.array(g_matr)
                    #print(A)
                    #print(B)
                    #print('-----------------')
                    res = np.array_equal(A, B)

                    if res:
                        return True
                except:
                    print(type(new_matr), type(g_matr))
        return False


    @staticmethod
    def gen_graph(nv, ne, type_):
        list_v = []
        list_e = []
        for i in range(nv):
            list_v.append(Vertex(i+1))
        for i in range(ne):
            st = randint(1, nv)
            fn = randint(1, nv)
            weight = 1
            if type_=='weight':
                weight=uniform(0.0, 100.0)
            e = Edge(st, fn, w=weight)
            list_e.append(e)
        result_graph = Graph(list_v, list_e, type_)
        return result_graph




if __name__=="__main__":
    g = Graph.input_graph('good_graph.txt')
    d, way=g.Dijkstra(1, 4)

    print(way)