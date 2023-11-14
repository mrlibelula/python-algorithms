from collections import deque
import time, threading

class Queue:
    def __init__(self) -> None:
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
# orders excercise (with multi-threading)
class Order:
    def __init__(self) -> None:
        self.orders = Queue()
        
    def place_orders(self, orders):
        for order in orders:
            self.orders.enqueue(order)
            print("Ordered: " + order)
            time.sleep(0.5)

    def serve_order(self):
        order = self.orders.dequeue()
        print("Served: " + order)
        return order
    
    def serve_orders(self):
        while self.orders.size():
            self.serve_order()
            time.sleep(2)
    
if __name__ == '__main__':
    o = Order()
    orders = ['pizza','fricase','pasta','silpancho','burger']
    t1 = threading.Thread(target=o.place_orders, args=(orders,))
    t2 = threading.Thread(target=o.serve_orders)

    time1 = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    time2 = time.time()
    time_diff = time2 - time1

    print("\nAll orders were served in " + str(time_diff) + ' seconds')

