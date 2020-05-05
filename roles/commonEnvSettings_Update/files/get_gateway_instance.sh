pathTopolopy=$1/groups
INSTANCE=$(jq --arg hostnameShort "$2" --slurp '.[].groups[].services[] | select (.id | contains("instance")) | select(.name==$hostnameShort) |.id' $pathTopolopy/topology.json)

echo "${INSTANCE//'"'}"
