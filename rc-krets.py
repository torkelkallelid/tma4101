import numpy as np
import matplotlib.pyplot as plt

# Parametere
R = 100e3 # ohm
C = 100e-6  # farad
V = 9.5  # Batterispenning (V)

# Teoretisk modell
t_teori = np.linspace(0, 30, 1000)  # Tid i sekunder
v_teori = V * (1 - np.e**(-t_teori / (R*C)))

# Målinger

t_målinger = [n for n in range(30)]
v_målinger = [0, 1.12, 2.37, 3.17, 3.68, 4.13, 4.69, 5.07, 5.52, 5.83, 6.20, 6.36, 6.60, 6.82, 7.02, 7.31, 7.57, 7.80, 7.99, 8.16, 8.27, 8.35, 8.41, 8.50, 8.56, 8.65, 8.79, 8.80, 8.82, 8.86]

# Plot
plt.figure()

plt.plot(t_teori, v_teori, color='blue', label="Modell")
plt.plot(t_målinger, v_målinger, marker='o', markersize=4, color='red', label="Målinger")


plt.title("Spenningen over kondensatoren")
plt.xlabel("Tid (s)")
plt.ylabel("Spenning (v)")
plt.legend()
plt.grid()
plt.show()