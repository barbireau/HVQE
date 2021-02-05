#!/bin/bash
#SBATCH -N 1
#SBATCH -n 2
#SBATCH -t 5-00:00:00
#SBATCH -p fat_soil_shared
#SBATCH --mem=1GB
#SBATCH --gres=gpu:1

for npar in {12..240..12}
do
python3 ~/HVQE/HVQE.py $PWD $npar 3 --cost_fn infidelity
done
