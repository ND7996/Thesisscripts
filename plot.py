import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.read_csv("2F8A_output1.log")
print("Contents in csv file:\n", df)

df.plot(x="Time (ps)", y="Potential Energy (kJ/mole)")
plt.show()
df.plot(x="Temperature (K)", y="Kinetic Energy (kJ/mole)", marker="o")
plt.show()



