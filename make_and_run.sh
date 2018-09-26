#!/usr/bin/env bash

make

./simplefem 

python Plot_Norms.py

python Plot_Norms_Strain.py

python Regressions.py

python Strain_Rate_Regressions.py