""" Graphical user interface to classify the tests """
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from sklearn.cluster import KMeans
from PySide6.QtWidgets import QTableWidgetItem, QComboBox # pylint: disable=no-name-in-module
from PySide6.QtGui import QColor # pylint: disable=no-name-in-module
from PySide6.QtCore import Qt # pylint: disable=no-name-in-module

colors_clustering =  ['tab:blue', 'tab:brown', 'tab:orange', 'tab:pink', 'tab:green', 'tab:gray', 'tab:red', 'tab:olive', 'tab:purple','tab:cyan', 'lime', 'indigo', 'pink', 'gold','white','k', 'yellow','cyan','blue', 'peru', 'cadetblue', 'lightblue', 'deepskyblue', 'skyblue', 'steelblue', 'greenyellow', 'olivedrab', 'yellowgreen', 'darkolivegreen', 'greenyellow', 'lawngreen','honeydew','darkseagreen', 'dimgray', 'darkgray', 'silver', 'lightgray', 'gainsboro','whitesmoke','snow'] #pylint:disable=line-too-long
AllParameters = ['mean of H [GPa]', 'mean of E [GPa]', 'mean of Er [GPa]']
Labels = ['Hardness [GPa]', 'Young\'s Modulus [GPa]', 'reduced Modulus [GPa]']

colors_clustering_using = []

