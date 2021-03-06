# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    visited = []
    #Astar uses PriorityQueue as its modified UCS/Djikstra
    frontier = util.Stack()
    #Push start with empty path and cost
    frontier.push((problem.getStartState(),[]))
    while not frontier.isEmpty():
        #Get top out of frontier
        current, path = frontier.pop()
        #If top never visited, check goal and get successors.
        if current not in visited:
            visited.append(current)
            #If Goal, return list of actions
            if problem.isGoalState(current):
                return path
            for state, direction, cost in problem.getSuccessors(current):
                if state not in visited:
                    #Access path thus far and append the successor direction.
                    updatePath = path + [direction]
                    #Push successor and updated path onto frontier
                    #Cost is cost of path + heuristic
                    frontier.push((state, updatePath))


    # start = problem.getStartState()
    # frontier = util.Stack()
    # visited = {}
    # path = util.Queue()
    #
    # frontier.push(start)
    # visited[start]= "", ""
    # while not frontier.isEmpty():
    #     currentNode = frontier.pop()
    #     if problem.isGoalState(currentNode):
    #         break
    #     for state, direction, cost in problem.getSuccessors(currentNode):
    #         if state not in visited:
    #             #key is state, value is parent
    #             visited[state] = currentNode, direction
    #             frontier.push(state)
    #         else:
    #             #if child is a successor to current update path
    #             if state in frontier.list:
    #                 visited[state] = currentNode, direction
    #
    # while currentNode != problem.getStartState():
    #     currentNode, direction = visited[currentNode]
    #     path.push(direction)
    # return path.list

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    #Astar uses PriorityQueue as its modified UCS/Djikstra
    frontier = util.Queue()
    #Push start with empty path and cost
    frontier.push((problem.getStartState(),[]))
    while not frontier.isEmpty():
        #Get top out of frontier
        current, path = frontier.pop()
        #If top never visited, check goal and get successors.
        if current not in visited:
            visited.append(current)
            #If Goal, return list of actions
            if problem.isGoalState(current):
                return path
            for state, direction, cost in problem.getSuccessors(current):
                if state not in visited:
                    #Access path thus far and append the successor direction.
                    updatePath = path + [direction]
                    #Push successor and updated path onto frontier
                    #Cost is cost of path + heuristic
                    frontier.push((state, updatePath))
    # start = problem.getStartState()
    # print "Start State: ", start
    # frontier = util.Queue()
    # visited = {}
    # path = util.Queue()
    #
    # frontier.push(start)
    # visited[start]= "", ""
    # while not frontier.isEmpty():
    #     currentNode = frontier.pop()
    #     if problem.isGoalState(currentNode):
    #         break
    #     for state, direction, cost in problem.getSuccessors(currentNode):
    #         if state not in visited:
    #             #key is state, value is parent
    #             visited[state] = currentNode, direction
    #             frontier.push(state)
    #
    #
    # while currentNode != problem.getStartState():
    #     currentNode, direction = visited[currentNode]
    #     path.push(direction)
    # return path.list

    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    #Astar uses PriorityQueue as its modified UCS/Djikstra
    frontier = util.PriorityQueue()
    #Push start with empty path and cost
    frontier.push((problem.getStartState(),[]),0)
    while not frontier.isEmpty():
        #Get top out of frontier
        current, path = frontier.pop()
        #If top never visited, check goal and get successors.
        if current not in visited:
            visited.append(current)
            #If Goal, return list of actions
            if problem.isGoalState(current):
                return path
            for state, direction, cost in problem.getSuccessors(current):
                if state not in visited:
                    #Access path thus far and append the successor direction.
                    updatePath = path + [direction]
                    #Push successor and updated path onto frontier
                    #Cost is cost of path + heuristic
                    frontier.push((state, updatePath), problem.getCostOfActions(updatePath))

    # start = problem.getStartState()
    # frontier = util.PriorityQueue()
    # visited = {}
    # path = util.Queue()
    #
    # frontier.push((start, 0), 0)
    # visited[start]= "", "", ""
    # while not frontier.isEmpty():
    #     currentNode, addCost = frontier.pop()
    #     if problem.isGoalState(currentNode):
    #         break
    #     for state, direction, cost in problem.getSuccessors(currentNode):
    #         if state not in visited:
    #             #key is state, value is parent, cost is total cost found so far
    #             visited[state] = currentNode, direction, cost + addCost
    #             #Add the successor to the queue with cost being total so far
    #             #Need to add twice due to how the priorityQ was implemented.
    #             frontier.push((state, cost + addCost), cost + addCost)
    #         else:
    #             #If a successor has already been visited, check if the new route would have a lesser cost.
    #             if visited[state][2] > cost + addCost:
    #                 #If lesser cost route, update the connection.
    #                 visited[state] = currentNode, direction, cost + addCost
    #
    # while currentNode != problem.getStartState():
    #     currentNode, direction, cost = visited[currentNode]
    #     path.push(direction)
    # return path.list

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    #Astar uses PriorityQueue as its modified UCS/Djikstra
    frontier = util.PriorityQueue()
    #Push start with empty path and cost
    frontier.push((problem.getStartState(),[]),0)
    while not frontier.isEmpty():
        #Get top out of frontier
        current, path = frontier.pop()
        #If top never visited, check goal and get successors.
        if current not in visited:
            visited.append(current)
            #If Goal, return list of actions
            if problem.isGoalState(current):
                return path
            for state, direction, cost in problem.getSuccessors(current):
                if state not in visited:
                    #Access path thus far and append the successor direction.
                    updatePath = path + [direction]
                    #Push successor and updated path onto frontier
                    #Cost is cost of path + heuristic
                    frontier.push((state, updatePath), problem.getCostOfActions(updatePath) + heuristic(state, problem))



    # start = problem.getStartState()
    # frontier = util.PriorityQueue()
    # visited = {}
    # path = util.Queue()
    #
    # frontier.push((start, 0), 0)
    # visited[start]= "", "", ""
    # while not frontier.isEmpty():
    #     currentNode, addCost = frontier.pop()
    #     #print "-------TOP:",currentNode
    #     if problem.isGoalState(currentNode):
    #         break
    #     for state, direction, cost in problem.getSuccessors(currentNode):
    #         newcost = cost + addCost + heuristic(state,problem)
    #         if state not in visited:
    #             #key is state, value is parent, cost is total cost found so far
    #             visited[state] = currentNode, direction, newcost
    #             #Add the successor to the queue with cost being total so far
    #             #Need to add twice due to how the priorityQ was implemented.
    #             frontier.push((state, cost + addCost), newcost)
    #         else:
    #             #If a successor has already been visited, check if the new route would have a lesser cost.
    #             if visited[state][2] > newcost:
    #                 #If lesser cost route, update the connection.   This needs to be reflected in frontier properly.
    #                 visited[state] = currentNode, direction, newcost
    #     #print frontier.heap
    # while currentNode != problem.getStartState():
    #     currentNode, direction, cost = visited[currentNode]
    #     path.push(direction)
    # return path.list

    # start = problem.getStartState()
    # frontier = util.PriorityQueue()
    # visited = {}
    # path = util.Queue()
    #
    # frontier.push(start,1)
    # while not frontier.isEmpty():
    #     currentNode = frontier.pop()
    #     if problem.isGoalState(currentNode):
    #         break
    #     for state, direction, cost in problem.getSuccessors(currentNode):
    #         if state not in visited:
    #             #key is state, value is parent
    #             visited[state] = currentNode, direction
    #             frontier.push(state,cost + heuristic(state,problem))
    #
    # while currentNode != problem.getStartState():
    #     currentNode, direction = visited[currentNode]
    #     path.push(direction)
    # return path.list


    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
