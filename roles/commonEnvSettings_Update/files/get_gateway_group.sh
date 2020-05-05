pathTopolopy=$2/groups
GROUPNO=$(jq --arg inputParam "$1" --slurp '.[].groups[] | select(.name==$inputParam) | .id' $pathTopolopy/topology.json)
echo "${GROUPNO//'"'}"
