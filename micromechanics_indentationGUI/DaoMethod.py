""" Module of Dao method correcting pile-up effect """

from scipy.optimize import curve_fit
import pylab as plt
import numpy as np

def LoadingCurveFunc(h, C, A, B):
  """
  function of loading curve
  """
  B=0
  return C * (h + A)**2 + B

def LoadingCurveFunc_Inverse(p, C, A, B):
  """
  inverse function of loading curve
  """
  B=0
  return ((p-B)/C)**0.5 - A

def func_LoadingWork(h0, h1, C, A, B):
  """
  Returns:
    float: the work of loading curve [mN*µm]
  """
  B=0
  LoadingWork = C/3*(h1+A)**3 + B*h1 - C/3*(h0+A)**3 - B*h0
  return LoadingWork

def func_HoldingWork(h0, h1, p0):
  """
  Returns:
    float: the work of holding curve [mN*µm]
  """
  HoldingWork = (h1-h0)*p0
  return HoldingWork

def func_unLoadingWork(h0,h1,B,hf,m):
  """
  Returns:
    float: the work of unloading curve [mN*µm]
  """
  unLoadingWork = B/(m+1)*(h1-hf)**(m+1) - B/(m+1)*(h0-hf)**(m+1)
  return unLoadingWork

def func_Cheng1998(h,A,B,C):
  """
  Cheng 1998
  """
  return A*h**2 + B*h**1 + C

def func_Dao2001(h,A,B,C,D,E):
  """
  Dao 2021
  """
  return A*h**4 + B*h**3 + C*h**2 + D*h**1 + E



