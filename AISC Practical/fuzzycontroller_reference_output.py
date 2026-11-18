import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Input and output variables
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# ---------------------------------
# Temperature Membership Functions
# ---------------------------------
temp['cold'] = fuzz.trimf(temp.universe, [0, 0, 20])
temp['cool'] = fuzz.trimf(temp.universe, [10, 20, 30])
temp['warm'] = fuzz.trimf(temp.universe, [20, 30, 40])
temp['hot'] = fuzz.trimf(temp.universe, [30, 40, 40])

# ---------------------------------
# Humidity Membership Functions
# (kept as in the original program)
# ---------------------------------
humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [25, 50, 75])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# ---------------------------------
# Fan Speed Membership Functions
# ---------------------------------
fan['off'] = fuzz.trimf(fan.universe, [0, 0, 25])
fan['low'] = fuzz.trimf(fan.universe, [10, 30, 50])
fan['medium'] = fuzz.trimf(fan.universe, [35, 55, 75])
fan['high'] = fuzz.trimf(fan.universe, [60, 80, 100])
fan['max'] = fuzz.trimf(fan.universe, [75, 100, 100])

# ---------------------------------
# Fuzzy Rules
# Original rule logic is retained:
# low temperature  -> cold
# medium temperature -> warm
# high temperature -> hot
# slow / medium / fast fan outputs
# are represented by low / medium / high.
# ---------------------------------
rules = [
    ctrl.Rule(temp['cold'] & humidity['low'], fan['low']),
    ctrl.Rule(temp['cold'] & humidity['high'], fan['medium']),
    ctrl.Rule(temp['warm'], fan['medium']),
    ctrl.Rule(temp['hot'], fan['high'])
]

# Create control system and simulation
system = ctrl.ControlSystem(rules)
simulation = ctrl.ControlSystemSimulation(system)

# Input values
temperature_value = 35
humidity_value = 80

simulation.input['temperature'] = temperature_value
simulation.input['humidity'] = humidity_value

# Calculate output
simulation.compute()

# ---------------------------------
# Plot 1: Temperature Membership Functions
# ---------------------------------
temp.view()
plt.title("Temperature Membership Functions")
plt.xlabel("temperature")
plt.ylabel("Membership")
plt.tight_layout()

# ---------------------------------
# Plot 2: Fan Speed Membership Functions
# ---------------------------------
fan.view()
plt.title("Fan Speed Membership Functions")
plt.xlabel("fan_speed")
plt.ylabel("Membership")
plt.tight_layout()

# Display both separate graphs
plt.show()

# Display simulation results
print("\n--- Fuzzy AC Controller Simulation ---")
print("Temperature:", temperature_value)
print("Humidity:", humidity_value)
print("Fan Speed:", round(simulation.output['fan_speed'], 2))
