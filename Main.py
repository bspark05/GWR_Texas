'''
Created on Nov 9, 2015

@author: Bumsub
'''
import PyGWR.FileIO as pyFileIO
import matplotlib.pyplot as plt
import seaborn as sns
from array import array
import numpy as np
#from pysal.esda.mapclassify import Fisher_Jenkss
from matplotlib.colors import Normalize
from images2gif import writeGif
from PIL import Image
import os

def norm_cmap(values, cmap, vmin=None, vmax=None):
    """
    Normalize and set colormap
    
    Parameters
    ----------
    values : Series or array to be normalized
    cmap : matplotlib Colormap
    normalize : matplotlib.colors.Normalize
    cm : matplotlib.cm
    vmin : Minimum value of colormap. If None, uses min(values).
    vmax : Maximum value of colormap. If None, uses max(values).
    
    Returns
    -------
    n_cmap : mapping of normalized values to colormap (cmap)
    
    """
    mn = vmin or min(values)
    mx = vmax or max(values)
    norm = Normalize(vmin=mn, vmax=mx)
    n_cmap = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    return n_cmap

    
def sig6_map1(xCoord, yCoord, sList):
    value1 = -2.56
    value2 = -1.96
    value3 = 0
    value4 = 1.96
    value5 = 2.56
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    ax.scatter(xCoord,yCoord, s= oneGroup3, c='#D3D3D3', edgecolor='none', label ='-1.96 ~ 0.00')
    ax.scatter(xCoord,yCoord, s= oneGroup4, c='#D3D3D3', edgecolor='none', label ='0.00 ~ 1.96')
    
    ax.scatter(xCoord,yCoord, s= oneGroup1, c='#000080', edgecolor='none', label = '~ -2.56')
    ax.scatter(xCoord,yCoord, s= oneGroup2, c='#0000FF', edgecolor='none', label ='-2.56 ~ -1.96')
    
    ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF0000', edgecolor='none', label ='1.96 ~ 2.56')
    ax.scatter(xCoord,yCoord, s= oneGroup6, c='#800000', edgecolor='none', label ='2.56 ~')
    
    ax.legend(loc='upper left', numpoints=3, ncol=3, fontsize=9, bbox_to_anchor=(0, 0))
    
    return fig, ax


def value6_map1(xCoord, yCoord, sList):
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    maxValue = np.amax(s)
    minValue = np.amin(s)
    
    if abs(maxValue) >= abs(minValue):
        absRange = abs(maxValue)
    else:
        absRange = abs(minValue)
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
    
    
    
    ax.scatter(xCoord,yCoord, s= oneGroup1, c='#3300CC', edgecolor='none', label = '~' + legendValue1)
    ax.scatter(xCoord,yCoord, s= oneGroup2, c='#3333FF', edgecolor='none', label = legendValue1 + '~' + legendValue2)
    ax.scatter(xCoord,yCoord, s= oneGroup3, c='#33CCFF', edgecolor='none', label = legendValue2 + '~' + legendValue3)
    
    ax.scatter(xCoord,yCoord, s= oneGroup4, c='#FFCC00', edgecolor='none', label = legendValue3 + '~' + legendValue4)
    ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF6600', edgecolor='none', label = legendValue4 + '~' + legendValue5)
    ax.scatter(xCoord,yCoord, s= oneGroup6, c='#FF0000', edgecolor='none', label = legendValue5 + '~')
    
    ax.legend(loc='upper left', numpoints=6, ncol=3, fontsize=9, bbox_to_anchor=(0, 0))
    
    return fig, ax

