#!/bin/bash

if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    exit -1    
fi

num=$1
mkdir $num
cp blank.py $num/script.py
chmod +x $num/script.py
echo "Write the sample input"
cat > $num/input
cd $num
subl . &
