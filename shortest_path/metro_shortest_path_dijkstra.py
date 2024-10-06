from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {} # create a general list for all nodes and vertcies

    def add_vertex(self, vertex): # add vertex if not in list and allocate list for it's neighbors
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2): # add edge (undirected graph)
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print(f'Node {vertex1} or {vertex2} does not exist in graph')

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f'{vertex}: [{self.adjacency_list[vertex]}]\n')

    def bfs (self, start_vertex, end_vertex): # breadth-first search algorithm (find shortest path)
        visited = set() # list of visited nodes (optimization)
        queue = deque([start_vertex]) # add first element so start queue from
        visited.add(start_vertex) 
        distances = {start_vertex: 0}
        paths = {start_vertex: [start_vertex]} 

        while queue: 
            current_vertex = queue.popleft() 

            if current_vertex == end_vertex:
                return distances[end_vertex], paths[end_vertex]

            for neighbor in self.adjacency_list[current_vertex]: # go through all neighbors for curr node
                if neighbor not in visited: 
                    visited.add(neighbor)
                    queue.append(neighbor)
                    distances[neighbor] = distances[current_vertex] + 1 # update distance for neighbor 
                    paths[neighbor] = paths[current_vertex] + [neighbor] # update path to the neighbor
        return float('inf'), [] 
        
    """
    Diijkstra's algorithm for searching the shortest distances to every node in weighted graph.
    To restore the path we'll use a simple approach of subtraction distance to node and edge weight
    and compare the result with distance to node and if it matches add to the path.

    Need to reinsert data with weights for every edge 
    now e.g.: {'A': {'B', 'C', ...}, ...} -> {'A':{'B':1, 'C':2, ...}, ...}
    """        

    def dijkstra(self, start_vertex): #FIXME

        distances = {node: float('inf') for node in self.adjacency_list} # inf distances to replace with any shorter
        distances[start] = 0 # start vertex is 0 distance

        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            for neighbor, weight in self.adjacency_list[current_node].items(): # {'A':{'B':2, 'C':3, ...}, ...}
                distance = distances[current_node] + weight # update distance with cur_dist + weight

                if distance < distances[neighbor]: # if new distance less than in list, than update
                    distances[neighbor] = distance # and add this node to queue to process
                    queue.append(neighbor)

        return distances


