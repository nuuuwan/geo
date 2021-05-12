DIST_NAME=geo

python3 setup.py test
pylint src/$DIST_NAME

git add *
git commit -m "$1"
git pull
git push

open https://github.com/nuuuwan/$DIST_NAME