def Classification_HE(self):
  """ Graphical user interface to classify the tests according to H and E """
  global colors_clustering_using #pylint:disable=global-statement
  #get Inputs
  files_list = (self.ui.textEdit_Files_tabClassification.toPlainText()).split("\n")
  IfUsingFoundNumberClusters = self.ui.checkBox_ifUsingFoundNumberClusters_tabClassification.isChecked()
  maxMSD = self.ui.doubleSpinBox_MSD_tabClassification.value() # the maximum Mean of Squared Distances
  IfPlotElbow = self.ui.checkBox_ifPlotElbow_tabClassification.isChecked()
  WeightingRatio = self.ui.doubleSpinBox_WeightingRatio_tabClassification.value()
  DimensionX = self.ui.comboBox_DimensionX_tabClassification.currentIndex()
  DimensionY = self.ui.comboBox_DimensionY_tabClassification.currentIndex()
  DimensionX_Name = AllParameters[DimensionX]
  DimensionY_Name = AllParameters[DimensionY]
  ax_HE = self.static_ax_HE_tabClassification
  ax_HE.cla()
  DimensionXvalue_collect=[]
  DimensionYvalue_collect=[]
  FileNumber_collect=[]
  TestName_collect=[]
  for FileNumber, file in enumerate(files_list):
    try:
      data = pd.read_excel(file, sheet_name=None)
    except Exception as e: #pylint: disable=broad-except
      suggestion = 'Please check the typed complete paths of files' #pylint: disable=anomalous-backslash-in-string
      self.show_error(str(e), suggestion)
    try:
      DimensionYvalue = data.get('Results')[DimensionY_Name].to_numpy()
      DimensionYvalue_collect = np.concatenate((DimensionYvalue_collect, DimensionYvalue), axis=0)
      DimensionXvalue = data.get('Results')[DimensionX_Name].to_numpy()
      DimensionXvalue_collect = np.concatenate((DimensionXvalue_collect, DimensionXvalue), axis=0)
      for TestName in data.get('Results')['Test Name'].to_numpy():
        TestName_collect.append(TestName)
        FileNumber_collect.append(FileNumber)

    except Exception as e: #pylint: disable=broad-except
      suggestion = f"Please check the Column Names of H and E in {file}" #pylint: disable=anomalous-backslash-in-string
      self.show_error(str(e), suggestion)

  # factor_y is used to correct the big difference of absolute value between hardness and modulus
  # factor_y = (np.std(E_collect, ddof=1))/ (np.std(H_collect, ddof=1)) * WeightingRatio
  factor_y = (np.max(DimensionXvalue_collect)-np.min(DimensionXvalue_collect))/ (np.max(DimensionYvalue_collect)-np.min(DimensionYvalue_collect)) * WeightingRatio
  # constrcuting the data set X for K-means Clustering
  X = np.concatenate((np.array([DimensionXvalue_collect]).T, np.array([DimensionYvalue_collect]).T*factor_y), axis=1)
  # using the sum of squared distances (ssd) to find an optimal cluster Number
  ssd={} # sum of squared distances
  if IfUsingFoundNumberClusters:
    if len(DimensionYvalue_collect)>30:
      max_K = 30
    else:
      max_K = len(DimensionYvalue_collect)
    for k in range(1, max_K):
      cluster = KMeans(n_clusters=k,random_state=0,n_init=10).fit(X)
      ssd[k] = cluster.inertia_ #inertia_: Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.
    ssd_values = np.array(list(ssd.values()))/len(DimensionXvalue_collect) # ssd per data ponit
    ssd_keys = np.array(list(ssd.keys()))
    try:
      index = np.where(ssd_values<=maxMSD)
      n_clusters=int(ssd_keys[index][0])
      if IfPlotElbow:
        # plot cluster number vs ssd
        plt.close()
        _, ax = plt.subplots()
        ax.plot(ssd_keys,ssd_values)
        ax.scatter(ssd_keys,ssd_values)
        ax.scatter(ssd_keys[index][0],ssd_values[index][0], label=f"N at MSD = {ssd_values[index][0]:.1f}")
        ax.legend()
        ax.set_xlabel('Number of Clusters')
        ax.set_ylabel('Mean of squared Distances (MSD) [-]')
        ax.set_title(f"MSD < {maxMSD:.1f}")
        plt.show()
    except Exception as e: #pylint:disable=broad-except
      if IfPlotElbow:
        # plot cluster number vs ssd
        plt.close()
        _, ax = plt.subplots()
        ax.plot(ssd_keys,ssd_values)
        ax.scatter(ssd_keys,ssd_values)
        ax.set_xlabel('Number of Clusters')
        ax.set_ylabel('Mean of squared Distances (MSD) [-]')
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
  colors_clustering_using = []
  try:
    for k in range(n_clusters):
      # setting the background color of comboBox
      currentIndex = self.ui.tableWidget_tabClassification.cellWidget(k,1).currentIndex()
      colors_clustering_using.append(colors_clustering[currentIndex])
  except:
    pass
  if len(colors_clustering_using) != n_clusters:
    colors_clustering_using = colors_clustering
  for i in range(n_clusters):
    if i<=9:
      ax_HE.scatter(X[y_pred==i, 0], X[y_pred==i, 1]/factor_y, marker=marker1, color=colors_clustering_using[i], edgecolors='black', s=30, alpha=0.8)
    else:
      ax_HE.scatter(X[y_pred==i, 0], X[y_pred==i, 1]/factor_y, marker=marker2, color=colors_clustering_using[i], s=20, alpha=0.8)
    ax_HE.text(centroid[i, 0], centroid[i, 1]/factor_y, s=f"#{i+1}")
  ax_HE.scatter(centroid[:,0],centroid[:,1]/factor_y,marker='x',s=100,c='black', zorder=3)
  ax_HE.set_aspect(factor_y/ WeightingRatio)
  def showWeightingRatio(ax=ax_HE):
    width=0.1
    xl = ax_HE.get_xlim()[1] - ax_HE.get_xlim()[0]
    yl = ax_HE.get_ylim()[1] - ax_HE.get_ylim()[0]
    x0 = 0.8*xl +ax_HE.get_xlim()[0]
    y0 = 0.1*yl +ax_HE.get_ylim()[0]
    x1 = (0.8+width)*xl +ax_HE.get_xlim()[0]
    y1 = 0.1*yl +ax_HE.get_ylim()[0]
    x2 = (0.8+width)*xl +ax_HE.get_xlim()[0]
    y2 = y1 + width*yl*WeightingRatio
    ax.plot([x0,x1,x2,x0],[y0,y1,y2,y0])
    ax.text(x0-0.2*width*xl,y0-0.08*yl,'Weighting\n    Ratio', color='tab:blue')
  showWeightingRatio(ax=ax_HE)
  ax_HE.set_ylabel(Labels[DimensionY])
  ax_HE.set_xlabel(Labels[DimensionX])
  ax_HE.set_title(f"{files_list[0].split(self.slash)[-2]}{self.slash}{files_list[0].split(self.slash)[-1]}\n")
  self.static_canvas_HE_tabClassification.figure.set_tight_layout(True)
  self.static_canvas_HE_tabClassification.draw()
  #listing Results
  self.ui.tableWidget_tabClassification.setRowCount(n_clusters)
  def ComboBoxBGcolorChanged():
    for k in range(n_clusters):
      # setting the background color of comboBox
      currentIndex = self.ui.tableWidget_tabClassification.cellWidget(k,1).currentIndex()
      Color = mcolors.to_rgba(colors_clustering[currentIndex])
      self.ui.tableWidget_tabClassification.cellWidget(k,1).setStyleSheet(f"background-color : rgba({Color[0]*255},{Color[1]*255},{Color[2]*255},{Color[3]*255});")
  for k in range(n_clusters):
    #cluster Number
    self.ui.tableWidget_tabClassification.setItem(k,0,QTableWidgetItem(f"{k+1}"))
    #color
    if len(colors_clustering_using) != n_clusters:
      #
      comboBox = QComboBox()
      for row, color in enumerate(colors_clustering):
        Color = mcolors.to_rgba(color)
        comboBox.addItem(color)
        model = comboBox.model()
        model.setData(model.index(row, 0), QColor(Color[0]*255,Color[1]*255,Color[2]*255,Color[3]*255), Qt.BackgroundRole)
      self.ui.tableWidget_tabClassification.setItem(k,1,QTableWidgetItem())
      self.ui.tableWidget_tabClassification.setCellWidget(k, 1, comboBox)
      Color = mcolors.to_rgba(colors_clustering[k])
      # setting the background color of comboBox
      self.ui.tableWidget_tabClassification.cellWidget(k,1).setCurrentIndex(k)
      self.ui.tableWidget_tabClassification.cellWidget(k,1).setStyleSheet(f"background-color : rgba({Color[0]*255},{Color[1]*255},{Color[2]*255},{Color[3]*255});")
      self.ui.tableWidget_tabClassification.cellWidget(k,1).currentIndexChanged.connect(ComboBoxBGcolorChanged)

    #Number of data
    self.ui.tableWidget_tabClassification.setItem(k,2,QTableWidgetItem(f"{len(X[y_pred==k, 0])}"))
    #mean of x
    self.ui.tableWidget_tabClassification.setItem(k,3,QTableWidgetItem(f"{(X[y_pred==k, 0]).mean():.2f}"))
    #std of x
    self.ui.tableWidget_tabClassification.setItem(k,4,QTableWidgetItem(f"{(X[y_pred==k, 0]).std(ddof=1):.2f}"))
    #mean of y
    self.ui.tableWidget_tabClassification.setItem(k,5,QTableWidgetItem(f"{(X[y_pred==k, 1]/factor_y).mean():.2f}"))
    #std of y
    self.ui.tableWidget_tabClassification.setItem(k,6,QTableWidgetItem(f"{(X[y_pred==k, 1]/factor_y).std(ddof=1):.2f}"))
  # the mapping can be plotted after the K-means clustering
  self.ui.pushButton_PlotMappingAfterClustering_tabClassification.setEnabled(True)

  #prepare for export
  if DimensionX == 0:
    self.tabClassification_H_collect=DimensionXvalue_collect
  elif DimensionX == 1:
    self.tabClassification_E_collect=DimensionXvalue_collect
  elif DimensionX == 2:
    self.tabClassification_Er_collect=DimensionXvalue_collect

  if DimensionY == 0:
    self.tabClassification_H_collect=DimensionYvalue_collect
  elif DimensionY == 1:
    self.tabClassification_E_collect=DimensionYvalue_collect
  elif DimensionY == 2:
    self.tabClassification_Er_collect=DimensionYvalue_collect

  if 0 not in (DimensionX, DimensionY):
    self.tabClassification_H_collect=np.zeros(len(DimensionXvalue_collect))
  if 1 not in (DimensionX, DimensionY):
    self.tabClassification_E_collect=np.zeros(len(DimensionXvalue_collect))
  if 2 not in (DimensionX, DimensionY):
    self.tabClassification_Er_collect=np.zeros(len(DimensionXvalue_collect))

  self.tabClassification_ClusterLabels=cluster.labels_
  self.tabClassification_FileNumber_collect = FileNumber_collect
  self.tabClassification_TestName_collect = TestName_collect

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

