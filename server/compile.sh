#!/bin/bash

cd output/
pdflatex -halt-on-error -interaction=nonstopmode doc.tex > NUL 2>&1
if [ $? -eq 0 ]; then
    pdfcrop doc.pdf > NUL 2>&1
    pdftoppm -r 1000 doc-crop.pdf | pnmtopng > output.png
    STR=1
else
    STR=0
fi
rm doc*
rm NUL
cd ../
export STR
