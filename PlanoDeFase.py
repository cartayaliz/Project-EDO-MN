import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X , Y = np.meshgrid(x, y)

U = -3 * X + Y  # dx/dt
V = -4 * X - 2 * Y  # dy/dt

plt.figure(figsize=(12, 10))

plt.streamplot(X, Y, U, V, density=1.5, color='blue', linewidth=1,arrowsize=1.5)

plt.plot(0, 0, 'ro', markersize=10, markerfacecolor='red', label='Punto crítico (0,0)')


plt.title('Plano de Fase - Sistema Acoplado\nFoco Estable - Todas las trayectorias convergen al origen')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()