DIST_NAME=geo

python3 setup.py test
pylint src/$DIST_NAME


COMMIT_MSG="Auto ($(date))"
echo $COMMIT_MSG

git add *
git commit -m $COMMIT_MSG
git pull
git push

open https://github.com/nuuuwan/$DIST_NAME
