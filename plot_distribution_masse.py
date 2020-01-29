import numpy as np 
import matplotlib.pyplot as plt 
import os

# pour mémoire, les données sont issues de la manip 2019_04_09_P_S_M2
# le film a été fait avec les images du plot 'Distribution de la masse'

def PARAMS():
    # chemins des fichiers data
    path = "/media/DD2/recherche/hyphes_croissance/data/2019_04_09_P_S_M2/VST/outputData/"
    return path
    
    
def plot_distribution( path, filename):
    
    f = np.loadtxt( path + filename)
    
    radius = np.sqrt( f[:,0]**2 + f[:,1]**2 )

    sort = np.argsort( radius)
    radius = radius[sort]
    f = f[sort,:]
    
    # distribution de la masse
    nbins = 50
    radius_bins = np.linspace( 0, np.max(radius), nbins)
    DM = np.array([])
    for inc in range(nbins-1) :
        DM = np.append( DM, np.sum(f[(radius > radius_bins[inc]) & (radius < radius_bins[inc+1]),2]))

    fname = 'Distribution des distance au centre des segments'
    plt.close( fname)
    plt.figure( fname)
    plt.hist( radius, bins=50)
    plt.title(filename)
    plt.xlabel('RADIUS')
#    plt.savefig('distribution_masse/' + filename + '1.png')

    fname = 'Distribution des longueurs des segments'
    plt.close( fname)
    plt.figure( fname)
    plt.hist( f[:,2], bins=50)
    plt.title(filename)
    plt.xlabel('LENGTH')
#    plt.savefig('distribution_masse/' + filename + '2.png')
    
    fname = 'Localisation des segments'
    plt.close( fname)
    plt.figure( fname)
    plt.title(filename)
    plt.plot( f[:,0], -1*f[:,1], '.k')
#    plt.savefig('distribution_masse/' + filename + '3.png')
        
    fname = 'Distribution de la masse'
    plt.close( fname)
    plt.figure( fname)
    deltaR = np.diff( radius_bins )[0]
    deltaS = np.pi *  deltaR*( deltaR + 2*radius_bins[1:] )
    plt.plot(radius_bins[1:], DM / deltaS, '-ok')
#    plt.plot(radius_bins[1:], DM , '-or')
    plt.title(filename)
    plt.xlabel('R0')
    plt.ylabel('sum Mass / dS')
    plt.savefig('distribution_masse/' + filename + '4.png')
        
    plt.show()

    return f, radius, radius_bins, DM


if __name__ == "__main__":
    
    path = PARAMS()
    allfiles = os.listdir(path)
    files = [ fname for fname in allfiles if fname.endswith('.gpickle.txt')]

    for inc in range(len(files)): 
        f, radius, radius_bins, DM = plot_distribution(path , files[inc])

