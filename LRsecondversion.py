import numpy as np
from sklearn import linear_model
from scipy import stats
from firebase import firebase
from datetime import datetime
from threading import Timer
import time

url = "https://iot-dw-1d-2017.firebaseio.com/" # URL to Firebase database
token = "0lYSxo2k1Jrr3i3rxhyb3IFy3kTKEAsXP39n3mpV" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

print "Reading from my database."
infrared =  firebase.get('/Infrared') # get the value from the node age
methane =  firebase.get('/Methane')
ultrasound = firebase.get('Ultrasound')
if infrared == '':
    infrared = 0
if methane == '':
    methane = 0
if ultrasound == '':
    ultrasound = 0


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
def exponent(x,n):
    for i in range(len(x)):
        # if x[i] < 0 and n%2 == 0:
        #     x[i] = -x[i]**n
        # else:
        x[i] = x[i]**n
    return x
def main():

    x = [[-4,2,-1,12,15,-5,-3,1,-5,25],[1.834,400,1.834,220,1.834,250,150,400,320,0]]
    y = [1.8666666666666667,3.533333333333333,1.3333333333333335,4.0,0.8666666666666667,3.6,3.4,3.533333333333333,3.2,0]
    #x.append(exponent(x[0],2))
    x.append(x[0])
    x.append(x[1])

    x_list = np.array(x)
    y_list = np.array(y)
    x_list[0] = exponent(x_list[0],2)
    x_list[1] = exponent(x_list[1],2)
    clf = LinearRegression()
    clf.fit(np.transpose(x_list), np.transpose(y_list))

    print clf.coef_

    points = []
    R1 = 0
    for j in range(len(x_list[0])):
        for i in range(len(clf.coef_)):
            R1 += clf.coef_[i]*x_list[i][j]

        points.append(R1)
        R1 = 0
    def R_squared(x,y):
        slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)
        return r_value**2
    #print R_squared(points,y_list)




    def algo(x,y):
        return clf.coef_[0]*x**2-clf.coef_[2]*x+clf.coef_[1]*y**2+clf.coef_[3]*y,25-x,y
    def Implementation():
        while True:

            P_A,height_A,methane_A = algo(0,methane)
            P_B,heihgt_B,methane_B = algo(0,0)
            P_C,height_C,methane_C = algo(0,0)
            dict_routes = {}
            print P_A,P_B,P_C

            P_BAC = 1/((6*P_B+15*P_A+28*P_C)*34)
            P_ABC = 1/((12*P_A+21*P_B+34*P_C)*40)
            P_BCA = 1/((6*P_B+20*P_C+33*P_A)*39)
            P_ACB = 1/((12*P_A+25*P_C+38*P_B)*39)
            P_CBA = 1/((12*P_C+25*P_B+34*P_A)*40)
            P_CAB = 1/((12*P_C+24*P_A+33*P_B)*36)

            dict_routes['BAC'] = P_BAC
            dict_routes['CAB'] = P_CAB
            dict_routes['CBA'] = P_CBA
            dict_routes['ACB'] = P_ACB
            dict_routes['BCA'] = P_BCA
            dict_routes['ABC'] = P_ABC

            time.sleep(5)

            def keywithmaxval(d):
                """ a) create a list of the dict's keys and values;
                    b) return the key with the max value"""
                v = list(d.values())
                k = list(d.keys())
                return k[v.index(max(v))]

            print keywithmaxval(dict_routes)
    t = Timer(1, Implementation)
    t.start()

#code to make it run at 7am everyday

# x = datetime.today()
# print x.second
#
# y = x.replace(day=x.day,hour=x.hour,minute=x.minute+1,second=x.second,microsecond=x.microsecond)
# print y
# delta_t = y-x
# secs = delta_t.seconds+1
# print secs
# while True:
#     t = Timer(1,main)
#     t.start()
main()