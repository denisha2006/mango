
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class MLP:
    def __init__(self):
        self.lr = 0.5
        self.epoch = 2000
        self.losses = []

    def train(self, X, Y):

        np.random.seed(1)

        self.w1 = np.random.randn(2, 2)
        self.w2 = np.random.randn(2, 1)

        self.b1 = np.zeros((1, 2))
        self.b2 = np.zeros((1, 1))

        print("\n=== MLP Training: Negation XOR ===")

        for epoch in range(1, self.epoch + 1):

            h = sigmoid(X @ self.w1 + self.b1)
            out = sigmoid(h @ self.w2 + self.b2)

            loss = np.mean((Y - out) ** 2)
            self.losses.append(loss)

            err = (out - Y) * out * (1 - out)
            dh = (err @ self.w2.T) * h * (1 - h)

            self.w2 -= self.lr * h.T @ err
            self.w1 -= self.lr * X.T @ dh

            self.b2 -= self.lr * err.sum(axis=0, keepdims=True)
            self.b1 -= self.lr * dh.sum(axis=0, keepdims=True)

            # Print loss after every 200 epochs
            if epoch % 200 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.6f}")

    def predict(self, X):

        h = sigmoid(X @ self.w1 + self.b1)
        out = sigmoid(h @ self.w2 + self.b2)

        return (out >= 0.5).astype(int)


# Negation XOR (XNOR) Dataset
X = np.array([
    [0, 0],[0, 1],[1, 0], [1, 1]])

Y = np.array([[1], [0], [0], [1]])


# Create and train model
model = MLP()
model.train(X, Y)


# Predictions
print("\nPredicted:")
print(model.predict(X).flatten())

print("\nExpected:")
print(Y.flatten())


# Plot Epoch vs Loss
plt.plot(range(1, len(model.losses) + 1), model.losses)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("MLP Training Loss - Negation XOR")

plt.xticks(np.arange(0, 3001, 500))
plt.grid()

plt.show()
