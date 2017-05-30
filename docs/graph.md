# Graph Theory
 
Graph theory is a topic that shows up commonly in competitive programming. 
 
A graph is a sort of map. You can imagine many nodes (houses, cities, other objects) which are interconnected by edges (roads). Graph theory aims to answer questions about the paths between these nodes.
 
## Graph Traversal
 
Breadth First Search and Depth First Search are methods of traversing a graph that can be used to gather information such as if a specific node exists or to find a valid path to that node. 
 
### Breadth First Search
BFS visits all nodes one “layer” at a time. Starting at the root it looks at all child nodes of the root. Afterwards, for each of these children, it will perform the same action, it will check all the children of the children of the root. It is easier to understand with a picture:
 
![bfs tree](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/390px-Breadth-first-tree.svg.png)
 
#### Java implmentation
The following is an example in Java of how to implement BFS. This is the solution to [VM7WC '16 #3 Silver - Can Shahir even get there?!
](https://dmoj.ca/problem/vmss7wc16c3p2). After reaching a node, it adds all of its children and moves to the next node in the queue. This ensures that each layer will be opened one by one.
 
```java
import java.util.*;
 
public class Main {
 
  public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
 
  static Scanner scan = new Scanner(System.in);
 
  public static void main(String[] args) {
    int n, m, a, b;
    n = scan.nextInt();
    m = scan.nextInt();
    a = scan.nextInt();
    b = scan.nextInt();
   
    //Creating a graph using adjacency lists
    //In this case the houses (nodes) are numbers, so you can just use arraylists/arrays
    //If the nodes are strings, you pretty much have to use a HashMap
   
    for (int i = 0; i <= n; i ++) { //Creating new arraylists for each possible node (n nodes)
      graph.add(new ArrayList<Integer>());
    }
   
    int x, y;
   
    for (int i = 0; i < m; i ++) {
      x = scan.nextInt();
      y = scan.nextInt();
      graph.get(x).add(y); //adds the adjacent node (neighbor) to the graph
      graph.get(y).add(x); //adds the connection the other way
      //Means that x will be connnected to y and y will be connceted to x
    }
   
    if (BFS(a,b))
      System.out.println("GO SHAHIR!");
    else
      System.out.println("NO SHAHIR!");
  }
 
  //BFS will start at the start node, and check all the nodes beside it
  //It adds those nodes to the queue, and then spreads out again
  // Keeps expanding one "layer" at a time until the target is seen or until there's nothing left to check
  public static boolean BFS(int start, int end) {
    ArrayDeque<ArrayList<Integer>> queue = new ArrayDeque<>(); //Double ended queue, similar functions as arraylist, faster pop from front though
    HashSet<Integer> visited = new HashSet<>(); //stores visited nodes
    ArrayList<Integer> temp = new ArrayList<Integer>();
    temp.add(start); //Creates a temporary "path" containing only the start node
    queue.add(temp);
   
    while(queue.size() != 0){ //If the queue is not empty
        ArrayList<Integer> path = queue.poll(); //Gets the first path in the queue
        int node = path.get(path.size()-1); //Gets the last node in the path
       
        if (node == end) { //If you've found the target
          return true;
        }
       
        if(!visited.contains(node)){ //If vertex hasn't already been visited
            for (int adj: graph.get(node)) { //Checks all neighbor nodes
              ArrayList<Integer> newpath = new ArrayList<Integer>(path); //Copies the current path IMPORTANT TO DO THIS CONSTUCTOR COPY OR IT WILL POINT TO SAME MEMORY
              newpath.add(adj); //Adds the neighboring node to the path
              queue.add(newpath); //Adds the new path into the queue
            }
            visited.add(node); //Adds the node to visited
        }
    }
   
    return false; //Queue is empty, all nodes have been checked, no possible path
  }
}
```
 
### Depth First Search
DFS continues visiting the first (or leftmost) child of each node until there are no more nodes. Afterwards, it returns to the parent of the last node in the path, and visits the rest of it’s children. It goes as deep as possible down each path, and then moves up one layer and checks as deep as possible again. It is easier to understand with a picture.
 
![dfs tree](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/300px-Depth-first-tree.svg.png)
 
Depth first search can be written iteratively by changing one line of iterative breadth first search.
> Hint: you can then switch the deque to a simple vector
 
DFS can also be written recursively.

```cpp
DFS(start,end,path) {
	// In python recursion you must copy the path since it passes by reference
    // otherwise it will be passed a copy in C++ and Java
	path = path + [start] // Python
	path.push(start) // Other languages
	if (start == end)
    	return path
	if (graph[start].size == 0) // Reached the end of a path (a leaf)
		return [] // No path possible
	for each node in graph[start] { // For-each loop through all children of the current node
		if (node not in path) { // Do not go backwards in the path
			newpath = DFS(node,end,path)
			if newpath != [] // If a path to the end if found
				return newpath
	return [] // If nothing is found return nothing
}
```

## Dijkstra's Algorithm

In many cases, you are trying to find the shortest path from a single source to a destination given that each edge between nodes have different lengths or **weights**. This common problem, often known as finding the *Single Source Shortest Path*, can be solved using Dijkstra's algorithm.

### MIT OpenCourseware
[![ocw dijkstras](https://img.youtube.com/vi/2E7MmKv0Y24/0.jpg)](https://www.youtube.com/watch?v=2E7MmKv0Y24)

### Implementation
Below is a partial Python solution to [Single Source Shortest Path](https://dmoj.ca/problem/sssp) using Dijkstra's.


```python
def dijkstras(Graph, weights, source):
    distances = {}
    for i in Graph:
		distances[i] = inf
	q, visited = [(0, source)], set() 
    distances[source] = 0
    while q:
		(dist, v1) = heappop(q)
		if v1 in visited:
        	continue
		visited.add(v1)
		for v2 in Graph[v1]:
			if v2 not in visited:
				newd = dist + weights[(v1, v2)]	
                heappush(q, (dist + weights[(v1, v2)], v2))
			if distances[v2] > newd:
				distances[v2] = newd
  return distances

