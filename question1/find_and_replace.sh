#!/bin/bash

if ! [ $# -eq 2 ]; then
    echo Usage: ./find_and_replace \<find\> \<replace\>
    exit 1
fi

mkdir -p replace

cp *.txt replace/
cd replace

sed -i .bak "s/$1/$2/g" *
rm *.bak

cd ..
