#!/bin/sh -l

echo "Running Spam Check on the message: $1"
cd /usr/bin/
python main.py "$1"
echo "Spam Check Finished!"
