class stack:
	def __init__(self,size=0):
		self.size=size
		self.list1=[]
	def add(self,data):
		if len(self.list1)==self.size:
			print("Stack is full")
			return
		self.list1.append(data)
		
	def remove(self):
		if len(self.list1)==0:
			print("Stack is empty")
			return
		self.list1.pop()
a=stack(3)
a.add(1)
print(a.list1)
a.add(2)
print(a.list1)
a.add(3)
print(a.list1)
a.remove()
print(a.list1)

		
		
