
import numpy as np
import matplotlib.pyplot as plt

class SLP:
    def __init__(self):
        self.lr = 0.5
        self.epoch = 100

    def step(self, z):
        return np.where(z >= 0, 1, 0)

    def train(self, X, Y):
        self.w = np.zeros(2)
        self.b = 0

        print("\n=== Perceptron Training: AND Gate ===")

        for epoch in range(1, self.epoch + 1):

            error = 0

            for xi, yi in zip(X, Y):

                pred = self.step(np.dot(xi, self.w) + self.b)
                err = yi - pred

                self.w += self.lr * err * xi
                self.b += self.lr * err

                error += int(err != 0)

            print(f"Epoch {epoch}: Errors={error}, "
                  f"w={self.w}, b={self.b:.2f}")

            if error == 0:
                break

    def predict(self, xi):
        return self.step(np.dot(xi, self.w) + self.b)


# AND Gate Dataset
X = np.array([[1, 0], [0, 1], [0, 0], [1, 1]])
Y = np.array([0, 0, 0, 1])


# Create and train model
model = SLP()
model.train(X, Y)


# Predictions
print("\nPredictions:", model.predict(X))
print("Expected:    ", Y)


# Plot Decision Boundary
x_line = np.linspace(-0.5, 1.5, 100)
y_line = -(model.w[1] * x_line + model.b) / model.w[0]

plt.plot(x_line, y_line, label="Decision Boundary")
plt.scatter(X[:, 0], X[:, 1], c=Y)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("SLP Decision Boundary - AND Gate")
plt.legend()
plt.grid()

plt.show()
