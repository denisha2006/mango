import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

# Temperature range
x = np.arange(0, 101, 1)

# -------------------------------
# 1. Membership Functions
# -------------------------------

# Triangular Membership Functions
cold = fuzz.trimf(x, [0, 20, 40])
warm = fuzz.trimf(x, [30, 50, 70])
hot = fuzz.trimf(x, [60, 80, 101])

# Trapezoidal Membership Function
cool = fuzz.trapmf(x, [0, 10, 30, 45])

# Gaussian Membership Function
comfortable = fuzz.gaussmf(x, 22, 5)

# Sigmoid Membership Function
very_hot = fuzz.sigmf(x, 70, 0.3)


# -------------------------------
# 2. Plot Each MF Separately
#    (Four separate graph areas)
# -------------------------------

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Graph 1: Triangular MF
ax[0, 0].plot(x, cold, label="Cold")
ax[0, 0].plot(x, warm, label="Warm")
ax[0, 0].plot(x, hot, label="Hot")
ax[0, 0].set_title("Triangular MF - Temperature")
ax[0, 0].set_xlabel("Temperature (°C)")
ax[0, 0].set_ylabel("Membership (µ)")
ax[0, 0].legend()
ax[0, 0].grid(True)

# Graph 2: Trapezoidal MF
ax[0, 1].plot(x, cool, label="Cool")
ax[0, 1].set_title("Trapezoidal MF - Cool")
ax[0, 1].set_xlabel("Temperature (°C)")
ax[0, 1].set_ylabel("Membership (µ)")
ax[0, 1].legend()
ax[0, 1].grid(True)

# Graph 3: Gaussian MF
ax[1, 0].plot(x, comfortable, label="Comfortable")
ax[1, 0].set_title("Gaussian MF - Comfortable")
ax[1, 0].set_xlabel("Temperature (°C)")
ax[1, 0].set_ylabel("Membership (µ)")
ax[1, 0].legend()
ax[1, 0].grid(True)

# Graph 4: Sigmoid MF
ax[1, 1].plot(x, very_hot, label="Very Hot")
ax[1, 1].set_title("Sigmoid MF - Very Hot")
ax[1, 1].set_xlabel("Temperature (°C)")
ax[1, 1].set_ylabel("Membership (µ)")
ax[1, 1].legend()
ax[1, 1].grid(True)

fig.suptitle("Fuzzy Membership Functions", fontsize=14)
plt.tight_layout()
plt.show()


# -------------------------------
# 3. Fuzzy Set Operations
# -------------------------------

union = np.fmax(cold, warm)
intersection = np.fmin(cold, warm)
complement = 1 - cold

plt.figure(figsize=(10, 6))
plt.plot(x, union, label="Union (Cold OR Warm)")
plt.plot(x, intersection, label="Intersection (Cold AND Warm)")
plt.plot(x, complement, label="Complement (NOT Cold)")

plt.title("Fuzzy Set Operations")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership (µ)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# -------------------------------
# 4. Membership Values at 35°C
# -------------------------------

t = 35

print("\nAt Temperature =", t, "°C:")
print("Cold =", round(fuzz.interp_membership(x, cold, t), 3))
print("Warm =", round(fuzz.interp_membership(x, warm, t), 3))
print("Hot  =", round(fuzz.interp_membership(x, hot, t), 3))
