# By Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

# Date: January 2025

class Node:
    def __init__(self, ring, index):
        self.ring = ring  # Reference to the ring network
        self.index = index  # Index of this node in the ring
        self.leader = False  # Flag to indicate if this node is the leader

    def send_message(self, message):
        next_node = self.ring[(self.index + 1) % len(self.ring)]  # Get the next node in the ring
        next_node.receive_message(message)  # Send the message to the next node

    def receive_message(self, message):
        if message == self.index:  # If the message is from this node
            self.leader = True  # Declare this node as the leader
            print(f"Node {self.index} is the leader.")
        else:
            self.send_message(message)  # Forward the message to the next node

def initialize_ring(num_nodes):
    ring = [Node(None, i) for i in range(num_nodes)]  # Create the ring with the specified number of nodes
    for node in ring:
        node.ring = ring  # Set the ring reference for each node
    return ring

def start_election(ring):
    for node in ring:
        node.send_message(node.index)  # Each node sends a message with its index

# Example usage
num_nodes = 5  # Number of nodes in the ring
ring = initialize_ring(num_nodes)  # Initialize the ring
start_election(ring)  # Start the leader election process