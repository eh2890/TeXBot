#!/bin/bash

cd output/
pdflatex -halt-on-error -interaction=nonstopmode doc.tex
if [ $? -eq 0 ]; then
    echo OK
    pdfcrop doc.pdf
    pdftoppm -r 1000 doc-crop.pdf | pnmtopng > output.png
else
    echo FAIL
fi
rm doc*
cd ../
echo 'done'

