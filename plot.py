from matplotlib import pyplot as plt

x = [21, 22, 23, 24, 25, 31]
y = [3000, 10000, 24000, 50000, 800000, 1000000]

plt.style.use('fivethirtyeight')

plt.bar(x, y, label="a")

plt.ylabel('salary')
plt.xlabel('ages')
plt.title("Salary by Age")

plt.legend()


plt.show()
