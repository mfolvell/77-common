#!/bin/bash
set -e
set -u
if ! rpm -qa | grep -qw xmlstarlet; then
    echo " ************* Install av xmlstarlet ************* "
    sudo yum -y install xmlstarlet
    clear
fi

git remote update
if git diff-index --quiet HEAD --; then
   echo "There is no local change.  release can continue"
else
   echo "WARNING! Your branch has diverged from origin."
   echo "You may consider running git pull/push before releasing"
   read -p "Continue anyway [Yn]? " -n 1 -r
   echo
   if [[ ! $REPLY =~ ^[Yy]$ ]]; then
     echo "aborted"
     exit 1
   fi
fi

ver=$( xmlstarlet sel -N 'x=http://maven.apache.org/POM/4.0.0' \
    -t -v "//x:project/x:version" pom.xml )
version=${ver//-SNAPSHOT/}

echo "Creating release for version: "$version
read -p "Continue [Yn]? " -n 1 -r

git tag -a "v$version" -m "Releasing version $version"

# git add pom.xml
# git commit -m "Endret pom (fjernet SNAPSHOT fra version)"
# git push -u origin $branch_name
#
# git checkout master
mvn release:update-versions
git push origin "v$version"
git add pom.xml
git commit -m "Bompet versjonsnr i pom.xml"
git push -u origin master
