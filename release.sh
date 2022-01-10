#!/bin/bash
set -e
set -u
git remote update
if git diff-index --quiet HEAD --; then
   echo "Det er INGEN lokale endringer.  release kan fortsette"
else
   echo "ADVARSEL! Din branch haer lokale endringer som IKKE er commitet."
   echo "Du bør vurdere git pull/push før kjøring av relase"
   read -p "Forsette [Yn]? " -n 1 -r
   echo
   if [[ ! $REPLY =~ ^[Yy]$ ]]; then
     echo "aborted"
     exit 1
   fi
fi

ver=$( xmllint --xpath "/*[name()='project']/*[name()='version']/text()" pom.xml )
version=${ver//-SNAPSHOT/}

echo "Lage release for version: "$version
read -p "Fortsette [Yn]? " -n 1 -r

git tag -a "v$version" -m "Releasing version $version"

branch_name="release/v$version"
echo "Ny release branch" "$branch_name"
git branch "release/v$version"
git push -u origin "$branch_name"
git co master

mvn release:update-versions
git push origin "v$version"
git add pom.xml
git commit -m "Bompet versjonsnr i pom.xml"
git push -u origin master