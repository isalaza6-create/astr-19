class dog:

	def __init__(self, arms, legs, eyes, fur, tail):

		self.arms=float(arms)
		self.legs=float(legs)
		self.eyes=int(eyes)
		self.fur = bool(fur)
		self.tail = bool(tail)

def main():

	mydog = dog(arms=0.4,legs=0.6,eyes=2,fur=True,tail=True)

	print("arms=0.4")
	print("legs=0.6")
	print("eyes=2")
	print("fur=true")
	print("tail=true")

if __name__ == '__main__':
	main()
