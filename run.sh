#!/bin/bash

if [ -f "url_test.txt" ]; then
    rm url_test.txt
fi
python3 main.py --operation get --countGet 15 > url_test.txt
python3 main.py --operation extract --countExtract 10 --source url_test.txt
