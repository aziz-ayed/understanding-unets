#!/bin/bash
#MSUB -r train_learnlets_undecimated              # Request name
#MSUB -n 1                         # Number of tasks to use
#MSUB -c 2                         # I want 2 cores per task since io might be costly
#MSUB -x
#MSUB -T 86400                      # Elapsed time limit in seconds
#MSUB -o learnlet_train_subclassed_%I.o              # Standard output. %I is the job id
#MSUB -e learnlet_train_subclassed_%I.e              # Error output. %I is the job id
#MSUB -q v100               # Queue
#MSUB -Q normal
#MSUB -m scratch,work
#MSUB -@ zaccharie.ramzi@gmail.com:begin,end
#MSUB -A gch0424                  # Project ID

set -x
cd $workspace/understanding-unets

. ./submission_scripts/env_config.sh

ccc_mprun -E '--exclusive' -n 1 python3 ./learning_wavelets/training_scripts/learnlet_subclassed_training.py -nf 64 -u&

wait  # wait for all ccc_mprun(s) to complete.
