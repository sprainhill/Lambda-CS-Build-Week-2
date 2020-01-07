# when you run out of unexplored directions
# to go you need to figure out where to go next

# the best way to do this is going to be 
# to do a breadth first search for the shortest
# path to a room that has an '?' unexplored direction
# if there are now unexplored directions
# than congratulations you have traversed
# the entire maze

class bfs():
    def __init__(self, starting_room):
        self.starting_room = starting_room
    
    def honk(self):
        print(f"honk!")

    