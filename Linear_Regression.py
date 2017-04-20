import numpy as np
from sklearn import linear_model
from scipy import stats
from sklearn.metrics import r2_score
from firebase import firebase

url = "https://iot-dw-1d-2017.firebaseio.com/" # URL to Firebase database
token = "0lYSxo2k1Jrr3i3rxhyb3IFy3kTKEAsXP39n3mpV" # unique token used for authentication
firebase = firebase.FirebaseApplication(url, token)
class LinearRegression(linear_model.LinearRegression):
    """
    LinearRegression class after sklearn's, but calculate t-statistics
    and p-values for model coefficients (betas).
    Additional attributes available after .fit()
    are `t` and `p` which are of the shape (y.shape[1], X.shape[1])
    which is (n_features, n_coefs)
    This class sets the intercept to 0 by default, since usually we include it
    in X.
    """

    def _init_(self, *args, **kwargs):  
        if not "fit_intercept" in kwargs:
            kwargs['fit_intercept'] = False
        super(LinearRegression, self)\
                ._init_(*args, **kwargs)

    def fit(self, X, y, n_jobs=1):
        self = super(LinearRegression, self).fit(X, y, n_jobs)

        sse = np.sum((self.predict(X) - y) ** 2, axis=0) / float(X.shape[0] - X.shape[1])
        se = np.array([np.sqrt(np.diagonal(sse * np.linalg.inv(np.dot(X.T, X))))])
        self.t = self.coef_ / se
        self.p = 2 * (1 - stats.t.cdf(np.abs(self.t), y.shape[0] - X.shape[1]))
        return self
def exponent(x,n):       #find any list of x's to the power of n, this helps us to do polynomial regression as well
    for i in range(len(x)):
        # if x[i] < 0 and n%2 == 0:
        #     x[i] = -x[i]**n
        # else:
        x[i] = x[i]**n
    return x

x = [[-4,2,-1,12,15,-5,-3,1,-5,25],[1.834,400,1.834,220,1.834,250,150,400,320,0]]   # x is our independent variables, this is a list of sensor inputs for different images
y = [1.8666666666666667,3.533333333333333,1.3333333333333335,4.0,0.8666666666666667,3.6,3.4,3.533333333333333,3.2,0] # y is priority level of a bin, this is gotten through survey randomized 

#numbers, therefore we would have our points on the graph each representing: ultrasonic reading, methane reading, corresponding to a priority level(gotten from people's references)
#x.append(exponent(x[0],2))

x.append(x[0])
x.append(x[1])

x_list = np.array(x)  # preparing the inputs of linear regression
y_list = np.array(y)
x_list[0] = exponent(x_list[0],2)  # we found this order by trying multiple types of input, we realize that second order gives us a very good R squared value.
x_list[1] = exponent(x_list[1],2)
clf = LinearRegression()
clf.fit(np.transpose(x_list), np.transpose(y_list))  #this helps us finish the linear regression.


print clf.coef_  # now the attribute coef_ represents the coefficients in front of each variable 
coeffs = []  #make coeffs a normal list, because firebase does not take in numpy arrays
for i in clf.coef_:
    coeffs.append(i)

firebase.put('/','coefficients',coeffs)
#put the coefficients as a list to firebase

points = []
R1 = 0
for j in range(len(x_list[0])):
    for i in range(len(clf.coef_)):
        R1 += clf.coef_[i]*x_list[i][j]

    points.append(R1)
    R1 = 0              # This appends all the fitted points to a two dimensional list
def R_squared(x,y):   # This helps us get R squared value, if we want we can also get standard error and p value, etc.
    slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)
    return r_value**2
#These lines of code helps us get the R squared value to make sure that the algorithm we fit to the points is close enough

