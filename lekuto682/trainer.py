from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class Trainer():
    def train(self):
        scaler = StandardScaler()
        model = LinearRegression()
