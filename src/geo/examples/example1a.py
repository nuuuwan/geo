"""Example."""
import matplotlib.pyplot as plt
from geo import geodata

gpd_df = geodata.get_region_geodata('LK-11', 'dsd')
gpd_df.plot()
plt.show()
