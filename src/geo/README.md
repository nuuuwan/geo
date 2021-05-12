# Geo

**Geo** is a python library for drawing maps of Sri Lanka and its various [administrative regions](https://en.wikipedia.org/wiki/Administrative_divisions_of_Sri_Lanka) (Provinces, Districts, DSDs, GNDs etc). It fundalemtally plays to following functions:
1. Implements data fetching, that pulls TopoJSON data from https://github.com/nuuuwan/geo-data
2. Implements map drawing, which wraps around [geopandas](https://geopandas.org/) and [mapplotlib](https://matplotlib.org/)
3. Provides some examples that pull data from [GIG ("Generalized Information Graph")](https://test.pypi.org/project/gig-nuuuwan/), which itself provices access to various data related to Sri Lanka.

# Installing Geo

```bash
pip install -i https://test.pypi.org/simple/ geo-nuuuwan
```

or

```bash
pip install geo-nuuuwan
```

# Example Map Plots

## Sri Lanka with Province Boundaries

```python
from geo import geo

region_geodata = geo.get_region_geodata('LK', 'province')
geo.plot_geodata(region_geodata, 'Sri Lanka with Province Boundaries')
```

## Colombo District with DSD Boundaries

```python
region_geodata = get_region_geodata('LK-11', 'dsd')
plot_geodata(region_geodata, 'Colombo District with DSD Boundaries')
```
