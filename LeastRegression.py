import matplotlib.pyplot as mtpl
import numpy as np
from scipy.optimize import curve_fit

data = np.loadtxt("DATA1.csv",unpack=True,delimiter=',')
errv5 , errv10 , errv15 = np.loadtxt("DATA_ERROR1.csv",unpack=True)

oNL5 , PNL5 , PNL5err = np.loadtxt("PNL5.csv",unpack = True,delimiter=",")
oND5 , PND5 , PND5err = np.loadtxt("PND5.csv",unpack = True,delimiter=",")
oNL10 , PNL10 , PNL10err = np.loadtxt("PNL10.csv",unpack = True,delimiter=",")
oND10 , PND10 , PND10err = np.loadtxt("PND10.csv",unpack = True,delimiter=",")
oNL15 , PNL15 , PNL15err = np.loadtxt("PNL15.csv",unpack = True,delimiter=",")
oND15 , PND15 , PND15err = np.loadtxt("PND15.csv",unpack = True,delimiter=",")
oPL5 , PPL5 , PPL5err = np.loadtxt("PPL5.csv",unpack = True,delimiter=",")
oPD5 , PPD5 , PPD5err = np.loadtxt("PPD5.csv",unpack = True,delimiter=",")
oPL10 , PPL10 , PPL10err =  np.loadtxt("PPL10.csv",unpack = True,delimiter=",")
oPD10 , PPD10 , PPD10err = np.loadtxt("PPD10.csv",unpack = True,delimiter=",")
oPL15 , PPL15 , PPL15err = np.loadtxt("PPL15.csv",unpack = True,delimiter=",")
oPD15 , PPD15 , PPD15err = np.loadtxt("PPD15.csv",unpack = True,delimiter=",")

oA5 , pA5 = np.loadtxt("AN5.csv",unpack=True,delimiter=',')
oA10 , pA10 = np.loadtxt("AN10.csv",unpack=True,delimiter=',')
oA15 , pA15 = np.loadtxt("AN15.csv",unpack=True,delimiter=',')

#import all data from a .csv document
o1 , V1 , PL1 , PD1 , o2 , V2 , PL2 , PD2 , o3 , V3 , PL3 , PD3 = data

#firstly plot the graph without trend showing, in order to find out guessed parameters
mtpl.figure()
mtpl.xlim(100,310)
mtpl.ylim(3,15)

#mtpl.figure()
#a = mtpl.plot(o1,V1,".")
#b = mtpl.plot(o2,V2,".")
#c = mtpl.plot(o3,V3,".")
#mtpl.savefig("V.jpg")

#.figure()
#a = mtpl.plot(o1,PL1,".")
#b = mtpl.plot(o2,PL2,".")
#c = mtpl.plot(o3,PL3,".")
#mtpl.savefig("PL.jpg")

#mtpl.figure()
#a = mtpl.plot(o1,PD1,".")
#b = mtpl.plot(o2,PD2,".")
#c = mtpl.plot(o3,PD3,".")
#mtpl.savefig("PD.jpg")

pgv5 = [1.47 , 210000]
pgv10 = [1.64 , 205*10**3]
pgv15 = [1.755 , 195*10**3]

def R_parameter(o,V,R,error_bar,para_guess):
    def amplitude1(o,E,O):
        V = E / (10**-9 * (o**2 * R**2 + 0.022**2 * (o**2 - O**2)**2)**(1/2))
        return V
    P, CM = curve_fit(amplitude1 , o , V , para_guess , sigma = error_bar , method='trf')
    Error = np.sqrt(np.diag(CM))
    return P , Error

def P_parameter(o,y,error_bar,para_guess):
    def amplitude2(o,R):
        y = np.arctan(R / (o * 0.022 - 1 / (o * 10**-9)))
        return y
    P, CM = curve_fit(amplitude2 , o , y , para_guess , sigma = error_bar)
    Error = np.sqrt(np.diag(CM))
    return P , Error

def PA(o,y,para_guess):
    def amplitude2(o,R):
        y = np.arctan(R / (o * 0.022 - 1 / (o * 10**-9)))
        return y
    P, CM = curve_fit(amplitude2 , o , y , para_guess , method='trf')
    Error = np.sqrt(np.diag(CM))
    return P , Error

E5 = R_parameter(o1,V1,500,errv5,pgv5)
E10 = R_parameter(o2,V2,1000,errv10,pgv10)
E15 = R_parameter(o3,V3,1500,errv15,pgv15)

pnl5 = P_parameter(oNL5 , PNL5 , PNL5err , 500)
pnl10 = P_parameter(oNL10 , PNL10 , PNL10err , 1000)
pnl15 = P_parameter(oNL15 , PNL15 , PNL15err , 1500)

ppl5 = P_parameter(oPL5 , PPL5 , PPL5err , 500)
ppl10 = P_parameter(oPL10 , PPL10 , PPL10err , 1000)
ppl15 = P_parameter(oPL15 , PPL15 , PPL15err , 1500)

pnd5 = P_parameter(oND5 , PND5 , PND5err , 500)
pnd10 = P_parameter(oND10 , PND10 , PND10err , 1000)
pnd15 = P_parameter(oND15 , PND15 , PND15err , 1500)

ppd5 = P_parameter(oPD5 , PPD5 , PPD5err , 500)
ppd10 = P_parameter(oPD10 , PPD10 , PPD10err , 1000)
ppd15 = P_parameter(oPD15 , PPD15 , PPD15err , 1500)

pa5 = PA(oA5 , pA5 , 500)
pa10 = PA(oA10 , pA10 , 1000)
pa15 = PA(oA15 , pA15 , 1500)

#PA5 = P_AUTO(omega5,A5,pgp5)
#PA10 = P_AUTO(omega10,A10,pgp10)
#PA15 = P_AUTO(omega15,A15,pgp15)

print(E5 , E10 , E15)
print(f"for L method, negative side have {pnl5},{pnl10},{pnl15}")
print(f"for L method, positive side have {ppl5},{ppl10},{ppl15}")
print(f"for D method, negative side have {pnd5},{pnd10},{pnd15}")
print(f"for D method, positive side have {ppd5},{ppd10},{ppd15}")
print(f"for A method, negative side have {pa5},{pa10},{pa15}")
print(f"for A method, positive side have {pa5},{pa10},{pa15}")

def chi2(o,y_data,R):
    y_fit = np.arctan(R / (o * 0.022 - 1 / (o * 10**-9)))
    mean = np.mean(y_data)
    d = (y_data - y_fit)**2
    D = (y_data - mean)**2
    r2 = 1 - np.sum(d) / np.sum(D)
    return r2

print(chi2(oA5 , pA5 , 720.81899918))
print(chi2(oA10 , pA10 , 1229.87711176))
print(chi2(oA15 , pA15 , 1745.62097194))
