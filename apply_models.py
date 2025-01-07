
import mlmodels_file as modls
from sklearn.linear_model import LinearRegression

file_path = "Global Health Statistics.csv"
model_to_apply = LinearRegression()

X_train, X_test, y_train, y_test = modls.preprocess_data(
    file_path,
    ['Average Treatment Cost (USD)', 'Prevalence Rate (%)'],
    'Recovery Rate (%)'
)
X_train_scaled, X_test_scaled = modls.scale_features(X_train,X_test)

model = modls.train_model(model_to_apply, X_train_scaled, y_train)
metrics = modls.evaluate_model(model, X_test_scaled, y_test)

pred1 = model.predict([[100, 50]])

print(pred1)
