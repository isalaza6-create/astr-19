class dog:

	def __init__(self, legs, eyes, fur, tail):

		self.legs=int(legs)
		self.eyes=int(eyes)
		self.fur = bool(fur)
		self.tail = bool(tail)

def main():

	mydog = dog(legs=4,eyes=2,fur=True,tail=True)

	print("legs=4")
	print("eyes=2")
	print("fur=true")
	print("tail=true")

if __name__ == '__main__':
	main()