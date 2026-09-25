import numpy as np

#Financial inputs
S = float(input("Current cryptocurrency price (S) = "))
K = float(input("Strike price (K) = "))
T = float(input("Time to maturity (T) = "))
r = float(input("Risk-free rate (r) = "))
div = float(input("Dividend yield (div) = "))
sig = float(input("Volatility (sig) = "))

#Numerical inputs
N = int(input("Time steps (N) = "))
Nj = int(input("Price steps (Nj) = "))
dx = float(input("Grid spacing (dx) = "))

#Option specification
option_type = int(input("Option type (0 = CALL, 1 = PUT) = "))
exercise_style = int(input("Exercise style (0 = EUROPEAN, 1 = AMERICAN) = "))


#Compute constant
dt = T/N
nu = r - div - 0.5*sig**2
edx = np.exp(dx)
pu = -0.25*dt*((sig/dx)**2 + nu/dx)
pm = 1 + 0.5*dt*(sig/dx)**2 + 0.5*r*dt
pd = -0.25*dt*((sig/dx)**2 - nu/dx)

#initializing
inde = float(S*np.exp(-Nj*dx))
apm = [inde]
ovm = []
ovmp = []

for j in range(1, 2*Nj+1):
    ri = apm[j-1]*edx
    apm.append(ri)

if option_type == 0:
    for j in range(1, 2*Nj+2):
        rj = max(0, apm[j-1] - K)
        ovm.append(rj)
elif option_type == 1:
    for j in range(1, 2*Nj+2):
        rj = max(0, K - apm[j-1])
        ovm.append(rj)


#boundary condition
if option_type == 0:
    lamL = 0.0
    lamU = apm[-1] - apm[-2]
elif option_type == 1:
    lamL = -1*(apm[1]-apm[0])
    lamU = 0.0

#lattice & boundary
def solve_CNtri_system():
    ovmp = []
    pmp = []
    pp = []
    pmp0 = pm + pd
    pp0 = -pu*ovm[2] - (pm-2)*ovm[1] - pd*ovm[0] + pd*lamL
    pmp.append(pmp0)
    pp.append(pp0)
    for j in range(2,2*Nj):
        pmpj = pm - pu*pd/pmp[j-2]
        ppj = -pu*ovm[j+1] - (pm-2)*ovm[j] - pd*ovm[j-1] - pp[j-2]*pd/pmp[j-2]
        pmp.append(pmpj)
        pp.append(ppj)
    C = (pp[2*Nj-2] + pmp[2*Nj-2]*lamU)/(pu + pmp[2*Nj-2])
    C1 = C - lamU
    ovmp.append(C)
    ovmp.append(C1)
    for j in range(1, 2*Nj-1):
        dov = (pp[2*Nj-2-j] - pu*ovmp[j])/pmp[2*Nj-2-j]
        ovmp.append(dov)
    C2 = (-pu*ovm[2] - (pm-2)*ovm[1] - pd*ovm[0] - pu*ovmp[-2] - pm*ovmp[-1])/pd
    ovmp.append(C2)
    return ovmp

#exercise determine
if exercise_style == 0:
    for i in range(1, N+1):
        ovmp = solve_CNtri_system()
        for j in range(0, 2*Nj+1):
            ovm[j] = ovmp[-j-1]
elif exercise_style == 1:
    if option_type == 0:
        for i in range(1, N+1):
            ovmp = solve_CNtri_system()
            for j in range(0, 2*Nj+1):
                ovm[j] = max(ovmp[-j-1], apm[j] - K)
    elif option_type == 1:
        for i in range(1, N+1):
            ovmp = solve_CNtri_system()
            for j in range(0, 2*Nj+1):
                ovm[j] = max(ovmp[-j-1], K - apm[j])

Option_value = ovm[Nj]
print(Option_value)

