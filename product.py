product = []
while True:
	name = input('insert the product name:');
	if 'q' == name:
		break;
	price = input('insert price:');
	p = [];
	p.append(name);
	p.append(price)
	product.append(p);
print(product);