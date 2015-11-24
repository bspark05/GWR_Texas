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
    
    symbolSize=10
    
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
    
    symbolSize=10
    
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
    
    symbolSize=10
    
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

if __name__ == '__main__':
    
#     filename1 = "SaleApartment2014"
#     filename2 = "_GWR_listwise"
    filename1 = "_8_Urban_texas"
    filename2 = "_listwise"

    
#     fieldnameList = ['Intercept', 'AGE', 'COMPLEX', 'COMDIST', 'SUBWAY', 'MAJROAD', 'AGEAVE', 'POPDEN', 'BLSPOPF', 'FIRENO', 'CAR2012R', 'TAX', 'AREA_1', 'FLOOR1_1']     
    rangeList = [7.00, 0.2, 0.13, 0.1, 0.1, 0.06, 3.6, 0.3, 12, 0.01, 1.16, 0.31, 0.71, 0.11]
    
    fieldnameList = ['Intercept', 'WHITE', 'HISP', 'BLWPOV', 'MEDINC', 'UPTOHIGH', 'INS', 'MEDICARE', 'MEDICAID','Male', 'POPDEN']
    
    for idx, field in enumerate(fieldnameList):
        fieldname = 'est_'+field
        rangeValue = rangeList[idx]
        print(rangeValue) 
          
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
          
                 
        fig, ax = sig6_map1(xCoord, yCoord, attr1)
           
#         fig, ax = value6_map1(xCoord, yCoord, attr1)
         
#         fig, ax = value6_map2(xCoord, yCoord, attr1, rangeValue)
           
        ax.set_xlabel(lstFlds[0])
        ax.set_ylabel(lstFlds[1])
        ax.axis('off')
        ax.set_title(lstFlds[fieldIndex]+"_"+filename[:-9])
        fig.savefig("GWRresult/t_values/"+filename+"_"+lstFlds[fieldIndex]+".png")
        print("save successfully")
          
     
     
     
#     #filepath1 = 'E:/Programming/Eclipse/Git/pygwr_bpark/'
#     filepath1 = 'D:/Programming/Project/pygwr_bpark/'
#     filepath2 = 'GWRresult/est_values1/'
#     filepath3 = 'GWRresult/gif1/'
#     fileDir = os.path.join(os.path.dirname(__file__), filepath2)
#     #print fileDir
#       
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
              
    

