```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class MarketAnalysis:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = pd.read_csv(data_file)
        self.model = LinearRegression()

    def preprocess_data(self):
        self.data = self.data.dropna()
        self.X = self.data.drop('MarketShare', axis=1)
        self.y = self.data['MarketShare']

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=0)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def predict_market_share(self):
        self.y_pred = self.model.predict(self.X_test)
        return self.y_pred

    def get_accuracy(self):
        return metrics.r2_score(self.y_test, self.y_pred)

    def analyze_market(self):
        self.preprocess_data()
        self.split_data()
        self.train_model()
        return self.get_accuracy()

if __name__ == "__main__":
    market_analysis = MarketAnalysis("market_data.csv")
    accuracy = market_analysis.analyze_market()
    print(f"Market Analysis Model Accuracy: {accuracy}")
```