"""Setup."""
import time
import setuptools
DIST_NAME = 'geo'

IS_PRE_RELEASE = False
MAJOR, MINOR, PATCH = 1, 0, 0
if IS_PRE_RELEASE:
    PRE_RELEASE_LABEL = '%d' % (time.time())
    version = '%d.%d.%drc%s' % (MAJOR, MINOR, PATCH, PRE_RELEASE_LABEL)
else:
    version = '%d.%d.%d' % (MAJOR, MINOR, PATCH)

with open("src/%s/README.md" % DIST_NAME, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="%s-nuuuwan" % DIST_NAME,
    version=version,
    author="Nuwan I. Senaratna",
    author_email="nuuuwan@gmail.com",
    description="Generalized information graph.",
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
