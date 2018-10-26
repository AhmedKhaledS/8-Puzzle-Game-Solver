from abc import ABC, abstractmethod
import queue
import priorityQueue



class Container:
	@abstractmethod
	def get_element(self):
		pass

	@abstractmethod
	def put_element(self, element):
		pass

	@abstractmethod
	def is_empty(self):
		pass

class Stack(Container):
	def __init__(self):
		self.stack = []

	def get_element(self):
		element = self.stack.pop()
		return element

	def put_element(self, element):
		self.stack.append(element)

	def is_empty(self):
		if self.stack:
			return False
		return True

class Queue(Container):
	def __init__(self):
	    self.qu = queue.Queue()

	def get_element(self):
		element = self.qu.get_nowait()
		return element

	def put_element(self, element):
		self.qu.put(element)

	def is_empty(self):
		return self.qu.empty()

class PriorityQueue(Container):
	def __init__(self, cost_function):
		self.priority_queue = priorityQueue.PriorityQueueWithFunction(cost_function)

	def put_element(self, element):
		self.priority_queue.push(element)

	def get_element(self):
		return self.priority_queue.pop()

	def is_empty(self):
		return self.priority_queue.isEmpty()

def main():
	qu = Queue()
	print (qu.is_empty())
	qu.put_element(4)
	qu.put_element(5)
	qu.put_element(6)
	print (qu.is_empty())
	print(qu.get_element())

	stk = Stack()
	print (stk.is_empty())
	stk.put_element(4)
	stk.put_element(5)
	stk.put_element(6)
	print (stk.is_empty())
	print(stk.get_element())


if __name__ == '__main__':
	main()