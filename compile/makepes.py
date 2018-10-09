import numpy as np
import matplotlib.pyplot as plt

colors = {"shiv_purple" : 'darkorchid',
"shiv_blue" : 'dodgerblue',
"shiv_green" : '#00933C',
"shiv_yellow" : '#FCCB09',
"shiv_orange" : 'darkorange',
"shiv_red" : '#EE352E'}

def double_well(x,E,C):
    return E*((C*(x**4))-(x**2))

def plot1():
    fig = plt.figure()
    x_min = -1.5
    x_max = 1.5
    num_pts = 1000
    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)

    plt.plot(x,y,color = colors["shiv_blue"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("double_well.eps")

def plot2():
    fig = plt.figure()

    x_min = -1.5
    x_max = 1.5
    num_pts = 1000

    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)

    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[-0.1,-0.1],linestyle='--',color=colors["shiv_red"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("double_well2.eps")

def plot3():
    fig = plt.figure()

    x_min = -1.5
    x_max = 1.5
    num_pts = 1000

    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)

    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("double_well3.eps")

def plot4():
    fig = plt.figure()

    x_min = -1.5
    x_max = 1.5
    num_pts = 1000

    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)

    plt.plot(x,y,color = colors["shiv_blue"],linestyle='--')

    x = np.linspace(x_min,x_max,num_pts)

    y_new = double_well(x,1,0.55)
    E = y[0]/y_new[0]
    y = double_well(x,E,0.55)


    plt.plot(x,y,color = colors["shiv_purple"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    #plt.plot([x_min,x_max],[0.05,0.05],linestyle='--',color="black")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("double_well4.eps")

def gaussian(x,center,height,w):
    return np.exp(-(x-center)**2/(2*w*w))*height/(np.sqrt(2*np.pi*w*w))


def plot5():
    fig = plt.figure()
    x_min = -1.5
    x_max = 1.5
    num_pts = 1000
    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)
    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    y = gaussian(x,-1,0.01,0.05)
    y -= 0.5
    plt.plot(x,y,color = colors["shiv_green"])

    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("metadynamics1.eps")

def plot7():
    fig = plt.figure()
    x_min = -1.5
    x_max = 1.5
    num_pts = 1000
    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)
    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    y = gaussian(x,-1,0.01,0.05)
    y += gaussian(x,-1.1,0.01,0.05)
    # y += gaussian(x,-0.9,0.01,0.05)
    # for i in range(15):
    #     y += gaussian(x,-1+(0.2*np.random.randn()),0.01,0.05)
    y -= 0.5
    plt.plot(x,y,color = colors["shiv_green"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("metadynamics2.eps")

def plot8():
    fig = plt.figure()
    x_min = -1.5
    x_max = 1.5
    num_pts = 1000
    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)
    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    y = gaussian(x,-1,0.01,0.05)
    y += gaussian(x,-1.1,0.01,0.05)
    y += gaussian(x,-1.15,0.01,0.05)
    y += gaussian(x,-1.14,0.01,0.05)
    y += gaussian(x,-0.89,0.01,0.05)
    y += gaussian(x,-0.90,0.01,0.05)
    y += gaussian(x,-0.95,0.01,0.05)
    y += gaussian(x,-0.82,0.01,0.05)
    y += gaussian(x,-1.1,0.01,0.05)
    # y += gaussian(x,-0.9,0.01,0.05)
    # for i in range(15):
    #     y += gaussian(x,-1+(0.2*np.random.randn()),0.01,0.05)
    y -= 0.5
    plt.plot(x,y,color = colors["shiv_green"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("metadynamics3.eps")

def plot9():
    fig = plt.figure()
    x_min = -1.5
    x_max = 1.5
    num_pts = 1000
    x = np.linspace(x_min,x_max,num_pts)
    y = double_well(x,1,0.5)
    plt.plot(x,y,color = colors["shiv_blue"])
    plt.plot([x_min,x_max],[0.1,0.1],linestyle='--',color=colors["shiv_red"])
    y = gaussian(x,-1,0.01,0.05)
    for i in range(50):
        y += gaussian(x,-1+(1.0*(np.random.random()-0.5)),0.01,0.05)
    y -= 0.5
    plt.plot(x,y,color = colors["shiv_green"])
    plt.xlabel(r"$x$")
    plt.ylabel(r"$V(x)$")
    fig.set_tight_layout(True)
    plt.savefig("metadynamics4.eps")
def plot6():
    for i in range(5):
        fig = plt.figure()
        x_min = -1.5
        x_max = 1.5
        num_pts = 1000
        x = np.linspace(x_min,x_max,num_pts)
        y = double_well(x,1,0.5)
        plt.plot(x,y,color = colors["shiv_blue"])
        T = 0.1 + (i*0.05)
        plt.plot([x_min,x_max],[T,T],linestyle='--',color=colors["shiv_red"])
        plt.xlabel(r"$x$")
        plt.ylabel(r"$V(x)$")
        fig.set_tight_layout(True)
        plt.savefig("pt{}.eps".format(i))




plot1()
plot2()
plot3()
plot4()
plot5()
plot6()
plot7()
plot8()
plot9()
