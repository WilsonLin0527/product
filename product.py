
import os #operating system

def read_file(filename):
	product = [];
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' == line:
				continue;
			name, price = line.strip().split(',');
			product.append([name, price]);
		print(product);
	return product;

def user_input(product):
	while True:
		name = input('insert the product name:');
		if 'q' == name:
			break;
		price = input('insert price:');
		p = [name, price];
		product.append(p);
	print(product);
	return product;

def print_product(product):	
	for p in product:
		if '商品,價格' == p:
			continue;
		print(p[0], 'is $', p[1]);

def write_file(filename, product):	
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格 \n');
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')

def main_function():
	filename = 'product.csv';
	if os.path.isfile(filename):
		product = read_file(filename);
	product = user_input(product);
	print_product(product);
	write_file(filename, product);

main_function()