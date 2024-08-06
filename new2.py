import matplotlib.pyplot as plt

cate = ['apple', 'banana', 'orange', 'strawberry', 'grape']
values = [25, 30, 15, 20, 35]

plt.clf()
plt.bar(cate, values, color = 'skybule')
plt.title("fruit sales")

plt.xlabel('fruit')
plt.ylabel('sales')
plt.savefig('.과일/파일.png')
plt.show()
