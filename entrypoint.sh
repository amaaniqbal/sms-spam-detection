#!/bin/sh -l

echo "Running Spam Check on the message: $1"
python /usr/bin/main.py "$1"
echo "Spam Check Finished!"
