import numpy as np
from tabulate import tabulate 
from astropy.table import Table

x = np.linspace(0.0, 2.0 * np.pi, 1000)
y = np.sin(x)




table_data = [(a, b) for a, b in zip(x, y)]


table_headers = ["x", "sin(x)"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers,
	floatfmt=".6f")


astropy_table = Table() 
astropy_table["x"] = x 
astropy_table["sin(x)"] = y 


astropy_table["x"].format = "{:.6f}"
astropy_table["sin(x)"].format = "{:.6f}"


def main():
	print(table_data) 
	print(python_table) 
	print(astropy_table) 

if __name__=='__main__':
	main()