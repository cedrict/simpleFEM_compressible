# Notebook to plot and examine the convergence rate of the strains and of $\phi$ with grid spacing


import numpy as np
import matplotlib.pyplot as plt


data1 = np.loadtxt("OUT/errors_spacing_strain_1.dat")
h = data1[:,0]
dxu_L1_1 = data1[:,1]
dxu_L2_1 = data1[:,2]
dxv_L1_1 = data1[:,3]
dxv_L2_1 = data1[:,4]
dyu_L1_1 = data1[:,5]
dyu_L2_1 = data1[:,6]
dyv_L1_1 = data1[:,7]
dyv_L2_1 = data1[:,8]
phi_L1_1 = data1[:,9]
phi_L2_1 = data1[:,10]


# In[16]:


data2 = np.loadtxt("OUT/errors_spacing_strain_2.dat")

dxu_L1_2 = data2[:,1]
dxu_L2_2 = data2[:,2]
dxv_L1_2 = data2[:,3]
dxv_L2_2 = data2[:,4]
dyu_L1_2 = data2[:,5]
dyu_L2_2 = data2[:,6]
dyv_L1_2 = data2[:,7]
dyv_L2_2 = data2[:,8]
phi_L1_2 = data2[:,9]
phi_L2_2 = data2[:,10]


# In[17]:


data3 = np.loadtxt("OUT/errors_spacing_strain_3.dat")

dxu_L1_3 = data3[:,1]
dxu_L2_3 = data3[:,2]
dxv_L1_3 = data3[:,3]
dxv_L2_3 = data3[:,4]
dyu_L1_3 = data3[:,5]
dyu_L2_3 = data3[:,6]
dyv_L1_3 = data3[:,7]
dyv_L2_3 = data3[:,8]
phi_L1_3 = data3[:,9]
phi_L2_3 = data3[:,10]


# In[18]:


data5 = np.loadtxt("OUT/errors_spacing_strain_4.dat")

dxu_L1_5 = data5[:,1]
dxu_L2_5 = data5[:,2]
dxv_L1_5 = data5[:,3]
dxv_L2_5 = data5[:,4]
dyu_L1_5 = data5[:,5]
dyu_L2_5 = data5[:,6]
dyv_L1_5 = data5[:,7]
dyv_L2_5 = data5[:,8]
phi_L1_5 = data5[:,9]
phi_L2_5 = data5[:,10]

x = np.log(h)


f,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))

ax1.plot(x,np.log(dxu_L1_1),"-+",label="Benchmark 1")
ax1.plot(x,np.log(dxu_L1_2),"-+",label="Benchmark 2")
ax1.plot(x,np.log(dxu_L1_3),"-+",label="Benchmark 3")
ax1.plot(x,np.log(dxu_L1_5),"-+",label="Benchmark 4")
ax1.legend()
ax1.set_xlabel("log(h)")
ax1.set_ylabel("log($e_{xx}$ $L_1$)")

ax2.plot(x,np.log(dyv_L1_1),"-+",label="Benchmark 1")
ax2.plot(x,np.log(dyv_L1_2),"-+",label="Benchmark 2")
ax2.plot(x,np.log(dyv_L1_3),"-+",label="Benchmark 3")
ax2.plot(x,np.log(dyv_L1_5),"-+",label="Benchmark 4")
ax2.legend()
ax2.set_xlabel("log(h)")
ax2.set_ylabel("log($e_{yy}$ $L_1$)")

ax3.plot(x,np.log(dxv_L1_1),"-+",label="Benchmark 1")
ax3.plot(x,np.log(dxv_L1_2),"-+",label="Benchmark 2")
ax3.plot(x,np.log(dxv_L1_3),"-+",label="Benchmark 3")
ax3.plot(x,np.log(dxv_L1_5),"-+",label="Benchmark 4")
ax3.legend()
ax3.set_xlabel("log(h)")
ax3.set_ylabel("log($e_{xy}$ $L_1$)")

ax4.plot(x,np.log(phi_L1_1),"-+",label="Benchmark 1")
ax4.plot(x,np.log(phi_L1_2),"-+",label="Benchmark 2")
ax4.plot(x,np.log(phi_L1_3),"-+",label="Benchmark 3")
ax4.plot(x,np.log(phi_L1_5),"-+",label="Benchmark 4")
ax4.legend()
ax4.set_xlabel("log(h)")
ax4.set_ylabel("log($\phi$ $L_1$)")

