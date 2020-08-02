# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

class Solution:
    def getNeighbours(self, curr, graph):
        try:
            return graph[curr]
        except KeyError:
            return []

    def colourNode(self, curr, initial, final):
        try:
            initial.remove(curr)
            final.add(curr)
        except KeyError:
            pass

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = set(range(numCourses))
        grey = set()
        black = set()

        if len(prerequisites) == 0:
            return True
        
        def traverse(curr, graph, white, grey, black) -> bool:
            if curr in grey:
                return False
            self.colourNode(curr, white, grey)
            neighbours = self.getNeighbours(curr, graph)
            for neighbour in neighbours:
                if neighbour not in black:
                    res = traverse(neighbour, graph, white, grey, black)
                    if res == False:
                        return False
            self.colourNode(curr, grey, black)
            return True
        graph = {}
        for x in prerequisites:
            try:
                graph[x[0]].append(x[1])
            except KeyError:
                graph[x[0]] = [x[1]]
        
        for i in range(numCourses):
            if i not in black:
                if traverse(i, graph, white, grey, black) == False:
                    return False
        return True
        