def value6_map2(xCoord, yCoord, sList, rangeValue):
    
    symbolSize=5
    
    s = np.asarray(sList)
    
    absRange = rangeValue
    
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
    
    group1 = np.ma.masked_where(s > value1, s)
    group2 = np.ma.masked_where(np.logical_or(s< value1, s> value2), s)
    group3 = np.ma.masked_where(np.logical_or(s< value2, s> value3), s)
    group4 = np.ma.masked_where(np.logical_or(s< value3, s> value4), s)
    group5 = np.ma.masked_where(np.logical_or(s< value4, s> value5), s)
    group6 = np.ma.masked_where(s < value5, s)
    
    
    oneGroup1 = []
    oneGroup2 = []
    oneGroup3 = []
    oneGroup4 = []
    oneGroup5 = []
    oneGroup6 = []
    
    for grp1 in group1:
        if grp1 !='--':
            oneGroup1.append(symbolSize)
        else:
            oneGroup1.append(0)
    
    for grp2 in group2:
        if grp2 !='--':
            oneGroup2.append(symbolSize)
        else:
            oneGroup2.append(0)
    
    for grp3 in group3:
        if grp3 !='--':
            oneGroup3.append(symbolSize)
        else:
            oneGroup3.append(0)
    
    for grp4 in group4:
        if grp4 !='--':
            oneGroup4.append(symbolSize)
        else:
            oneGroup4.append(0)
            
    for grp5 in group5:
        if grp5 !='--':
            oneGroup5.append(symbolSize)
        else:
            oneGroup5.append(0)
            
    for grp6 in group6:
        if grp6 !='--':
            oneGroup6.append(symbolSize)
        else:
            oneGroup6.append(0)
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
    
    
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
    
    
    
    ax.scatter(xCoord,yCoord, s= oneGroup1, c='#3300CC', edgecolor='none', label = '~' + legendValue1)
    ax.scatter(xCoord,yCoord, s= oneGroup2, c='#3333FF', edgecolor='none', label = legendValue1 + '~' + legendValue2)
    ax.scatter(xCoord,yCoord, s= oneGroup3, c='#33CCFF', edgecolor='none', label = legendValue2 + '~' + legendValue3)
    
    ax.scatter(xCoord,yCoord, s= oneGroup4, c='#FFCC00', edgecolor='none', label = legendValue3 + '~' + legendValue4)
    ax.scatter(xCoord,yCoord, s= oneGroup5, c='#FF6600', edgecolor='none', label = legendValue4 + '~' + legendValue5)
    ax.scatter(xCoord,yCoord, s= oneGroup6, c='#FF0000', edgecolor='none', label = legendValue5 + '~')
    
    #ax.legend(loc='upper left', numpoints=6, ncol=3, fontsize=9, bbox_to_anchor=(0, 0))
    
    return fig, ax

def map2(xCoord, yCoord, estValues, tValues):
    
    valueList = []

    for ind, value in enumerate(xCoord):
        tempArray = [float(value), float(yCoord[ind]), float(estValues[ind]), float(tValues[ind])]
        valueList.append(tempArray)
    
    value1T = -1.96
    value2T = 1.96


    newValueList = []
    index = 0 
    for value in valueList:
        if (value[3] > value2T) or (value[3] < value1T):
            newValueList.append(value)
            index+=1
    
    newxCoord = []
    newyCoord = []
    newEstValues = []
    newTValues = []
    
    for newValue in newValueList:
        newxCoord.append(newValue[0])
        newyCoord.append(newValue[1])
        newEstValues.append(newValue[2])
        newTValues.append(newValue[3])
    
    symbolSize=5
      
    sEst = np.asarray(newEstValues)
    
    
    s = np.asarray(estValues)
    
    maxValue = np.amax(s)
    minValue = np.amin(s)
    
    if abs(maxValue) >= abs(minValue):
        absRange = abs(maxValue)
    else:
        absRange = abs(minValue)
      
    value1 = -(absRange/3*2)
    value2 = -(absRange/3)
    value3 = 0
    value4 = absRange/3
    value5 = absRange/3*2
      
    group1Est = np.ma.masked_where(sEst > value1, sEst)
    group2Est = np.ma.masked_where(np.logical_or(sEst< value1, sEst> value2), sEst)
    group3Est = np.ma.masked_where(np.logical_or(sEst< value2, sEst> value3), sEst)
    group4Est = np.ma.masked_where(np.logical_or(sEst< value3, sEst> value4), sEst)
    group5Est = np.ma.masked_where(np.logical_or(sEst< value4, sEst> value5), sEst)
    group6Est = np.ma.masked_where(sEst < value5, sEst)
      
      
    oneGroup1Est = []
    oneGroup2Est = []
    oneGroup3Est = []
    oneGroup4Est = []
    oneGroup5Est = []
    oneGroup6Est = []
      
    for grp1 in group1Est:
        if grp1 !='--':
            oneGroup1Est.append(symbolSize)
        else:
            oneGroup1Est.append(0)
      
    for grp2 in group2Est:
        if grp2 !='--':
            oneGroup2Est.append(symbolSize)
        else:
            oneGroup2Est.append(0)
      
    for grp3 in group3Est:
        if grp3 !='--':
            oneGroup3Est.append(symbolSize)
        else:
            oneGroup3Est.append(0)
      
    for grp4 in group4Est:
        if grp4 !='--':
            oneGroup4Est.append(symbolSize)
        else:
            oneGroup4Est.append(0)
              
    for grp5 in group5Est:
        if grp5 !='--':
            oneGroup5Est.append(symbolSize)
        else:
            oneGroup5Est.append(0)
              
    for grp6 in group6Est:
        if grp6 !='--':
            oneGroup6Est.append(symbolSize)
        else:
            oneGroup6Est.append(0)
      
      
    legendValue1 = str(round(value1,2))
    legendValue2 = str(round(value2,2))
    legendValue3 = str(round(value3,2))
    legendValue4 = str(round(value4,2))
    legendValue5 = str(round(value5,2))
              
              
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1,1)
  
    ax.scatter(newxCoord,newyCoord, s= oneGroup1Est, c='#3300CC', edgecolor='none', label = '~' + legendValue1)
    ax.scatter(newxCoord,newyCoord, s= oneGroup2Est, c='#3333FF', edgecolor='none', label = legendValue1 + '~' + legendValue2)
    ax.scatter(newxCoord,newyCoord, s= oneGroup3Est, c='#33CCFF', edgecolor='none', label = legendValue2 + '~' + legendValue3)
      
    ax.scatter(newxCoord,newyCoord, s= oneGroup4Est, c='#FFCC00', edgecolor='none', label = legendValue3 + '~' + legendValue4)
    ax.scatter(newxCoord,newyCoord, s= oneGroup5Est, c='#FF6600', edgecolor='none', label = legendValue4 + '~' + legendValue5)
    ax.scatter(newxCoord,newyCoord, s= oneGroup6Est, c='#FF0000', edgecolor='none', label = legendValue5 + '~')
      
    ax.legend(loc='upper left', numpoints=6, ncol=3, fontsize=9, bbox_to_anchor=(0, 0))
      
    return fig, ax

