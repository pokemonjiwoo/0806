import matplotlib.pyplot as plt

x = [17, 18, 19, 20, 21, 22, 23]
y = [65, 70, 70, 75, 80, 85, 85]

plt.plot(x, y, marker = 'o', linestyle = '-', color = 'b', label = 'humidity')
plt.xlabel('Time(hour)')
plt.ylabel('Humidity(c)')
plt.legend()
plt.grid(True)
plt.savefig('./저장.png')
plt.show()