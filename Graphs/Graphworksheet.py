import matplotlib.pyplot as plt


days = ["monday", "tuesday", "wednesday"]
reps = [1, 2, 3]
plt.plot(days, reps)
plt.xlabel("reps")
plt.ylabel("days")
plt.title("workout")
plt.show()
