#!/bin/bash

# Makes all the python files in current dir runnable
for i in *.py
do
    chmod +x $i
done