import numpy as np 


# def expo(x): 
# 	return np.exp(x)



def fn(x):
	return x**3+8


def main():
	x=9
	print(x)

	print(fn(x))
	
	
	if fn(x) > 27: 
		print("YAY!")


if __name__ == "__main__":
	main()
