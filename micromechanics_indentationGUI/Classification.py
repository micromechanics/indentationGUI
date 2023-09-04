""" Graphical user interface to classify the tests """
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PySide6.QtWidgets import QTableWidgetItem # pylint: disable=no-name-in-module

def Classification_HE(self):
  """ Graphical user interface to classify the tests according to H and E """

  #get Inputs
  files_list = (self.ui.textEdit_Files_tabClassification.toPlainText()).split("\n")
  IfUsingFoundNumberClusters = self.ui.checkBox_ifUsingFoundNumberClusters_tabClassification.isChecked()
  IfPlotElbow = self.ui.checkBox_ifPlotElbow_tabClassification.isChecked()

  ax_HE = self.static_ax_HE_tabClassification
  ax_HE.cla()
  H_collect=[]
  E_collect=[]
  for file in files_list:
    try:
      data = pd.read_excel(file, sheet_name=None)
    except Exception as e: #pylint: disable=broad-except
      suggestion = 'Please check the typed complete paths of files' #pylint: disable=anomalous-backslash-in-string
      self.show_error(str(e), suggestion)
    H = data.get('Results')['mean of H [GPa]'].to_numpy()
    H_collect = np.concatenate((H_collect, H), axis=0)
    E = data.get('Results')['mean of E [GPa]'].to_numpy()
    E_collect = np.concatenate((E_collect, E), axis=0)

  # factor_y is used to correct the big difference of absolute value between hardness and modulus
  factor_y = (np.amax(E_collect)-np.amin(E_collect))/ (np.amax(H_collect)-np.amin(H_collect))
  # constrcuting the data set X for K-means Clustering
  X = np.concatenate((np.array([E_collect]).T, np.array([H_collect]).T*factor_y), axis=1)
  # using the sum of squared distances (ssd) to find an optimal cluster Number
  ssd={} # sum of squared distances
  if IfUsingFoundNumberClusters:
    for k in range(1, 30):
      cluster = KMeans(n_clusters=k,random_state=0,n_init=10).fit(X)
      ssd[k] = cluster.inertia_ #inertia_: Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.
    ssd_values = np.array(list(ssd.values()))
    ssd_keys = np.array(list(ssd.keys()))
    change_amplitude = np.absolute((ssd_values[2:]-ssd_values[1:-1])/np.absolute((ssd_values[1:-1]-ssd_values[:-2])))
    try:
      index = np.where(change_amplitude>=1)
      n_clusters=int(ssd_keys[1:-1][index][1])
      if IfPlotElbow:
        # plot cluster number vs ssd
        plt.close()
        _, ax = plt.subplots()
        ax.plot(ssd_keys,ssd_values)
        ax.scatter(ssd_keys,ssd_values)
        ax.scatter(ssd_keys[1:-1][index][1],ssd_values[1:-1][index][1], label='optimal N of Clusters determined by Elbow Method')
        ax.legend()
        ax.set_xlabel('Number of Clusters')
        ax.set_ylabel('Sum of squared Distances [-]')
        plt.show()
    except Exception as e: #pylint:disable=broad-except
      if IfPlotElbow:
        # plot cluster number vs ssd
        plt.close()
        _, ax = plt.subplots()
        ax.plot(ssd_keys,ssd_values)
        ax.scatter(ssd_keys,ssd_values)
        ax.set_xlabel('Number of Clusters')
        ax.set_ylabel('Sum of squared Distances [-]')
        plt.show()
      suggestion = 'the optimal number of clusters cannot be found.'
      self.show_error(str(e), suggestion)
    self.ui.spinBox_NumberClusters_tabClassification.setValue(n_clusters)
  n_clusters=self.ui.spinBox_NumberClusters_tabClassification.value()
  cluster = KMeans(n_clusters=n_clusters,random_state=0,n_init=10).fit(X)
  y_pred = cluster.labels_
  self.parameters_from_Classification_HE = [X, cluster, factor_y]
  marker1='o'
  marker2='D'
  centroid=cluster.cluster_centers_
  # plot the results of K-means Clustering
  for i in range(n_clusters):
    if i<=9:
      ax_HE.scatter(X[y_pred==i, 0], X[y_pred==i, 1]/factor_y, marker=marker1, edgecolors='black', s=30, alpha=0.9)
    else:
      ax_HE.scatter(X[y_pred==i, 0], X[y_pred==i, 1]/factor_y, marker=marker2, s=20, alpha=0.9)
    ax_HE.text(centroid[i, 0], centroid[i, 1]/factor_y, s=f"#{i+1}")
  ax_HE.scatter(centroid[:,0],centroid[:,1]/factor_y,marker='x',s=100,c='black', zorder=3)
  ax_HE.set_ylabel('Hardness [GPa]')
  ax_HE.set_xlabel('Young\'s Modulus [GPa]')
  self.static_canvas_HE_tabClassification.figure.set_tight_layout(True)
  self.set_aspectRatio(ax=ax_HE)
  self.static_canvas_HE_tabClassification.draw()
  #listing Results
  self.ui.tableWidget_tabClassification.setRowCount(n_clusters)
  for k in range(n_clusters):
    #cluster Number
    self.ui.tableWidget_tabClassification.setItem(k,0,QTableWidgetItem(f"{k+1}"))
    #Number of data
    self.ui.tableWidget_tabClassification.setItem(k,1,QTableWidgetItem(f"{len(X[y_pred==k, 0])}"))
    #mean of x
    self.ui.tableWidget_tabClassification.setItem(k,2,QTableWidgetItem(f"{(X[y_pred==k, 0]).mean():.2f}"))
    #std of x
    self.ui.tableWidget_tabClassification.setItem(k,3,QTableWidgetItem(f"{(X[y_pred==k, 0]).std(ddof=1):.2f}"))
    #mean of y
    self.ui.tableWidget_tabClassification.setItem(k,4,QTableWidgetItem(f"{(X[y_pred==k, 1]/factor_y).mean():.2f}"))
    #std of y
    self.ui.tableWidget_tabClassification.setItem(k,5,QTableWidgetItem(f"{(X[y_pred==k, 1]/factor_y).std(ddof=1):.2f}"))
  # the mapping can be plotted after the K-means clustering
  self.ui.pushButton_PlotMappingAfterClustering_tabClassification.setEnabled(True)