def PlotMappingWithoutClustering(self, plotClustering=False): #pylint:disable=too-many-locals
  """
  Graphical user interface to plot the mapping without the K-means Clustering

  Args:
    plotClustering (bool): the option to plot the mapping of K-means Clustering
  """

  def Plot2ExplainCycle(ax,x0,y0,radius,color='white'):
    """
    plot an open cycle to show the relationship between the cycle and the Berkovich indent

    Args:
      ax (class): matplotlib.axes.Axes
      x0 (float): x coordinate of the center of circle
      y0 (float): y coordinate of the center of circle
      radius (float): radius of the center of circle
      color (string): face color of the circle
    """
    plotCycle(ax=ax,x0=x0,y0=y0,radius=radius,stepsize=50)
    x1 = x0 + radius*np.cos(90./180 * np.pi)
    y1 = y0 + radius*np.sin(90./180 * np.pi)
    x2 = x0 + radius*np.cos(210./180 * np.pi)
    y2 = y0 + radius*np.sin(210./180 * np.pi)
    x3 = x0 + radius*np.cos(330./180 * np.pi)
    y3 = y0 + radius*np.sin(330./180 * np.pi)
    ax.plot([x1,x2,x3,x1],[y1,y2,y3,y1], color=color, linewidth=1)
    ax.plot([x1,x0],[y1,y0], color=color, linewidth=1)
    ax.plot([x2,x0],[y2,y0], color=color, linewidth=1)
    ax.plot([x3,x0],[y3,y0], color=color, linewidth=1)
    ax.text(x2+2.5*radius,y0-1*radius,'Berkovich\nIndentation Region', fontsize=11)

  def lim_change(ax):
    lx = ax.get_xlim()
    ly = ax.get_ylim()
    if (lx[1]-lx[0]) >= (ly[1]-ly[0]):
      factor = (Length+2*Spacing)/(lx[1]-lx[0])
    else:
      factor = (Length+2*Spacing)/(ly[1]-ly[0])
    index = axs_collect.index(ax)
    print('index',index)
    index_start = index - index % 4
    for i in np.arange(index_start,index_start+4,1):
      print('i',i)
      ax = axs_collect[i]
      try:
        paths_DICT[ax].set_sizes([s*factor**2 for s in point_sizes_DICT[ax]])
      except KeyError:
        pass

  #close all matplot figures before plotting new figures
  plt.close('all')

  #get Inputs
  files_list = (self.ui.textEdit_Files_tabClassification.toPlainText()).split("\n")
  DimensionX = self.ui.comboBox_DimensionX_tabClassification.currentIndex()
  DimensionY = self.ui.comboBox_DimensionY_tabClassification.currentIndex()
  IfShowRealSizeIndent = self.ui.checkBox_ifShowRealSizeIndent_tabClassification.isChecked()
  FlipMapping = self.ui.comboBox_FlipMapping_tabClassification.currentIndex()
  MarkerType = self.ui.comboBox_MarkerType_tabClassification.currentIndex()

  axs_collect=[]
  paths_DICT = {}
  point_sizes_DICT = {}
  for _, file in enumerate(files_list):
    #collect all the mapping scatters and their marker sizes
    fig = plt.figure(figsize=[8,8],dpi=100)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2, sharex=ax1, sharey=ax1)
    ax3 = fig.add_subplot(2,2,3, sharex=ax1, sharey=ax1)
    ax4 = fig.add_subplot(2,2,4, sharex=ax1, sharey=ax1)
    axs = [ax1,ax2,ax3,ax4]
    data = pd.read_excel(file, sheet_name=None)
    hmax = data.get('Results')['max. hmax [µm]'].to_numpy()
    DimensionX_Name = AllParameters[DimensionX]
    DimensionY_Name = AllParameters[DimensionY]
    DimensionYvalue = data.get('Results')[DimensionY_Name].to_numpy()
    DimensionXvalue = data.get('Results')[DimensionX_Name].to_numpy()
    X_Position = data.get('Results')['X Position [µm]'].to_numpy() #µm
    Y_Position = data.get('Results')['Y Position [µm]'].to_numpy() #µm
    X_length = X_Position.max()-X_Position.min()
    Y_length = Y_Position.max()-Y_Position.min()
    if X_length > Y_length:
      Length = X_length
    else:
      Length = Y_length

    if FlipMapping == 0:
      # X_Position.min() Y_Position.min() setting as the zero position
      X0_Position = X_Position.min()
      for i, _ in enumerate(X_Position):
        X_Position[i] = X_Position[i]-X0_Position
      Y0_Position = Y_Position.min()
      for i, _ in enumerate(Y_Position):
        Y_Position[i] = Y_Position[i]-Y0_Position
    if FlipMapping in (1,3):
      # X_Position.min() Y_Position.min() setting as the zero position, and filp left and right
      X0_Position = X_Position.min()
      for i, _ in enumerate(X_Position):
        X_Position[i] = -(X_Position[i]-X0_Position) + Length
      Y0_Position = Y_Position.min()
      for i, _ in enumerate(Y_Position):
        Y_Position[i] = Y_Position[i]-Y0_Position
    if FlipMapping in (2,3):
      # X_Position.min() Y_Position.min() setting as the zero position, and filp top and bottom
      Y0_Position = Y_Position.min()
      for i, _ in enumerate(Y_Position):
        Y_Position[i] = -(Y_Position[i]-Y0_Position) + Length
      X0_Position = X_Position.min()
      for i, _ in enumerate(X_Position):
        X_Position[i] = X_Position[i]-X0_Position

    try:
      Spacing = ( (X_Position[1]-X_Position[0])**2 + (Y_Position[1]-Y_Position[0])**2 )**0.5 #µm
    except:
      Spacing = 100
    else:
      if Spacing <0.01:
        Spacing = 100
    try:
      Spacing1 = ( (X_Position[2]-X_Position[1])**2 + (Y_Position[2]-Y_Position[1])**2 )**0.5 #µm
    except:
      pass
    else:
      if 0.01 < Spacing1 < Spacing:
        Spacing=Spacing1
    try:
      Spacing2 = ( (X_Position[-2]-X_Position[-1])**2 + (Y_Position[-2]-Y_Position[-1])**2 )**0.5 #µm
    except:
      pass
    else:
      if 0.01 < Spacing2 < Spacing:
        Spacing=Spacing2
    #hardness mapping
    cm_H = plt.cm.get_cmap('Blues')
    OnePixel = 72./ fig.dpi # 1point== fig.dpi/72. * pixels  # Pixel/Point
    OneMicroMeter = (ax1.get_position().x1 - ax1.get_position().x0)*fig.get_size_inches()[0] / (Length+2*Spacing) * fig.dpi * OnePixel #   Point/ µm
    if IfShowRealSizeIndent:
      markersize = (hmax[i]*np.tan(65.3/180*np.pi)*4*OneMicroMeter)**2
    else:
      markersize = Spacing
    mapping1 = axs[0].scatter(X_Position, Y_Position, c=DimensionYvalue, s=markersize, vmin=np.mean(DimensionYvalue)-2*np.std(DimensionYvalue,ddof=1), vmax=np.mean(DimensionYvalue)+2*np.std(DimensionYvalue,ddof=1), cmap=cm_H,marker='o')#pylint:disable=line-too-long
    paths_DICT[axs[0]] = mapping1
    print('mapping1',mapping1)
    point_sizes_DICT[axs[0]] = paths_DICT[axs[0]].get_sizes()
    #Young's modulus mapping
    cm_E = plt.cm.get_cmap('Purples')
    mapping2 = axs[1].scatter(X_Position, Y_Position, c=DimensionXvalue, s=markersize, vmin=np.mean(DimensionXvalue)-2*np.std(DimensionXvalue,ddof=1), vmax=np.mean(DimensionXvalue)+2*np.std(DimensionXvalue,ddof=1), cmap=cm_E)#pylint:disable=line-too-long
    paths_DICT[axs[1]] = mapping2
    point_sizes_DICT[axs[1]] = paths_DICT[axs[1]].get_sizes()
    if IfShowRealSizeIndent:
      Plot2ExplainCycle(ax=axs[3], x0=Length*0.58,y0=Length*0.1,radius=Length*0.08)
      Explaining = axs[3].scatter([Length*0.58], [Length*0.1], color='gray',s=(Length*0.08*2*OneMicroMeter)**2,marker='o')
      paths_DICT[axs[3]] = Explaining
      point_sizes_DICT[axs[3]] = paths_DICT[axs[3]].get_sizes()
    ScaleBarLength = Spacing
    while ScaleBarLength < 0.05*Length:
      ScaleBarLength = ScaleBarLength *10
    axs[3].plot([0,ScaleBarLength],[Length*0.12,Length*0.12], color='black', linewidth=8)
    axs[3].text(0, Length*0., f"{ScaleBarLength:.1f} µm", fontsize=14)
    axs[0].set_xlim(-Spacing, Length+Spacing)
    axs[0].set_ylim(-Spacing, Length+Spacing)
    axs[3].set_frame_on(False)
    axs[2].set_frame_on(False)
    axs[0].set_title(Labels[DimensionY][:-5]+'mapping')
    axs[1].set_title(Labels[DimensionX][:-5]+'mapping')
    cax_mapping1 = fig.add_axes([0.58, 0.45, 0.3, 0.02])
    cax_mapping2 = fig.add_axes([0.58, 0.36, 0.3, 0.02])
    fig.colorbar(mapping1, cax=cax_mapping1, orientation='horizontal', label=Labels[DimensionY])
    fig.colorbar(mapping2, cax=cax_mapping2, orientation='horizontal', label=Labels[DimensionX])
    fig.suptitle(f"{file.split(self.slash)[-2]}{self.slash}{file.split(self.slash)[-1]}\nSpacing = {Spacing:.1f} µm")

    if plotClustering:
      X, cluster, factor_y = self.parameters_from_Classification_HE
      axs[2].set_frame_on(True)
      axs[2].set_title('K-means Clustering')
      cluster_collect=[]
      for i, _ in enumerate(X_Position):
        # plotCycle(ax=axs[2],x0=X_Position[i],y0=Y_Position[i],radius=hmax[i]*np.tan(65.3/180*np.pi)*2,stepsize=20) #pylint: disable=unnecessary-list-index-lookup
        index = np.where( (np.absolute((X[:,1]/factor_y)-DimensionYvalue[i])<1.e-5) & (np.absolute(X[:,0]-DimensionXvalue[i])<1.e-5) )
        cluster_collect.append(int(cluster.labels_[index])+1)
      #Cluster mapping
      try:
        # create a colormap for plotting the K-means Clustering Mapping
        my_cmap = mpl.colors.ListedColormap(colors_clustering_using, name="my_cmap", N=np.max(cluster_collect))
        mpl.colormaps.register(cmap=my_cmap, force=True)
      except:
        pass
      cm_cluster = plt.cm.get_cmap('my_cmap')
      edgecolors =[]
      circleWidth = 0
      if MarkerType == 1:
        circleWidth = Spacing*0.05
        for cluster_number in cluster_collect:
          edgecolors.append(colors_clustering_using[cluster_number-1])
      mapping3 = axs[2].scatter(X_Position, Y_Position, c=cluster_collect, s=markersize, vmin=1, vmax=np.max(cluster_collect)+1, cmap=cm_cluster, facecolors='none', edgecolors=edgecolors, lw=markersize**0.5*circleWidth)#pylint:disable=line-too-long
      if MarkerType == 1:
        mapping3.set_facecolor('none')
      paths_DICT[axs[2]] = mapping3
      point_sizes_DICT[axs[2]] = paths_DICT[axs[2]].get_sizes()
      cax_mapping3 = fig.add_axes([0.58, 0.27, 0.3, 0.02])
      fig.colorbar(mapping3, cax=cax_mapping3, orientation='horizontal', label='Cluster Number [-]', ticks=np.arange(np.min(cluster_collect), np.max(cluster_collect)+1, 2), spacing='uniform')
      fig.suptitle(f"{file.split(self.slash)[-2]}{self.slash}{file.split(self.slash)[-1]}\nSpacing = {Spacing:.1f} µm, Number of Clusters = {len(cluster.cluster_centers_)} ")
      for ax in axs:
        ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labeltop=False, labelleft=False, labelright=False)
      fig.savefig(f"{file[:-5]}.svg", transparent=True)

    for ax in axs:
      axs_collect.append(ax)

  for ax in axs_collect:
    ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labeltop=False, labelleft=False, labelright=False)
    ax.callbacks.connect('xlim_changed', lim_change)
    ax.callbacks.connect('ylim_changed', lim_change)
    ax.set_aspect(1)
  plt.show()


def PlotMappingAfterClustering(self):
  """ Graphical user interface to plot the mapping after the K-means Clustering """
  #close all matplot figures before plotting new figures
  plt.close('all')
  #plot mappings of hardness, modulus and K-means Clustering
  self.PlotMappingWithoutClustering(plotClustering=True)
