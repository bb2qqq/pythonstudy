## 图的组成
一个图由两个集合和组成, V - Vertices(单数形式vertex), E - Edges
V里是各个节点。E里是所有节点之间的关系，
V: set([a, b, c, d])
E: set([(a,c), (b,c), (a,d)])

上述的V,E所构成的图G, 用图形化表示就是如下形状：
d--a--c--b

如果我们把E里的关系加上方向，我们就得到了directed graph, 简称digraph.  
图形化表示：
d <- a -> c <- b


