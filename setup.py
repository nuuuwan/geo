"""Setup."""

import setuptools

DIST_NAME = 'geo'
MAJOR, MINOR, PATCH = 1, 0, 3
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="%s-nuuuwan" % DIST_NAME,
    version=VERSION,
    author="Nuwan I. Senaratna",
    author_email="nuuuwan@gmail.com",
    description="Geographic Utilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nuuuwan/%s" % DIST_NAME,
    project_urls={
        "Bug Tracker": "https://github.com/nuuuwan/%s/issues" % DIST_NAME,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'geopandas',
        'shapely',
        'utils-nuuuwan',
        'gig-nuuuwan',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
