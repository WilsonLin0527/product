product = []
while True:
	name = input('insert the product name:');
	if 'q' == name:
		break;
	price = input('insert price:');
	p = [name, price];
	product.append(p);
print(product);

for p in product:
	print(p[0], 'is $', p[1]);

with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格 \n');
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')