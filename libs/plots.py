# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colorbar as clb
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

from matplotlib import ticker
from matplotlib.ticker import LogLocator

# customized library by Lucas Hale
from libs.DataModelDict import DataModelDict as dmd


def plotSingle2DLinear(comp,xtitle,ytitle,xscale,yscale):
	p_alpha = 1
	volume=50
	fig, ax = plt.subplots(figsize=(12, 9))

	ax.plot(comp[:,0],comp[:,1],lw=3)

	ax.set_xlabel(xtitle, fontsize=35, labelpad=15)
	ax.set_ylabel(ytitle, fontsize=35, labelpad=15)
	ax.tick_params(axis='x', labelsize=25, pad = 10)
	ax.tick_params(axis='y', labelsize=25, pad = 10)

	ax.set_xscale(xscale, nonposx='clip')
	ax.set_yscale(yscale, nonposx='clip')

	ax.set_xlim(950, 1150)
	ax.set_ylim(0, 1)

	ax.grid(True)
	fig.tight_layout()


	plt.show()

	return None


def plotDouble2DLinear(comp,comp2,xtitle,ytitle,y2title,xscale,yscale,y2scale):
	p_alpha = 1
	volume=50
	fig, ax = plt.subplots(figsize=(12, 9))
	ax2 = ax.twinx()

	ax.plot(comp[:,0],comp[:,1],lw=3, color='blue')
	ax2.plot(comp2[:,0],comp2[:,1],lw=3, color='red')

	ax.set_xlabel(xtitle, fontsize=35, labelpad=15)
	ax.set_ylabel(ytitle, fontsize=35, labelpad=15, color='blue')
	ax2.set_ylabel(y2title, fontsize=30, labelpad=15, color='red')
	ax.tick_params(axis='x', labelsize=25, pad = 10)
	ax.tick_params(axis='y', labelsize=25, pad = 10, colors='blue')
	ax2.tick_params(axis='y', labelsize=25, pad = 10, colors='red')

	ax.set_xscale(xscale, nonposx='clip')
	ax.set_yscale(yscale, nonposx='clip')
	ax2.set_yscale(y2scale, nonposx='clip')

	ax.locator_params(axis='x', nbins = 4)
	ax.locator_params(axis='y', nbins = 4)
	ax2.locator_params(axis='y', nbins = 4)

	ax.grid(True)
	fig.tight_layout()


	plt.show()

	return None


def plotdilatom(ascfile,comp,xtitle,ytitle,xscale,yscale):

	text_file = open(ascfile, "r")
	qdata = dmd(text_file)
	#print qdata.xml(indent=2)

	table = qdata.find('tabularData')
	distable = []
	for row in table['rows'].iterlist('row'):
		disrow = []
		for column in row.iterlist('column'):
			disrow.append(column['#text'])
		distable.append(disrow)
    
	del distable[0]
	#L0 = distable[0][2] 
	#print L0
	#print distable
	distable = np.array(distable)

        p_alpha = 1
        volume=50
        fig, ax = plt.subplots(figsize=(12, 9))

        ax.plot(comp[:,0],comp[:,1],lw=3)
	ax.plot(distable[:,1]+273.15,distable[:,2]/15000,'o') #,markevery=2)
        ax.set_xlabel(xtitle, fontsize=35, labelpad=15)
        ax.set_ylabel(ytitle, fontsize=35, labelpad=15)
        ax.tick_params(axis='x', labelsize=25, pad = 10)
        ax.tick_params(axis='y', labelsize=25, pad = 10)

        ax.set_xscale(xscale, nonposx='clip')
        ax.set_yscale(yscale, nonposx='clip')

        ax.set_xlim(800,1200)
        #ax.set_ylim(0, 50)

        ax.grid(True)
        fig.tight_layout()


        plt.show()


        return None

