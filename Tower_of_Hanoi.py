from copy import deepcopy


class Node:
    def __init__(self):
        self.state = [[], [], []]
        self.nodeNumber = 0
        self.status = 'idle'
        self.neighbours = []
        self.parent = None
        self.children = []  # For BFS
        self.point = 10


def move(st1, st2):
    s1 = st1[:]
    s2 = st2[:]

    if len(s1) > 0:
        topDisc = s1[len(s1) - 1]
        lastofS2 = len(s2) - 1

        if len(s2) == 0 or s2[lastofS2] > topDisc:
            s2.append(topDisc)
            s1.pop()

            return s1, s2
        else:
            return None
    else:
        return None


def moveDisc(n):
    global noOfPegs
    stacks = []

    for x in range(0, noOfPegs):
        for y in range(0, noOfPegs):

            stacks = move(n.state[x], n.state[y])

            if stacks != None:
                # print 'states after move', states
                nextnode = Node()
                nextnode = deepcopy(n)
                nextnode.state[x] = deepcopy(stacks[0])
                nextnode.state[y] = deepcopy(stacks[1])

                # print 'states', states
                # print '\n'
                # print 'next node',nextnode.state
                if nextnode.state in states:
                    # print 'nextnode in states'
                    a = 1  # dumb value
                else:
                    nodenumber = nextnode.nodeNumber
                    # print nextnode.state, 'next not in states'
                    states.append(nextnode.state)
                    return nextnode
    # print 'DEAD END'
    return None


def printPath(node):
    print('Tracing back the Path')
    while True:
        print('Node number: ', node.nodeNumber, '  State:  ', node.state)
        if node.parent != None:
            node = node.parent
        else:
            break


def BFS(node):
    global parentList, nodenumber, childList, targetFound, step

    print('\n STEP : ', step)
    step += 1
    for node in parentList:
        if targetFound == False:
            print('Parent Node:', node.nodeNumber, ' State :', node.state)
            exhausted = False
            parent = deepcopy(node)

            i = 1
            while exhausted == False:

                i += 1
                childnode = moveDisc(node)

                if childnode != None:
                    nodenumber += 1
                    childnode.nodeNumber = nodenumber
                    childnode.parent = node
                    parent.children.append(childnode)
                    childList.append(childnode)
                    print('     Child Node:', childnode.nodeNumber, 'State:', childnode.state)
                    # print 'states', states
                    if childnode.state == finalState:
                        print('Final target reached')
                        printPath(childnode)
                        targetFound = True


                else:
                    exhausted = True
    parentList = deepcopy(childList)
    childList = []
    if targetFound == False:
        BFS(parentList)



def readState():
    global noOfPegs
    state = []
    for x in range(0, noOfPegs):
        print('Discs in Peg', x + 1, ' : ', )
        a = [int(x) for x in input().split()]
        state.append(a)

    return state


noOfPegs = 3
shouldContinue = True
while shouldContinue:
    print('\n\nTower of Hanoi')

    print('1. Breadth First Search')
    print('2. Exit')

    algoNumber = input("Please select the option --> ")

    if algoNumber == '2':
        print('\nExiting')
        quit()

    print('\nInstructions for input:')
    print('-->An example input for discs in a peg >>> 3 2 1')
    print('-->This means your peg have 3 discs with disc of size 3 at bottom and disc of size 1 at top')
    print('-->If the peg is empty, just click ENTER; Do not input anything in that case')
    noOfPegs = int(input("\nEnter number of pegs--> "))

    print('\nEnter details for initial State')
    initialState = readState()
    print('\nEnter details for final State')
    finalState = readState()

    print('\nInitial state : ', initialState)
    print('Final states  : ', finalState)

    # initialState=[[1],[3],[2]]
    # finalState=[[3,1],[2],[]]

    # initialState=[[3],[1],[2]]
    # finalState=[[3,2,1],[],[]]
    states = []
    states = [initialState]
    nodenumber = 1
    time = 1
    targetFound = False

    node = Node()
    node.state = initialState
    node.nodeNumber = nodenumber
    parentList = [node]
    childList = []
    targetFound = False
    largestInTarget = False

    step: int = 1

    parentList = [node]
    childList = []

    if algoNumber == '1':
        print('\nYou selected Breadth First Search')
        BFS(node)

    elif algoNumber == '2':
        print('\nExiting')
        quit()

    else:
        print('Please select a valid option')
        continue
