def Floyd(graph,next):
    length = len(graph)

    for i in range(length):
        for j in range(length):

            for k in range(length):

                new_len = graph[i][k] + graph[k][j]
                if graph[i][j] > new_len:
                	graph[i][j] = new_len
                	next[i][j] = next[i][k]

    return graph, next

def Path(next,s,d):
	path = []

	if next[s][d] == float('inf') :
		print('Tidak ada jalan kesana')
		return path
	elif next[s][d] == 0 :
		print('Tidak terdefinisi')
		return path
	else :
		path.append(s)
		while s != d:
			s = next[s][d]
			path.append(s)

	return path

def NextPath(graph):
    path = []
    for a in graph:
        temp = []
        for b in a:
            if b != 0 and b != float('inf') :
                temp.append(a.index(b))
            else :
                temp.append(b)
        path.append(temp)
    return path


if __name__ == '__main__':
    ini = float('inf')
    graph_list = [
        [0,5,ini,10],
        [ini,0,3,ini],
        [ini,ini,0,1],
        [ini,ini,ini,0]
    ]
    path = NextPath(graph_list)  

  
    new_graph, new_path = Floyd(graph_list,path)
    ab=(Path(new_path,1,3))
    print(ab)
    