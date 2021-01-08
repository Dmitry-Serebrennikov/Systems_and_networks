import matplotlib.pyplot as plt

file_name = open('ping_statistic.txt')
lines = file_name.readlines()
time = []
total = 0

for line in lines[2:-4]:
    ln = line.split(' ')
    time.append(float(ln[6].split('=')[1]))
    total = total + time[-1]

#print(time)
plt.hist(time)
plt.title('Distribution of network delay')
plt.xlabel('Time delay')
plt.ylabel('Ping quantity')
#plt.show()
print('Average time delay: ', total / 1000)
plt.savefig('result.png', dpi=500)