queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after Enqueue:", queue)

dequeued = queue.pop(0)
print("Dequeued Element:", dequeued)

print("Front Element:", queue[0])

print("Current Queue:", queue)
