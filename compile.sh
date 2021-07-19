#!/bin/bash

cd output/
pdflatex doc.tex
pdfcrop doc.pdf
pdftoppm -r 1000 doc-crop.pdf | pnmtopng > output.png
rm doc*
cd ../
echo 'done'

