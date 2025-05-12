import copy
from random import randint, uniform
class Graph:
    def __init__(self, v, e, typo):
        if isinstance(v, Graph):
            self._v =copy.deepcopy(v._v)
            self._e = copy.deepcopy(v._e)
            self._type = copy.copy(v._type)
        else:
            self._v = v
            self._e = copy.deepcopy(e)
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
        for i in self._e[v]:
            if self._type=="veight":
                pass
            else:
                for i in self._e[v]:
                    if use[i]==False:
                        DFS(self, v, use)
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
    def Deicstra(self):
        e=self._e
if __name__=='__main__':
    g=Graph.input_as_vertex_list("j", file="K_5.txt")
    print(g)
