"""Example."""
import matplotlib.pyplot as plt
from geo import geodata

gpd_df = geodata.get_region_geodata('LK', 'dsd')

gpd_df['density'] = gpd_df['population'] / gpd_df['area']
gpd_df.plot(column='density', legend=True, cmap='OrRd')

plt.savefig('%s.png' % __file__)
plt.show()