def plotCycle(ax,x0,y0,radius,stepsize=20,markersize=1):
  """
  plot an open cycle

  Args:
    ax (class): matplotlib.axes.Axes
    x0 (float): x coordinate of the center of circle
    y0 (float): y coordinate of the center of circle
    radius (float): radius of the center of circle
    stepsize (int): the resolution of the circle
    markersize (int): the size of the pixel
  """
  theta = np.arange(0, 2 * (np.pi+ np.pi/stepsize), 2 * np.pi/stepsize)
  x = x0 + radius*np.cos(theta)
  y = y0 + radius*np.sin(theta)
  ax.plot(x,y,color='gray',linewidth=1, alpha=0.8)

def Plot2ExplainCycle(ax,x0,y0,radius):
  """
  plot an open cycle to show the relationship between the cycle and the Berkovich indent

  Args:
    ax (class): matplotlib.axes.Axes
    x0 (float): x coordinate of the center of circle
    y0 (float): y coordinate of the center of circle
    radius (float): radius of the center of circle
  """
  plotCycle(ax=ax,x0=x0,y0=y0,radius=radius,stepsize=50)
  x1 = x0 + radius*np.cos(90./180 * np.pi)
  y1 = y0 + radius*np.sin(90./180 * np.pi)
  x2 = x0 + radius*np.cos(210./180 * np.pi)
  y2 = y0 + radius*np.sin(210./180 * np.pi)
  x3 = x0 + radius*np.cos(330./180 * np.pi)
  y3 = y0 + radius*np.sin(330./180 * np.pi)
  ax.plot([x1,x2,x3,x1],[y1,y2,y3,y1], color='black', linewidth=1)
  ax.plot([x1,x0],[y1,y0], color='black', linewidth=1)
  ax.plot([x2,x0],[y2,y0], color='black', linewidth=1)
  ax.plot([x3,x0],[y3,y0], color='black', linewidth=1)
  ax.text(x2+2.5*radius,y0-1*radius,'Berkovich\nIndentation Region', fontsize=11)

