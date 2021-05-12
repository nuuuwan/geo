DIST_NAME=geo

cd docs

rm -rf build
make clean
rm source/utils.rst
rm source/modules.rst
sphinx-apidoc -f -o source ../src/$DIST_NAME

make html

open _build/html/source/$DIST_NAME.html
open https://${DIST_NAME}-nuuuwan.readthedocs.io/en/latest/?
