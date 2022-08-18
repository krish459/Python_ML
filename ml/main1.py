import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error


diabetes = datasets.load_diabetes()


# print(diabetes.keys())
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])


diabetes_X = np.array([[1],[2],[3]])
# print(diabetes_X)

diabetes_X_train = diabetes_X
diabetes_X_test = diabetes_X

diabetes_y_train = np.array([3,2,4])
diabetes_y_test = np.array([3,2,4])


model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_predict = model.predict(diabetes_X_test)

print("Mean sqaured error is : ",mean_squared_error(diabetes_y_test, diabetes_y_predict))

print("Weights: ",model.coef_)
print("Intercept : ",model.intercept_)

plt.scatter(diabetes_X_test, diabetes_y_test)
plt.plot(diabetes_X_test, diabetes_y_predict)
plt.show()
# Mean sqaured error is :  3035.060115291269
# Weights:  [941.43097333]
# Intercept :  153.39713623331644
