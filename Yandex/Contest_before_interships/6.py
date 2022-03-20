from queue import PriorityQueue
class Graph:
    def __init__(self , N):
        self.size = N
        self.mass =[[-1 for i in range(N)] for i in range(N)]
        self.visited = list()
        # for i in range(N):
        #     self.color.append(0)
    def dijkstra(self , start_vertex):
        D = {v:float('inf') for v in range(self.size)}
        D[start_vertex] = 0

        path_to_vertex = [-1 for i in range(self.size)]

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.size):
                if self.mass[current_vertex][neighbor] != -1:
                    distance = self.mass[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            #print(" nr: " ,neighbor , " cur: ", current_vertex)
                            path_to_vertex[neighbor] = current_vertex
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return path_to_vertex


N = int(input())
dist =[]
for i in range(N):
    x = list(input().split(' '))
    z =[]
    z.append(int(x[0]))
    z.append(int(x[1]))
	#x = [int(x[0]) , int(x[1])]
    dist.append(z)
max_dist = int(input())
first_second = list(input().split(' '))
first = int(first_second[0]) - 1
second = int(first_second[1]) - 1

# print(first , " " ,second)
# print(dist)
# class Edge:
#     def __init__(self , j ,length):
#         self.to = j 
#         self.length = length

graph = Graph(N)
for i in range(N):
    for j in range(i+1, N):
        length = abs( dist[i][0] - dist[j][0]) + abs(dist[i][1] - dist[j][1])
        if(length <= max_dist):
            graph.mass[i][j]= length
            graph.mass[j][i] = length

# for i in range(N):
#     for j in range(N):
#         if(graph.mass[i][j]!= -1):
#             print(i ," -->" , j , " length= " ,graph.mass[i][j] )


mass_path = graph.dijkstra(first)

if mass_path[second] == -1:
    print(-1)
else:
    count = 0
    i = second
    while i != first:
        i = mass_path[i]
        count +=1

    print(count)

# print(graph.dijkstra(0)[1])
