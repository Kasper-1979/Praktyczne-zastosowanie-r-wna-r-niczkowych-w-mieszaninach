import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.animation import FuncAnimation # type: ignore
from scipy.integrate import solve_ivp # type: ignore

# Etap 1: Równanie różniczkowe dla Q1(t)
def etap1(t, Q1):
    Q1_wartosc = Q1[0]
    # Równanie: dQ1/dt = 15 - (3 * Q1_wartosc) / 800
    dQ1_dt = 15 - (3 * Q1_wartosc) / 800
    return dQ1_dt

# Etap 2: Równanie różniczkowe dla Q2(t)
def etap2(t, Q2, tm):
    Q2_wartosc = Q2[0]
    # Równanie: dQ2/dt = -2 * Q2_wartosc / (400 - (t - tm))
    dQ2_dt = -2 * Q2_wartosc / (400 - (t - tm))
    return dQ2_dt

# Warunki początkowe dla Etapu 1
Q1_poczatkowe = [20]
zakres_czasu_etap1 = (0, 50)
punkty_czasu_etap1 = np.linspace(0, 50, 500)

# Ogólne równanie dla Etapu 1 (przed rozwiązaniem)
print("\nEtap 1 - Ogólne Równanie:")
print("dQ1/dt = 15 - (3 * Q1) / 800\n")

# Rozwiąż równanie różniczkowe Etapu 1
sol_etap1 = solve_ivp(etap1, zakres_czasu_etap1, Q1_poczatkowe, t_eval=punkty_czasu_etap1)

# Znajdź czas t_m, kiedy Q1 osiągnie 500 uncji
t_m = np.interp(500, sol_etap1.y[0], sol_etap1.t)
print(f"t_m (czas, kiedy Q1 osiągnie 500 uncji) = {t_m:.2f} godzin")

# Przekształcenie Etapu 1: Rozwiązanie równania różniczkowego
print("\nEtap 1 - Rozwiązanie Równania Różniczkowego:")
print("dQ1/dt = 15 - (3 * Q1) / 800")
print("Jest to równanie różniczkowe liniowe. Możemy użyć separacji zmiennych, aby je rozwiązać.")
print("1. Pomnóżmy obie strony przez dt: dQ1 = (15 - (3 * Q1) / 800) dt")
print("2. Zintegrować obie strony, aby uzyskać rozwiązanie.")
print(f"Rozwiązanie: Q1(t) = 4000 - 3998 * e^(-3 * t / 800)\n")

# Utwórz nowe rozwiązanie dla Etapu 1 aż do t_m
punkty_czasu_etap1_stop = np.linspace(0, t_m, 500)
sol_etap1_stop = solve_ivp(etap1, (0, t_m), Q1_poczatkowe, t_eval=punkty_czasu_etap1_stop)

# Warunki początkowe dla Etapu 2
Q2_poczatkowe = [500]
zakres_czasu_etap2 = (t_m, t_m + 400)
punkty_czasu_etap2 = np.linspace(t_m, t_m + 400, 500)

# Ogólne równanie dla Etapu 2 (przed rozwiązaniem)
print("Etap 2 - Ogólne Równanie:")
print("dQ2/dt = -2 * Q2 / (400 - (t - tm))\n")

# Przekształcenie Etapu 2: Rozwiązanie równania różniczkowego
print("\nEtap 2 - Rozwiązanie Równania Różniczkowego:")
print("dQ2/dt = -2 * Q2 / (400 - (t - tm))")
print("Jest to równanie różniczkowe separowalne. Możemy je rozwiązać podobnie.")
print("1. Pomnóżmy obie strony przez dt: dQ2 = (-2 * Q2 / (400 - (t - tm))) dt")
print("2. Zintegrować obie strony, aby uzyskać rozwiązanie.")
print(f"Rozwiązanie: Q2(t) = (435.476 - t) * 2 / 320\n")

# Rozwiąż równanie różniczkowe Etapu 2
sol_etap2 = solve_ivp(etap2, zakres_czasu_etap2, Q2_poczatkowe, t_eval=punkty_czasu_etap2, args=(t_m,))

# Połącz dane z obu etapów
total_time = np.concatenate((sol_etap1_stop.t, sol_etap2.t))
total_Q = np.concatenate((sol_etap1_stop.y[0], sol_etap2.y[0]))

# Tworzenie animacji
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Zanieczyszczenie w zbiorniku w czasie")
ax.set_xlabel("Czas (godziny)")
ax.set_ylabel("Zanieczyszczenie w zbiorniku (uncje)")
ax.grid(True)

# Rysuj krzywe Etapu 1 i Etapu 2
ax.plot(sol_etap1_stop.t, sol_etap1_stop.y[0], label="Zanieczyszczenie (Etap 1)", color='blue')
ax.plot(sol_etap2.t, sol_etap2.y[0], label="Zanieczyszczenie (Etap 2)", color='green')
ax.axvline(x=t_m, color='red', linestyle='--', label=f"t_m = {t_m:.2f} godzin")

# Dodaj legendę
ax.legend()

# Czerwona kropka animowana
red_dot, = ax.plot([], [], 'ro', label="Aktualne zanieczyszczenie")

def init():
    red_dot.set_data([], [])
    return red_dot,

def update(frame):
    red_dot.set_data([total_time[frame]], [total_Q[frame]])  # Wymaga list dla x i y
    return red_dot,

# Liczba klatek równa liczbie punktów czasowych
frames = len(total_time)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=20)

# Wyświetl animację
plt.show()
