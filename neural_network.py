#%%
import numpy as np
import sklearn
import scipy.io as sio
import tkinter as tk
from tkinter.filedialog import askopenfilename
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
#%% Read file

root = tk.Tk()
filename = askopenfilename()
print(filename)
root.withdraw()

mat_contents = sio.loadmat(filename)
data = mat_contents['data']
Xs = data[:,1:3]
ys = data[:,4:5]
N = len(data)

#%%
train_portion = 0.8
shuffled = data[np.random.permutation(N),:]
train_test_cutoff = int(np.floor(N*train_portion))
train_data = shuffled[0:train_test_cutoff-1,:]
test_data = shuffled[train_test_cutoff:-1,:]
y_train = train_data[:,-3:-1]
y_test = test_data[:,-3:-1]
X_train = train_data[:,0:-2]
X_test = test_data[:,0:-2]

#%% Init Model
kernel = 1.0 * Matern(length_scale=1.0, length_scale_bounds=(1e-1, 10.0),
                        nu=1.5)
gp1 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=20)
gp2 = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=20)
#%% Train Model
gp1.fit(X_train,y_train[:,0].reshape(-1,1))
gp2.fit(X_train,y_train[:,1].reshape(-1,1))
#%% Make predicitons

y_pred_1, std_mimo1 = gp1.predict(X_test, return_std=True)
y_pred_2, std_mimo2 = gp2.predict(X_test, return_std=True)

#%% Evaluate predictions