f.suptitle("L1 Norms for components of the strain rate tensor and $\phi$, for Benchmarks 1-4",fontsize=20,y=0.925)


f.savefig("Strain_Norms_L1.pdf")


f,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))

ax1.plot(x,np.log(dxu_L2_1),"-+",label="Benchmark 1")
ax1.plot(x,np.log(dxu_L2_2),"-+",label="Benchmark 2")
ax1.plot(x,np.log(dxu_L2_3),"-+",label="Benchmark 3")
ax1.plot(x,np.log(dxu_L2_5),"-+",label="Benchmark 4")
ax1.legend()
ax1.set_xlabel("log(h)")
ax1.set_ylabel("log($e_{xx}$ $L_2$)")

ax2.plot(x,np.log(dyv_L2_1),"-+",label="Benchmark 1")
ax2.plot(x,np.log(dyv_L2_2),"-+",label="Benchmark 2")
ax2.plot(x,np.log(dyv_L2_3),"-+",label="Benchmark 3")
ax2.plot(x,np.log(dyv_L2_5),"-+",label="Benchmark 4")
ax2.legend()
ax2.set_xlabel("log(h)")
ax2.set_ylabel("log($e_{yy}$ $L_2$)")

ax3.plot(x,np.log(dxv_L2_1),"-+",label="Benchmark 1")
ax3.plot(x,np.log(dxv_L2_2),"-+",label="Benchmark 2")
ax3.plot(x,np.log(dxv_L2_3),"-+",label="Benchmark 3")
ax3.plot(x,np.log(dxv_L2_5),"-+",label="Benchmark 4")
ax3.legend()
ax3.set_xlabel("log(h)")
ax3.set_ylabel("log($e_{xy}$ $L_2$)")

ax4.plot(x,np.log(phi_L2_1),"-+",label="Benchmark 1")
ax4.plot(x,np.log(phi_L2_2),"-+",label="Benchmark 2")
ax4.plot(x,np.log(phi_L2_3),"-+",label="Benchmark 3")
ax4.plot(x,np.log(phi_L2_5),"-+",label="Benchmark 4")
ax4.legend()
ax4.set_xlabel("log(h)")
ax4.set_ylabel("log($\phi$ $L_2$)")

f.suptitle("L2 Norms for components of the strain rate tensor and $\phi$, for Benchmarks 1-4",fontsize=20,y=0.925)

f.savefig("Strain_Norms_L2.pdf")


# # And now for the regression analysis
# # 

# # In[21]:


# y=np.abs(phi_L1_1)
# h=np.abs(x)
# m=np.linalg.lstsq(np.vstack([np.log(h), np.ones(len(np.log(h)))]).T,np.log(y))[0][0]
# m


# # In[22]:


# dxu_list = [dxu_L1_1,dxu_L1_2,dxu_L1_3,dxu_L1_5,dxu_L2_1,dxu_L2_2,dxu_L2_3,dxu_L2_5]
# dyv_list = [dyv_L1_1,dyv_L1_2,dyv_L1_3,dyv_L1_5,dyv_L2_1,dyv_L2_2,dyv_L2_3,dyv_L2_5]
# dxv_list = [dxv_L1_1,dxv_L1_2,dxv_L1_3,dxv_L1_5,dxv_L2_1,dxv_L2_2,dxv_L2_3,dxv_L2_5]
# phi_list = [phi_L1_1,phi_L1_2,phi_L1_3,phi_L1_5,phi_L2_1,phi_L2_2,phi_L2_3,phi_L2_5]


# # In[23]:


# def get_regression(x,y):
#     y=np.abs(y)
#     h=np.abs(x)
#     return np.linalg.lstsq(np.vstack([np.log(h), np.ones(len(np.log(h)))]).T,np.log(y))[0][0]


# # In[24]:


# dxu_regression_list=[]
# for dxu in dxu_list:
#     dxu_regression_list.append(get_regression(x,dxu))
# dxu_regression_list


# # In[25]:


# dxv_regression_list=[]
# for dxv in dxv_list:
#     dxv_regression_list.append(get_regression(x,dxv))
# dxv_regression_list


# # In[26]:


# dyv_regression_list=[]
# for dyv in dyv_list:
#     dyv_regression_list.append(get_regression(x,dyv))
# dyv_regression_list


# # In[27]:


# phi_regression_list=[]
# for phi in phi_list:
#     phi_regression_list.append(get_regression(x,phi))
# phi_regression_list

