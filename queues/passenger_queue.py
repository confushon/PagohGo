class PassengerNode:
  def __init__(self, passenger_id, arrival_time):
    self.passenger_id = passenger_id
    self.arrival_time = arrival_time
    self.next = None

class PassengerQueue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def is_empty(self):
    return self.front is None

  def enqueue(self, passenger_id, arrival_time):
    """Add passenger to the queue"""
    new_node = PassengerNode(passenger_id, arrival_time)

    if self.is_empty():
      self.front = self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node

    self.size += 1
