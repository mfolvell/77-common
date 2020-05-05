#!/bin/sh
if [ "$1" = "" ]; then
    echo "Usage: sh run.sh sampledir/scriptname.py"
    exit
fi;
path="`pwd`"
JYTHONPATH=$path:$JYTHONPATH; export JYTHONPATH
LOCDIR=$path; export LOCDIR
JSH=$LOCDIR/../../posix/bin/jython; export JSH

dir=`dirname $1`
file=`basename $1`

shift

cd $dir
exec "$JSH" "$file" "$@"
cd $LOCDIR
