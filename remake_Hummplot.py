from astropy.table import Table
import pandas

dat = Table.read('ray_rho_0032_0401.fits', format='fits')
df  = dat.to_pandas()
 
#df.wavelength # in angstroms
#df.flux       # relative flux 
#df.tau        # opacity; optical depth; (can get line density)

plt.plot(df.wavelength,df.flux)
plt.ylim(0,2.5)
plt.show()
