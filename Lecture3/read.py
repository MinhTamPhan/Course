from graph import Digraph, Node, WeightedEdge

def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    # TODO
    #print("Loading map from file..." + map_filename)
    g = Digraph()
    fileMap = open(map_filename, 'r')
    for line in fileMap:
        temp = line.split(' ');        
        src = Node(temp[0])
        dest = Node(temp[1])        
        if g.has_node(src) == False:
            g.add_node(src)
        if g.has_node(dest) == False:
            g.add_node(dest)
        edge = WeightedEdge(src, dest, int(temp[2]), int(temp[3]))
        g.add_edge(edge)       
    return g

load_map("mit_map.txt")