import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

a, g = 0.1 , 9.8
initial_conditions = [(0, 9.5), (0, 7),(0, 4.5), (1, 2), (3, 8), (5, 5.5) ]

def Torricelli_func(t, y, A_func):
    # Asegurar que y no sea negativo antes de calcular la raíz
    y_safe = np.maximum(y, 0)
    return -(a/A_func(y_safe)) * np.sqrt(2*g*y_safe)


def A_cylindrical(y):
    """Tanque cilíndrico: área constante"""
    return 1.0  # Área constante

def A_widening(y):
    """Tanque que se ensancha hacia arriba"""
    return 1.0 + 0.5 * y

def A_narrowing(y):
    """Tanque que se estrecha hacia arriba"""
    val = 2.0 - 0.15 * y
    return np.maximum(val, 0.1)

def isoclinas_plot(A_func, title):

    # Rango de visualización
    y_max = 25
    t_max = 17

    y_val = np.linspace(0.1, y_max, 20)
    t_val = np.linspace(0, t_max, 25)
    T, Y = np.meshgrid(t_val, y_val)
    
    # Calcular pendientes
    dYdt = Torricelli_func(T,Y, A_func)
    dTdt = np.ones_like(dYdt)  
    
    # Normalizar flechas para mejor visualización
    magnitude = np.sqrt(dTdt**2 + dYdt**2)
    dTdt_norm = dTdt / magnitude
    dYdt_norm = dYdt / magnitude
    
    plt.figure(figsize=(12, 7))
    plt.quiver(T, Y, dTdt_norm, dYdt_norm, scale=25, color='lightblue', alpha=0.6)

     # Integrar y trazar curvas solución para cada condición inicial
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 400)
    
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(initial_conditions))) #colores automáticos
    
    for i, (t0, y0) in enumerate(initial_conditions):
        # Resolver la EDO
        sol = solve_ivp(Torricelli_func, [t0, t_span[1]], [y0], args=(A_func,), 
                       t_eval=t_eval[t_eval >= t0], method='RK45')
      
        
        # Trazar la curva solución
        plt.plot(sol.t, sol.y[0], color=colors[i], linewidth=2, 
                label=f'y({t0}) = {y0}')
        
        # Marcar el punto inicial
        plt.plot(t0, y0, 'o', color=colors[i], markersize=8)

    plt.xlabel('Tiempo (t)')
    plt.ylabel('Altura de agua (y)')
    plt.title(f'Dinámica de vaciado - {title}')
    plt.grid(True , alpha=0.6)
    plt.axhline(0, color='black', linestyle='--', label='y=0 (equilibrio)')
    plt.legend()

    plt.show()



# Caso 1: Tanque cilíndrico
isoclinas_plot(A_cylindrical, "Tanque Cilíndrico (A constante)")

# # Caso 2: Tanque que se ensancha
isoclinas_plot(A_widening, "Tanque que se Ensancha (A crece con y)")

# # Caso 3: Tanque que se estrecha  
isoclinas_plot(A_narrowing, "Tanque que se Estrecha (A decrece con y)")