def insert_data(graph):
# Red Link
    graph.add_vertex("Haje")
    graph.add_vertex("Opatov")
    graph.add_vertex("Chodov")
    graph.add_vertex("Roztyly")
    graph.add_vertex("Kacerov")
    graph.add_vertex("Budejovicka")
    graph.add_vertex("Pankrac")
    graph.add_vertex("Vysehrad")
    graph.add_vertex("IP Pavlova")
    graph.add_vertex("Hlavni Nadrazi")
    graph.add_vertex("Vltavska")
    graph.add_vertex("Nadrazi Holesovice")
    graph.add_vertex("Kobylisy")
    graph.add_vertex("Ladvi")
    graph.add_vertex("Strizkov")
    graph.add_vertex("Prosek")
    graph.add_vertex("Letnany")

    # Green Link
    graph.add_vertex("Dejvicka")
    graph.add_vertex("Hradcanska")
    graph.add_vertex("Malostranska")
    graph.add_vertex("Staromestska")
    graph.add_vertex("Namesti Miru")
    graph.add_vertex("Jiriho z Podebrad")
    graph.add_vertex("Flora")
    graph.add_vertex("Zelivskeho")
    graph.add_vertex("Strasnicka")
    graph.add_vertex("Skalka")
    graph.add_vertex("Depo Hostivar")

    # Yellow link
    graph.add_vertex("Zlicin")
    graph.add_vertex("Stodulky")
    graph.add_vertex("Luka")
    graph.add_vertex("Luziny")
    graph.add_vertex("Hurka")
    graph.add_vertex("Nove Butovice")
    graph.add_vertex("Jinonice")
    graph.add_vertex("Radlicka")
    graph.add_vertex("Smichovske nadrazi")
    graph.add_vertex("Andel")
    graph.add_vertex("Karlovo Namesti")
    graph.add_vertex("Narodni trida")
    graph.add_vertex("Namesti Republiky")
    graph.add_vertex("Krizkova")
    graph.add_vertex("Invalidovna")
    graph.add_vertex("Palmovka")
    graph.add_vertex("Ceskomoravska")
    graph.add_vertex("Vysocanska")
    graph.add_vertex("Kolbenova")
    graph.add_vertex("Hloubetin")
    graph.add_vertex("Rajska zahrada")
    graph.add_vertex("Cerny Most")

    # Connected links
    graph.add_vertex("Mustek")
    graph.add_vertex("Florenc")
    graph.add_vertex("Muzeum")

    # Edges
    # Red edges
    graph.add_edge("Haje", "Opatov")
    graph.add_edge("Opatov", "Chodov")
    graph.add_edge("Chodov", "Roztyly")
    graph.add_edge("Roztyly", "Kacerov")
    graph.add_edge("Kacerov", "Budejovicka")
    graph.add_edge("Budejovicka", "Pankrac")
    graph.add_edge("Pankrac", "Vysehrad")
    graph.add_edge("Vysehrad", "IP Pavlova")
    graph.add_edge("IP Pavlova", "Muzeum")
    graph.add_edge("Muzeum", "Hlavni Nadrazi")
    graph.add_edge("Hlavni Nadrazi", "Florenc")
    graph.add_edge("Florenc", "Vltavska")
    graph.add_edge("Vltavska", "Nadrazi Holesovice")
    graph.add_edge("Nadrazi Holesovice", "Kobylisy")
    graph.add_edge("Kobylisy", "Ladvi")
    graph.add_edge("Ladvi", "Strizkov")
    graph.add_edge("Strizkov", "Prosek")
    graph.add_edge("Prosek", "Letnany")

    # Yellow edges
    graph.add_edge("Zlicin", "Stodulky")
    graph.add_edge("Stodulky", "Luka")
    graph.add_edge("Luka", "Luziny")
    graph.add_edge("Luziny", "Hurka")
    graph.add_edge("Hurka", "Nove Butovice")
    graph.add_edge("Nove Butovice", "Jinonice")
    graph.add_edge("Jinonice", "Radlicka")
    graph.add_edge("Radlicka", "Smichovske nadrazi")
    graph.add_edge("Smichovske nadrazi", "Andel")
    graph.add_edge("Andel", "Karlovo Namesti")
    graph.add_edge("Karlovo Namesti", "Narodni trida")
    graph.add_edge("Narodni trida", "Mustek")
    graph.add_edge("Mustek", "Namesti Republiky")
    graph.add_edge("Namesti Republiky", "Florenc")
    graph.add_edge("Florenc", "Krizkova")
    graph.add_edge("Krizkova", "Invalidovna")
    graph.add_edge("Invalidovna", "Palmovka")
    graph.add_edge("Palmovka", "Ceskomoravska")
    graph.add_edge("Ceskomoravska", "Vysocanska")
    graph.add_edge("Vysocanska", "Kolbenova")
    graph.add_edge("Kolbenova", "Hloubetin")
    graph.add_edge("Hloubetin", "Rajska zahrada")
    graph.add_edge("Rajska zahrada", "Cerny Most")

    # Green edges
    graph.add_edge("Dejvicka", "Hradcanska")
    graph.add_edge("Hradcanska", "Malostranska")
    graph.add_edge("Malostranska", "Staromestska")
    graph.add_edge("Staromestska", "Mustek")
    graph.add_edge("Mustek", "Muzeum")
    graph.add_edge("Muzeum", "Namesti Miru")
    graph.add_edge("Namesti Miru", "Jiriho z Podebrad")
    graph.add_edge("Jiriho z Podebrad", "Flora")
    graph.add_edge("Flora", "Zelivskeho")
    graph.add_edge("Zelivskeho", "Strasnicka")
    graph.add_edge("Strasnicka", "Skalka")
    graph.add_edge("Skalka", "Depo Hostivar")

def main():
    graph = Graph()
    
    insert_data(graph)    

    start_station = str(input("\nEnter the landing  station -> "))
    end_station = str(input("Enter the destination station -> "))
    distance, path = graph.bfs(start_station, end_station)
    print(f'\nDistance between {start_station} and {end_station}: {distance} stations\n')
    print(f'Your route from {start_station} to {end_station}: {path}\n')
 

if __name__ == "__main__":
    main()