def Dao(self, plot=False, PRINT=False):
  """
  Dao method
  """
  if PRINT:
    print('=================Before Dao Correction==============')
    print('hardness',self.hardness)
    print('modulus',self.modulus)
    print('====================================================')
  h_loading = self.h[self.iLHU[0][0]:self.iLHU[0][1]]
  p_loading = self.p[self.iLHU[0][0]:self.iLHU[0][1]]
  # mask = np.where((h_loading-h_loading[0])>0.07)
  mask = np.where((h_loading-h_loading[0])>0.05)
  h_loading = h_loading[mask]
  p_loading = p_loading[mask]
  popt_loading, _ = curve_fit(LoadingCurveFunc, h_loading, p_loading) #pylint: disable=unbalanced-tuple-unpacking
  hmax_loading = LoadingCurveFunc_Inverse(np.max(self.p),popt_loading[0], popt_loading[1], popt_loading[2])

  if plot:
    fig, ax = plt.subplots(2,1,sharex=True, gridspec_kw={'hspace':0, 'height_ratios': [3, 1]},figsize=(6, 6))
    ax0 = ax[0]
    ax1 = ax[1]
    ax0.scatter(self.h, self.p, color='tab:gray')
    ax0.scatter(h_loading, p_loading, s=5)
    h_new = np.arange(-popt_loading[1],hmax_loading+0.0001,0.0001)
    p_new = LoadingCurveFunc(h_new, popt_loading[0], popt_loading[1], popt_loading[2])
    ax0.plot(h_new, p_new, color='tab:orange')
    ax0.set_xlim(-popt_loading[1],np.max(self.h)*1.02)
    calculatedP = LoadingCurveFunc(h_loading,popt_loading[0],popt_loading[1], popt_loading[2])
    error = (calculatedP-p_loading)/p_loading*100
    ax1.scatter(h_loading,error,color='tab:orange',s=5)

  #Unloading curve
  h_unloading = self.h[self.iLHU[0][2]:self.iLHU[0][3]]
  p_unloading = self.p[self.iLHU[0][2]:self.iLHU[0][3]]
  mask = np.where(p_unloading>p_loading[0])
  h_unloading = h_unloading[mask]
  p_unloading = p_unloading[mask]
  #initial values of fitting
  hf0    = h_unloading[-1]/1.1
  m0     = 1.5
  B0     = max(abs(p_unloading[0] / np.power(h_unloading[0]-hf0,m0)), 0.001)  #prevent neg. or zero
  bounds = [[0,0,0.8],[np.inf, max(np.min(h_unloading),hf0), 10]]
  popt_unloading, _ = curve_fit(self.unloadingPowerFunc, h_unloading,p_unloading,      # pylint: disable=unbalanced-tuple-unpacking
                        p0=[B0,hf0,m0], bounds=bounds,
                          maxfev=1000 )#set ftol to 1e-4 if accept more and fail less
  hmax_unloading = self.inverse_unloadingPowerFunc(p_loading[-1], B=popt_unloading[0], hf=popt_unloading[1], m=popt_unloading[2]) #!!!!!!
  if plot:
    ax0.scatter(h_unloading, p_unloading, s=5, color='tab:pink',zorder=2)
    h_new_unloading = np.arange(popt_unloading[1],hmax_unloading+0.0001,0.0001)
    p_new_unloading = self.unloadingPowerFunc(h_new_unloading,popt_unloading[0],popt_unloading[1],popt_unloading[2])
    ax0.plot(h_new_unloading,p_new_unloading,color='tab:red')
    # fitting error analysis
    calculatedP = self.unloadingPowerFunc(h_unloading,popt_unloading[0],popt_unloading[1],popt_unloading[2])
    error = (calculatedP-p_unloading)/p_unloading*100
    ax1.scatter(h_unloading,error,color='tab:red',s=5)
    # setting the Plot
    ax0.set_ylabel(r'Force [$\mathrm{mN}$]',fontsize=16)
    ax1.set_ylabel(r"$\frac{P_{cal}-P_{mea}}{P_{mea}}x100$ [%]",fontsize=16)
    ax1.set_xlabel(r'Depth [$\mathrm{\mu m}$]',fontsize=16)
    ax0.tick_params(axis='both', direction='in',labelsize=14)
    ax1.tick_params(axis='both', direction='in',labelsize=14)
    fig.tight_layout()

  # Loading-Holding-Unloading work
  W_loading = func_LoadingWork(h0=-popt_loading[1], h1=hmax_loading, C=popt_loading[0], A=popt_loading[1], B=popt_loading[2])
  # W_loading = func_LoadingWork(h0=-popt_loading[1], h1=hmax_loading, C=popt_loading[0], A=popt_loading[1], B=popt_loading[2])
  W_holding = func_HoldingWork(h0=hmax_loading, h1=hmax_unloading, p0 = np.max(self.p))
  W_unloading = func_unLoadingWork(h0=popt_unloading[1],h1=hmax_unloading,B=popt_unloading[0], hf=popt_unloading[1], m=popt_unloading[2])
  W_elastic = W_unloading
  W_plastic = W_loading + W_holding - W_unloading
  Ratio_Wplastic_Wtotal = W_plastic/(W_plastic+W_elastic)


  #Cheng1998 half-included angle = 68°
  data_Cheng1998 = np.loadtxt('micromechanics_indentationGUI/H_over_reE_vs_Wp_over_wt_Cheng1998.py',delimiter=';')
  popt_Cheng1998, _ = curve_fit(func_Cheng1998, data_Cheng1998[:,0],data_Cheng1998[:,1]) #pylint: disable=unbalanced-tuple-unpacking
  if plot:
    fig3,ax3=plt.subplots()
    ax3.scatter(data_Cheng1998[:,0],data_Cheng1998[:,1], facecolor='None', edgecolor='tab:orange')
    Ratio_Wplastic_Wtotal_new = np.arange(0.58,1,0.001)
    H_over_reE_new = func_Cheng1998(Ratio_Wplastic_Wtotal_new, popt_Cheng1998[0], popt_Cheng1998[1], popt_Cheng1998[2])
    ax3.plot(Ratio_Wplastic_Wtotal_new, H_over_reE_new, color='tab:orange', label='half-included angle = 68°\n (Cheng and Cheng, 1998)')

  # Dao 2001 half-included angle = 70.3°
  hr_over_hm = np.arange(0.7,0.99,0.01)
  Ratio_Wplastic_Wtotal_Dao2001 = 1.61217 * (1.13111 - 1.74756**(-1.49291*hr_over_hm**2.535334) - 0.075187 * hr_over_hm**1.135826 )
  H_over_reE_Dao2001 = 0.268536 * (0.9952495 - hr_over_hm)**1.1142735
  popt_Dao2001, _ = curve_fit(func_Dao2001, Ratio_Wplastic_Wtotal_Dao2001, H_over_reE_Dao2001) #pylint: disable=unbalanced-tuple-unpacking
  H_over_reE_Dao2001_fitted = func_Dao2001(Ratio_Wplastic_Wtotal_Dao2001, popt_Dao2001[0], popt_Dao2001[1], popt_Dao2001[2], popt_Dao2001[3], popt_Dao2001[4])
  if plot:
    ax3.scatter(Ratio_Wplastic_Wtotal_Dao2001, H_over_reE_Dao2001, facecolor='None', edgecolor='tab:blue')
    ax3.plot(Ratio_Wplastic_Wtotal_Dao2001, H_over_reE_Dao2001_fitted, color='tab:blue', label='half-included angle = 70.3°\n (Dao et al., 2001)')
    ax3.scatter(Ratio_Wplastic_Wtotal, self.hardness/self.modulusRed, color='tab:red', marker='s')
    # setting the Plot
    ax3.set_xlabel(r'$\frac{W_{\rm plastic}}{W_{\rm total}}$ [-]',fontsize=16)
    ax3.set_ylabel(r'$\frac{\rm Hardness}{\rm reduced\ Modulus}$ [-]',fontsize=16)
    ax3.tick_params(axis='both', direction='in',labelsize=14)
    ax3.legend(fontsize=14, frameon=False)
    fig3.tight_layout()
    plt.show()

  H_over_reE_calc = func_Dao2001(Ratio_Wplastic_Wtotal, popt_Dao2001[0], popt_Dao2001[1], popt_Dao2001[2], popt_Dao2001[3], popt_Dao2001[4])
  correctedArea = self.Ac * (self.hardness/self.modulusRed  / H_over_reE_calc)**2
  correctedHardness = np.max(self.p)/correctedArea
  correctedModulusRed = correctedHardness/H_over_reE_calc
  correctedModulus = self.YoungsModulus(correctedModulusRed)
  if PRINT:
    print('=================After Dao Correction==============')
    print('H_over_reE_calc',H_over_reE_calc)
    print('hardness',correctedHardness)
    print('modulus',correctedModulus)
    print('====================================================')
  self.Ac = correctedArea
  self.hardness = correctedHardness
  self.modulus = correctedModulus
  self.modulusRed = correctedModulusRed
