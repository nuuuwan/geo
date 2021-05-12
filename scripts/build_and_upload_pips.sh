DIST_NAME=geo
REPOSITORY=testpypi
REPOSITORY_DOMAIN=test.pypi

# Build
scripts/clean.sh
python3 -m build

# Upload
python3 -m twine upload --repository $REPOSITORY dist/*

# View Project
open https://$REPOSITORY_DOMAIN.org/project/$DIST_NAME-nuuuwan/