def PlotMappingWithoutClustering(self, plotClustering=False):
  """
  Graphical user interface to plot the mapping without the K-means Clustering

  Args:
    plotClustering (bool): the option to plot the mapping of K-means Clustering
  """

  #close all matplot figures before plotting new figures
  plt.close('all')

  #get Inputs
  files_list = (self.ui.textEdit_Files_tabClassification.toPlainText()).split("\n")

  for file in files_list:
    fig = plt.figure(figsize=[8,8])
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2, sharex=ax1, sharey=ax1)
    ax3 = fig.add_subplot(2,2,3, sharex=ax1, sharey=ax1)
    ax4 = fig.add_subplot(2,2,4, sharex=ax1, sharey=ax1)
    axs = [ax1,ax2,ax3,ax4]
    data = pd.read_excel(file, sheet_name=None)
    hmax = data.get('Results')['max. hmax [µm]'].to_numpy()
    H = data.get('Results')['mean of H [GPa]'].to_numpy()
    E = data.get('Results')['mean of E [GPa]'].to_numpy()
    X_Position = data.get('Results')['X Position [µm]'].to_numpy() #µm
    Y_Position = data.get('Results')['Y Position [µm]'].to_numpy() #µm
    X_length = X_Position.max()-X_Position.min()
    Y_length = Y_Position.max()-Y_Position.min()
    if X_length > Y_length:
      Length = X_length
    else:
      Length = Y_length
    # X_Position.min() Y_Position.min() setting as the zero position, and filp left and right
    X0_Position = X_Position.min()
    for i, _ in enumerate(X_Position):
      X_Position[i] = -(X_Position[i]-X0_Position) + Length
    Y0_Position = Y_Position.min()
    for i, _ in enumerate(Y_Position):
      Y_Position[i] = Y_Position[i]-Y0_Position
    Spacing = ( (X_Position[1]-X_Position[0])**2 + (Y_Position[1]-Y_Position[0])**2 )**0.5 #µm
    #hardness mapping
    cm_H = plt.cm.get_cmap('Blues')
    mapping1 = axs[0].scatter(X_Position, Y_Position, c=H, vmin=H.min()-(H.max()-H.min())*0.5, vmax=H.max(), cmap=cm_H)
    #Young's modulus mapping
    cm_E = plt.cm.get_cmap('Purples')
    mapping2 = axs[1].scatter(X_Position, Y_Position, c=E, vmin=E.min()-(E.max()-E.min())*0.5, vmax=E.max(), cmap=cm_E)
    #markering indent region
    # for i, _ in enumerate(X_Position):
    #   plotCycle(ax=axs[0],x0=X_Position[i],y0=Y_Position[i],radius=hmax[i]*np.tan(65.3/180*np.pi)*2,stepsize=20) #pylint: disable=unnecessary-list-index-lookup
    #   plotCycle(ax=axs[1],x0=X_Position[i],y0=Y_Position[i],radius=hmax[i]*np.tan(65.3/180*np.pi)*2,stepsize=20) #pylint: disable=unnecessary-list-index-lookup
    axs[3].plot([0,Spacing],[Length*0.12,Length*0.12], color='black', linewidth=8)
    axs[3].text(0, Length*0., f"{Spacing:.1f} µm", fontsize=14)
    Plot2ExplainCycle(ax=axs[3],x0=Length*0.58,y0=Length*0.1,radius=Length*0.08)
    for ax in axs:
      ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labeltop=False, labelleft=False, labelright=False)
      ax.set_aspect(1)
    axs[0].set_xlim(-Spacing, Length+Spacing)
    axs[0].set_ylim(-Spacing, Length+Spacing)
    axs[3].set_frame_on(False)
    axs[2].set_frame_on(False)
    axs[0].set_title('Hardness mapping')
    axs[1].set_title('Young\'s Modulus mapping')
    cax_mapping1 = fig.add_axes([0.58, 0.45, 0.3, 0.02])
    cax_mapping2 = fig.add_axes([0.58, 0.36, 0.3, 0.02])
    fig.colorbar(mapping1, cax=cax_mapping1, orientation='horizontal', label='Hardness [GPa]')
    fig.colorbar(mapping2, cax=cax_mapping2, orientation='horizontal', label='Young\'s Modulus  [GPa]')

    if plotClustering:
      X, cluster, factor_y = self.parameters_from_Classification_HE
      axs[2].set_frame_on(True)
      axs[2].set_title('K-means Clustering')
      cluster_collect=[]
      for i, _ in enumerate(X_Position):
        # plotCycle(ax=axs[2],x0=X_Position[i],y0=Y_Position[i],radius=hmax[i]*np.tan(65.3/180*np.pi)*2,stepsize=20) #pylint: disable=unnecessary-list-index-lookup
        index = np.where( (np.absolute((X[:,1]/factor_y)-H[i])<1.e-5) & (np.absolute(X[:,0]-E[i])<1.e-5) )
        cluster_collect.append(int(cluster.labels_[index])+1)
      #Cluster mapping
      try:
        # create a colormap for plotting the K-means Clustering Mapping
        colors =  ['white', 'tab:cyan', 'tab:olive', 'pink', 'tab:brown', 'tab:pink', 'lime', 'indigo','tab:orange', 'gold', 'tab:green','tab:red','k','tab:purple', 'yellow','cyan','tab:blue','blue', 'peru'] #pylint:disable=line-too-long
        my_cmap = mpl.colors.ListedColormap(colors, name="my_cmap", N=np.max(cluster_collect))
        mpl.colormaps.register(cmap=my_cmap, force=True)
      except:
        pass
      cm_cluster = plt.cm.get_cmap('my_cmap')
      mapping3 = axs[2].scatter(X_Position, Y_Position, c=cluster_collect, vmin=1, vmax=np.max(cluster_collect)+1, cmap=cm_cluster)
      cax_mapping3 = fig.add_axes([0.58, 0.27, 0.3, 0.02])
      fig.colorbar(mapping3, cax=cax_mapping3, orientation='horizontal', label='Cluster Number [-]', ticks=np.arange(np.min(cluster_collect), np.max(cluster_collect)+1, 2), spacing='uniform')
      fig.savefig(f"{file[:-5]}.svg", transparent=True)
    else:
      plt.show()


def PlotMappingAfterClustering(self):
  """ Graphical user interface to plot the mapping after the K-means Clustering """
  #close all matplot figures before plotting new figures
  plt.close('all')
  #plot mappings of hardness, modulus and K-means Clustering
  self.PlotMappingWithoutClustering(plotClustering=True)
  plt.show()
