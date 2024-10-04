#!/bin/bash

python3 main.py --operation get --count 10 > url_test.txt
python3 main.py --operation extract --source url_test.txt
