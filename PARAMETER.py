import numpy as np
from scipy.optimize import curve_fit

Na , Naerr = np.loadtxt("Na.csv",unpack=True,delimiter=',')
Red , Rerr = np.loadtxt("R.csv",unpack=True,delimiter=',')
Blue , Berr = np.loadtxt("B.csv",unpack=True,delimiter=',')
Violet , Verr = np.loadtxt("P.csv",unpack=True,delimiter=',')

orderNa = np.arange(-4,5,1)
orderR = np.arange(-2,4,1)
orderB = np.arange(-2,5,1)
orderV = np.arange(-2,3,1)

def N(p,Y,err,l):
    def Bright_det(p,N):
         Y = p * l * N
         return Y
    N, Nmat = curve_fit(Bright_det , p , Y , sigma = err)
    Nerr = np.sqrt(np.diag(Nmat))
    return N, Nerr

N , Nerr = N(orderNa,Na,Naerr,589.6*10**-9)
print(N,Nerr)

def R(p,Y,err,N):
    def Bright_det(p,l):
        Y = p * l * N
        return Y
    R, Rmat = curve_fit(Bright_det , p , Y , sigma = err)
    Rerr = np.sqrt(np.diag(Rmat))
    return R, Rerr

Rr , Rrerr = R(orderR,Red,Rerr,N)
Rb , Rberr = R(orderB,Blue,Berr,N)
Rv , Rverr = R(orderV,Violet,Verr,N)
print(Rr , Rrerr,
      Rb , Rberr,
      Rv , Rverr)

def Rydburg(level,lam,err):
    def Balmer(level,R):
        lam = R * level
        return lam
    C, Cmat = curve_fit(Balmer , level , lam , sigma = err)
    Cerr = np.sqrt(np.diag(Cmat))
    return C , Cerr

Level = np.array([0.138888889 , 0.1875 , 0.21])
Lam =  np.array([1.53*10**6 , 2.06*10**6 , 2.30*10**6])
Lamerr =  np.array([1.19*10**3 , 1.59*10**-10 , 2.42*10**-10])

rydburg , rydburgerr = Rydburg(Level,Lam,Lamerr)
print(rydburg , rydburgerr)
