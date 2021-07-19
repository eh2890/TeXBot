#!/bin/bash

pdflatex -output-directory=output doc.tex
cd output/
pdfcrop doc.pdf
pdftoppm -r 1000 doc-crop.pdf | pnmtopng > output.png
rm doc*
cd ../
echo 'done'

