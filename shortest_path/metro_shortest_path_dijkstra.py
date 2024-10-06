from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {} # create a general list for all nodes and vertcies

    def add_vertex(self, vertex): # add vertex if not in list and allocate list for it's neighbors
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {} 

    def add_edge(self, vertex1, vertex2, weight): # add edge (undirected graph)
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].update({vertex2:weight}) # {'A':{'B':1, 'C':2, ...}, ...}
            
            self.adjacency_list[vertex2].update({vertex1:weight})
        else:
            print(f'Node {vertex1} or {vertex2} does not exist in graph')

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f'{vertex}: [{self.adjacency_list[vertex]}]\n')


    def dijkstra(self, start_vertex):

        distances = {node: float('inf') for node in self.adjacency_list} # inf distances to replace with any shorter
        distances[start_vertex] = 0 # start vertex is 0 distance

        queue = deque([start_vertex])

        while queue:
            current_node = queue.popleft()

            for neighbor, weight in self.adjacency_list[current_node].items(): # {'A':{'B':2, 'C':3, ...}, ...}
                distance = distances[current_node] + weight # update distance with cur_dist + weight

                if distance < distances[neighbor]: # if new distance less than in list, than update
                    distances[neighbor] = distance # and add this node to queue to process
                    queue.append(neighbor)

        return distances

    """
    Need to restore the path and output the whole path
    """

    def shortest_path(self, distances, start_vertex, end_vertex):

        shortest_path = [end_vertex]
        dist = distances[end_vertex]
        current_vertex = end_vertex

        while dist > 0:
            for neighbor, edge_weight in self.adjacency_list[current_vertex].items():
                if dist - edge_weight == distances[neighbor]:
                    dist -= edge_weight
                    current_vertex = neighbor
                    shortest_path.append(neighbor)
        
        return shortest_path


def insert_data(graph):
# Red Link
    graph.add_vertex("Haje")
    graph.add_vertex("Opatov")
    graph.add_vertex("Chodov")
    graph.add_vertex("Roztyly")
    graph.add_vertex("Kacerov")
    graph.add_vertex("Budejovicka")
    graph.add_vertex("Pankrac")
    graph.add_vertex("Prazskeho povstani")
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
    graph.add_edge("Haje", "Opatov", 3)
    graph.add_edge("Opatov", "Chodov", 3)
    graph.add_edge("Chodov", "Roztyly", 2)
    graph.add_edge("Roztyly", "Kacerov", 3)
    graph.add_edge("Kacerov", "Budejovicka", 2)
    graph.add_edge("Budejovicka", "Pankrac", 2)
    graph.add_edge("Pankrac", "Prazskeho povstani", 2)
    graph.add_edge("Prazskeho povstani", "Vysehrad", 2)
    graph.add_edge("Vysehrad", "IP Pavlova", 3)
    graph.add_edge("IP Pavlova", "Muzeum", 1)
    graph.add_edge("Muzeum", "Hlavni Nadrazi", 1)
    graph.add_edge("Hlavni Nadrazi", "Florenc", 2)
    graph.add_edge("Florenc", "Vltavska", 2)
    graph.add_edge("Vltavska", "Nadrazi Holesovice", 2)
    graph.add_edge("Nadrazi Holesovice", "Kobylisy", 6)
    graph.add_edge("Kobylisy", "Ladvi", 2)
    graph.add_edge("Ladvi", "Strizkov", 2)
    graph.add_edge("Strizkov", "Prosek", 2)
    graph.add_edge("Prosek", "Letnany", 2)

    # Yellow edges
    graph.add_edge("Zlicin", "Stodulky", 3)
    graph.add_edge("Stodulky", "Luka", 2)
    graph.add_edge("Luka", "Luziny", 1)
    graph.add_edge("Luziny", "Hurka", 2)
    graph.add_edge("Hurka", "Nove Butovice", 1)
    graph.add_edge("Nove Butovice", "Jinonice", 3)
    graph.add_edge("Jinonice", "Radlicka", 3)
    graph.add_edge("Radlicka", "Smichovske nadrazi", 4)
    graph.add_edge("Smichovske nadrazi", "Andel", 2)
    graph.add_edge("Andel", "Karlovo Namesti", 2)
    graph.add_edge("Karlovo Namesti", "Narodni trida", 1)
    graph.add_edge("Narodni trida", "Mustek", 1)
    graph.add_edge("Mustek", "Namesti Republiky", 2)
    graph.add_edge("Namesti Republiky", "Florenc", 1)
    graph.add_edge("Florenc", "Krizkova", 2)
    graph.add_edge("Krizkova", "Invalidovna", 2)
    graph.add_edge("Invalidovna", "Palmovka", 2)
    graph.add_edge("Palmovka", "Ceskomoravska", 3)
    graph.add_edge("Ceskomoravska", "Vysocanska", 2)
    graph.add_edge("Vysocanska", "Kolbenova", 2)
    graph.add_edge("Kolbenova", "Hloubetin", 3)
    graph.add_edge("Hloubetin", "Rajska zahrada", 4)
    graph.add_edge("Rajska zahrada", "Cerny Most", 2)

    # Green edges
    graph.add_edge("Dejvicka", "Hradcanska", 2)
    graph.add_edge("Hradcanska", "Malostranska", 2)
    graph.add_edge("Malostranska", "Staromestska", 2)
    graph.add_edge("Staromestska", "Mustek", 2)
    graph.add_edge("Mustek", "Muzeum", 1)
    graph.add_edge("Muzeum", "Namesti Miru", 2)
    graph.add_edge("Namesti Miru", "Jiriho z Podebrad", 2)
    graph.add_edge("Jiriho z Podebrad", "Flora", 2)
    graph.add_edge("Flora", "Zelivskeho", 2)
    graph.add_edge("Zelivskeho", "Strasnicka", 3)
    graph.add_edge("Strasnicka", "Skalka", 3)
    graph.add_edge("Skalka", "Depo Hostivar", 2)


def estim_time(graph, start_station, end_station): #FIXME
    """
    Every edge has a weight, which represents amount of segments 500m long. 
    For example, if edge has a weight 3 than a distance between 2 stations = 3*500=1500m=1.5km
    """
    avg_speed = 11 # average speed of metro in Prague ~ 40 km/h ~ 11 m/


def main():
    graph = Graph()
    
    insert_data(graph)    

    start_station = str(input("\nEnter the landing  station -> "))
    end_station = str(input("Enter the destination station -> "))


    distances = graph.dijkstra(start_station)
    path = graph.shortest_path(distances, start_station, end_station)
    
    print(f'Distances from {start_station} to every station: {distances}')

    print(f'\nShortest path look like this: ')

    for station in path:
        print(f'{station}', '-> ')


if __name__ == "__main__":
    main()


