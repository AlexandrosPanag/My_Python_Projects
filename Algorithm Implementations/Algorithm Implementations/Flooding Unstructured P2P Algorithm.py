# By Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

# Date: January 2025

import uuid
import time
from collections import defaultdict

class Peer: # Peer class
    def __init__(self, peer_id): # Constructor
        self.peer_id = peer_id # Peer ID
        self.neighbors = [] # Neighbors
        self.received_messages = set() # Received messages

    def add_neighbor(self, neighbor): # Add neighbor
        self.neighbors.append(neighbor) # Append neighbor
 
    def send_message(self, message): # Send message
        message_id = str(uuid.uuid4()) # Message ID
        self._flood_message(message, message_id) # Flood message

    def _flood_message(self, message, message_id, sender=None): # Flood message
        if message_id in self.received_messages: # If message ID in received messages
            return # Return
        self.received_messages.add(message_id) # Add message ID to received messages
        print(f"Peer {self.peer_id} received message: {message}") # Print message

        for neighbor in self.neighbors: # For each neighbor
            if neighbor != sender: # If neighbor not sender
                neighbor._flood_message(message, message_id, self) # Flood message

# Create peers
peer1 = Peer("Peer1")
peer2 = Peer("Peer2")
peer3 = Peer("Peer3")
peer4 = Peer("Peer4")

# Establish connections (neighbors)
peer1.add_neighbor(peer2)
peer2.add_neighbor(peer1)
peer2.add_neighbor(peer3)
peer3.add_neighbor(peer2)
peer3.add_neighbor(peer4)
peer4.add_neighbor(peer3)

# Send a message from peer1
peer1.send_message("Hello, P2P Network!")

# Output:
# Peer Peer1 received message: Hello, P2P Network!
# Peer Peer2 received message: Hello, P2P Network!
# Peer Peer3 received message: Hello, P2P Network!
# Peer Peer4 received message: Hello, P2P Network!