if __name__ == '__main__':
    
    filename1 = "_8_Urban_texas"
    filename2 = "_listwise"

    
    fieldnameList = ['Intercept', 'WHITE', 'HISP', 'BLWPOV', 'MEDINC', 'UPTOHIGH', 'INS', 'MEDICARE', 'MEDICAID','Male', 'POPDEN']
    
#     fieldnameList_t = ['std_residual']
    fieldnameList_t = []
    fieldnameList_est = []
    
    for fieldname in fieldnameList:
        fieldname_t = 't_'+fieldname
        fieldname_est = 'est_'+fieldname
        fieldnameList_t.append(fieldname_t)
        fieldnameList_est.append(fieldname_est)
    
    #change fieldnameList 
    for indx, fieldname in enumerate(fieldnameList_t):
          
        filename = filename1+filename2
               
        lstFlds, dicAttr = pyFileIO.read_CSV(filename+".csv")    
       
        #print(dicAttr)
        #print(lstFlds)
   
           
        fieldIndex = lstFlds.index(fieldname)
           
        xCoord = []
        yCoord = []
        attr1 = []
           
        for values in dicAttr.itervalues():
            #print(values)
            xCoord.append(values[2])
            yCoord.append(values[3])
            attr1.append(float(values[fieldIndex+1]))      
          
        fieldIndex1 = lstFlds.index('es'+fieldname)
         
        attr2 = []
         
        for values1 in dicAttr.itervalues():
             
            attr2.append(float(values1[fieldIndex1+1])) 
            
            
                 
        #change function
            # part 1-1 : visualization of t-values         
#         fig, ax = sig6_map1(xCoord, yCoord, attr1)
           
#         fig, ax = value6_map1(xCoord, yCoord, attr1)
         
#         fig, ax = value6_map2(xCoord, yCoord, attr1, rangeValue)

        fig, ax = map2(xCoord, yCoord, attr2, attr1)
           
        ax.set_xlabel(lstFlds[0])
        ax.set_ylabel(lstFlds[1])
        ax.axis('off')
        
        #change path 
        ax.set_title(lstFlds[fieldIndex][2:]+"_"+filename[:-9])
        fig.savefig("GWRresult/est_values1/"+filename+"_"+lstFlds[fieldIndex]+".png")
        print("save successfully")
          
     
     ## PART 2 - creating gif file 
     
     
     
#     #filepath1 = 'E:/Programming/Eclipse/Git/pygwr_bpark/'
#     filepath1 = 'D:/Programming/Project/pygwr_bpark/'
#     filepath2 = 'GWRresult/est_values1/'
#     filepath3 = 'GWRresult/gif1/'
#     fileDir = os.path.join(os.path.dirname(__file__), filepath2)
#     #print fileDir
#
#
#     #change fieldnameList 
#     for field in fieldnameList:
#         os.chdir(filepath1+filepath2)
#         os.getcwd()
#           
#         fieldname = 'est_'+field
#           
#         images = []    
#         i=1
#         while i<=12:
#             if i<10:
#                 filename3 = filename1+'0'+str(i)
#             else:
#                 filename3 = filename1+str(i)
#             i+=1    
#             filename = filename3+'_'+fieldname+'.png'
#               
#             images.append(Image.open(filename))
#       
#            
#         os.chdir(filepath1+filepath3)
#         os.getcwd()
#            
#         gifname = filename1+'_'+fieldname+'.gif'
#            
#         writeGif(gifname, images, duration=1)
#         print(gifname)
              
    

