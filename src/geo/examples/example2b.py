"""Example."""
import matplotlib.pyplot as plt
from geo import geodata

gpd_df = geodata.get_region_geodata('LK', 'dsd')

gpd_df['density'] = gpd_df['population'] / gpd_df['area']

gpd_df.plot(
    column='density',

    scheme='UserDefined',
    classification_kwds={
        'bins': [100, 200, 400, 800],
    },
    legend=True,
    legend_kwds={
        'labels': [
            '< 100',
            '100 - 200',
            '200 - 400',
            '400 - 800',
            '800 <',
        ],
    },
    cmap='OrRd',
    figsize=(7, 9),
)
plt.title('Population Density of Sri Lanka by DSD')

plt.savefig('%s.png' % __file__)
plt.show()
