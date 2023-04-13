""" Graphical user interface to plot load-depth curves """
import micromechanics.indentation as indentation

def plot_load_depth(self,tabName,If_inclusive_frameStiffness='inclusive'):
    """
    Graphical user interface to plot the load-depth curves of the chosen tests 

    Args:
      tabName (string): the name of Tab Widget
      If_inclusive_frameStiffness (string): 'inclusive' or 'exclusive'
    """
    #define indentation 
    i = eval('self.i_%s'%tabName)
    #reset testList
    i.testList = list(i.allTestList)
    #read ax to plot load depth curves
    ax=eval('self.static_ax_load_depth_tab_%s_frame_stiffness_%s'%(If_inclusive_frameStiffness,tabName))      
    ax.cla()
    #read static canvas
    static_canvas=eval('self.static_canvas_load_depth_tab_%s_frame_stiffness_%s'%(If_inclusive_frameStiffness,tabName))
    #read inputs from GUI
    showFindSurface = eval('self.ui.checkBox_showFindSurface_tab_%s_frame_stiffness_%s.isChecked()'%(If_inclusive_frameStiffness,tabName))  # showFindSurface verifies plotting dP/dh slope
    selectedTests=eval('self.ui.tableWidget_%s.selectedItems()'%tabName)
    show_iLHU=eval('self.ui.checkBox_iLHU_%s_frame_stiffness_%s.isChecked()'%(If_inclusive_frameStiffness,tabName))
    #plot the load-depth curves of the seclected tests
    for Test in selectedTests:
        column=Test.column()
        if column==0:  #Test Names are located at column 0
            i.testName=Test.text()
            if i.vendor == indentation.definitions.Vendor.Agilent:
                if show_iLHU:
                    i.output['plotLoadHoldUnload'] = True # plot iLHU
                i.nextAgilentTest(newTest=False)
                i.output['plotLoadHoldUnload'] = False
                i.nextTest(newTest=False,plotSurface=showFindSurface) 
            ax.set_title('%s'%i.testName)
            i.output['ax']=ax
            i.stiffnessFromUnloading(i.p, i.h, plot=True)
            i.output['ax']=None
    static_canvas.figure.set_tight_layout(True)
    static_canvas.draw()