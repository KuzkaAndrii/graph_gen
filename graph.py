import copy
import numpy as np
from itertools import permutations
import tkinter as tk
from random import randint, uniform
class Graph:
    def __init__(self, v, e, typo):
        if isinstance(v, Graph):
            self._v =copy.deepcopy(v._v)
            self._e = copy.deepcopy(v._e)
            self._n_e=copy.deepcopy(v._n_e)
            self._type = copy.copy(v._type)
        else:
            self._v = v
            self._e = copy.deepcopy(e)
            s=0
            for i in e:
                s+=len(i)
            self._n_e=s
            self._type = copy.deepcopy(typo)
    def graph_gen(self, vn, en, typo):
        v=vn
        e=[]
        for i in range(vn+1):
            e.append([])
        for i in range(en):
            a, b=randint(1, vn), randint(1, vn)
            if typo == "orgraph":
                e[a].append(b)
            elif typo == "veight":
                l=uniform(0.0001, 10)
                e[a].append((b, l))
                e[b].append((a, l))
            else:
                e[a].append(b)
                e[b].append(a)
        return Graph(v, e, typo)
    def DFS(self, v, use):
        use[v]=True
        #print(use, v)
        for i in self._e[v]:
            if self._type=="veight":
                for i in self._e[v]:
                    if use[i[0]] == False:
                        self.DFS(i[0], use)
                        return
            else:
                for i in self._e[v]:
                    if use[i]==False:
                        self.DFS(i, use)
                        return
        return
    def visualize(self):
        pass
    @staticmethod
    def input_as_vertex_list(typo, file=None):
        if file!=None:
            fi=open(file)
            v, m = map(int, fi.readline().split())
            e = []
            for i in range(v + 1):
                e.append([])
            for i in range(m):
                if typo == "veight":
                    s, f, m = map(float, fi.readline().split())
                    s, f = int(s), int(f)
                    e[s].append((f, m))
                    e[f].append((s, m))
                else:
                    s, f = map(int, fi.readline().split())
                    if typo == "orgraph":
                        e[s].append(f)
                    else:
                        e[s].append(f)
                        e[f].append(s)
            fi.close()
            return Graph(v, e, typo)

        else:
            v, m=map(int, input().split())
            e=[]
            for i in range(v+1):
                e.append([])
            for i in range(m):
                if typo=="veight":
                    s, f, m=map(float, input().split())
                    s, f=int(s), int(f)
                    e[s].append((f, m))
                    e[f].append((s, m))
                else:
                    s, f=map(int, input().split())
                    if typo=="orgraph":
                        e[s].append(f)
                    else:
                        e[s].append(f)
                        e[f].append(s)
            return Graph(v, e, typo)
    def __str__(self):
        print(self._v)
        for i in range(1, self._v+1):
            print(*self._e[i])
        return ""
    def Deicstra(self, s, s1):
        use=[False for i in range(self._v+1)]
        d=[-1.0 for i in range(self._v+1)]
        d[s]=0
        for i in range(1, self._v+1):
            corect_v=0
            for v in range(1, self._v+1):
                if (d[v]<d[corect_v] and d[v]>=0) or d[corect_v]==-1.0:
                    if use[v]==False:
                        corect_v=v
            use[corect_v]=True
            for e in self._e[corect_v]:
                if d[corect_v]>=0 and d[e[0]]>=0:
                    d[e[0]]=min(d[e[0]], d[corect_v]+e[1])
                else:
                    d[e[0]]=e[1]
        #print(d)
        return d[s1]
    def test_func(self):
        self.Deicstra(1, 3)
        return
    def is_together(self):
        use=[False for i in range(1, self._v+1)]
        self.DFS(1, use)
        for i in range(1, self._v):
            if not use[i]:
                return False
        return True
    def search_shortest_way(self, s, f):
        if self._type=='veight':
            res=self.Deicstra(s, f)
            return res
        else:
            return False

if __name__=='__main__':
    print()
