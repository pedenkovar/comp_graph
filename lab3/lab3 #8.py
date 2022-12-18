import matplotlib.pyplot as plt
x = []
y = []

for line in open('DS8.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(960-int(lines[1]))
    y.append(int(lines[0]))


plt.figure(figsize=(8, 8))    
plt.scatter(x, y, marker = 'o', c = 'b', s = 2) 

plt.gca()
plt.axis('off')

plt.savefig('affine transformation.png', dpi = 120)