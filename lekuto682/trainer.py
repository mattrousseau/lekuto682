from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

class Trainer():
    def train(self):
        scaler = StandardScaler()
        ohe = OneHotEncoder()
        model = LinearRegression()
