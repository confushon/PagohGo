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

  def dequeue(self, current_time):
    """Remove passenger from queue and calculate waiting time"""
    if self.is_empty():
      return None, 0

    removed_passenger = self.front
    self.front = self.front.next

    if self.front is None:
      self.rear = None

    self.size -= 1

    waiting_time = current_time - removed_passenger.arrival_time
    return removed_passenger.passenger_id, waiting_time

  def get_queue_size(self):
    """Display passengers currently in queue"""
    passenger = []
    current = self.front

    while current:
      passenger.append(
        f"{current.passenger_id} (arrived at {current.arrival_time})"
      )
      current = current.next

    return passengers

#Testing
queue = PassengerQueue()
queue.enqueue("S001", 5)
queue.enqueue("S002", 7)
pid, wait = queue.dequeue(10)
print(pid, wait)
