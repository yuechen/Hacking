#####################################################################
# Yuechen Zhao <yuechenzhao@college.harvard.edu>
# www.yuechenzhao.com
#
# Bounded Queue implementation in Python. If n is the capacity,
# this implementation requires O(n) space. Enqueue and dequeue
# both run in time O(1) via a circular array algorithm. 
# No effort was made to perform smart space management because it 
# offers no theoretic improvement in space usage and requres slowing 
# down the actual operations on the queue. This strategy works 
# especially well if the number of items in the queue is close to 
# capacity most of the time. If this assumption turns out to be false 
# and the size of the queue actually varies widely, optimizations can 
# be added to modify the memory usage as needed. In that case, we 
# should consider implementing a non-bounded queue.
#
# KPCB Fellows Application 2013
#
# To run (with tests): python queue.py
#####################################################################

"""
class Queue

Defines a bounded queue (FIFO) that has a preset capacity.
"""
class Queue:
	"""
	__init__(self, capacity)
	Constructor for the bounded queue.

	Arguments
	=========
	capacity (int):
		An integer capacity for the bounded queue.

	Returns
	=======
	<Nothing>
	"""
	def __init__(self, capacity):
		self.q = [0] * capacity  		# An array to hold the data of the queue
		self.head = 0					# The position of the head in the array
		self.size = 0					# The current # of items in the queue
		self.capacity = capacity 		# The capacity of the queue

	"""
	dequeue(self, capacity)
	Performs a dequeue operation and returns the integer
	at the head of the queue.

	Arguments
	=========
	<Nothing>

	Returns
	=======
	The integer at the front of the queue, if the queue is
	not empty. Otherwise, returns None.
	"""
	def dequeue(self):
		# Cannot dequeue if the queue is empty
		if self.size <= 0:
			return None

		# Return the value and move the head of the queue
		val = self.q[self.head]
		self.head = (self.head + 1) % self.capacity
		self.size -= 1
		return val

	"""
	enqueue(self, val)
	Performs an enqueue operation given some value to put
	into the queue.

	Arguments
	=========
	val (int)
		The integer value to insert into the queue.

	Returns
	=======
	True if the enqueue operation was successful, False otherwise.
	(i.e. If the queue is already full.)
	"""
	def enqueue(self, val):
		# Cannot enqueue is the queue is full
		if self.size >= self.capacity:
			return False

		# Insert the value at the end of the queue, increase the size
		self.q[(self.head + self.size) % self.capacity] = val
		self.size += 1
		return True

"""
stress_test(q)
Performs a stress test on the provided queue by inserting capacity ints 
into the queue and then dequeuing all of those values, checking for
the correct ordering of dequeued values. Checks that the size of the 
queue is correct along the way.

Note: this function leaves the queue completely empty after completion.

Arguments
=========
q (Queue)
	The queue upon which to perform the test.

Returns
=======
<Nothing>
"""
def stress_test(q):
	# Clear the queue
	while q.size > 0:
		q.dequeue()

	# Insert CAPACITY items into the queue
	for i in range(q.capacity):
	    q.enqueue(i)
	    assert(q.size == i + 1)
	assert(q.size == q.capacity)

	# Check that it's not possible to insert anymore
	assert(not q.enqueue(0))

	# Dequeue all the items
	for i in range(q.capacity):
		assert(q.size == q.capacity - i)
		assert(i == q.dequeue())
	assert(q.size == 0)

	# Check that it's not possible to dequeue anymore
	assert(q.dequeue() == None)

"""
main()
The main function. Constructs a queue and tests it for correctness.

Arguments
=========
<Nothing>

Returns
=======
<Nothing>
"""
def main():
	CAPACITY = 10000

	# Construct a queue
	q = Queue(CAPACITY)

	# Performs a stress test on a fresh queue
	stress_test(q)

	# Move the head by CAPACITY / 2 (for testing purposes only!)
	q.head = CAPACITY / 2

	# Perform some enqueue/dequeue mixed operations
	assert(q.size == 0)
	q.enqueue(5)
	q.enqueue(10)
	q.enqueue(15)
	assert(q.dequeue() == 5)
	q.enqueue(20)
	assert(q.size == 3)
	assert(q.dequeue() == 10)
	assert(q.dequeue() == 15)
	assert(q.dequeue() == 20)

	# Stress test again with the head moved
	stress_test(q)

if __name__ == "__main__":
	main()