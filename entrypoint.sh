#!/usr/bin/env bash

echo "Running Spam Check on ${inputs.message}"
python main.py ${inputs.message}
echo "Spam Check Finished!"
