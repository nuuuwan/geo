import matplotlib.pyplot as plt
from geo import geodata

gpd_df = geodata.get_region_geodata('LK', 'province')
gpd_df.plot()
plt.show()
