class Queue:
	def __init__(self,size=0):
		self.size=size
		self.list1=[]
	def add(self,data):
		if len(self.list1)>=self.size:
			print("queue is empty")
		self.list1.append(data)	
	def remove(self):
		if len(self.list1)<=0:
			print("queue is empty")
			return
		self.list1.pop(0)
obj=Queue(3)
obj.add(5)
print(obj.list1)
obj.add(6)
print(obj.list1)
obj.add(7)
print(obj.list1)

	
