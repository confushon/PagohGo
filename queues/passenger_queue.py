class PassengerNode:
  def __init__(self, passenger_id, arrival_time):
    self.passenger_id = passenger_id
    self.arrival_time = arrival_time
    self.next = None
