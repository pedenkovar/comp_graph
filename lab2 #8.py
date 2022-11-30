import matplotlib.pyplot as plt
x = []
y = []
for line in open('DS8.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y.append(int(lines[1]))

plt.figure(figsize=(8, 4.5))    
plt.scatter(x, y, marker = 'o', c = 'k', s = 1) 

plt.gca()
plt.axis('off')

plt.savefig('ds8(960x540).png', dpi = 120)