#!/usr/bin/python3

# 2022-jan-08 dlg created

import os

directory = os.getcwd()
with open('artifacts.h', 'w') as f:
    for item in os.scandir(directory):
        if (item.path.endswith(".pem") or item.path.endswith(".p7s")) and item.is_file():
            macro_name = item.name.upper().replace('.', '_')
            with open (item.name, "r") as current_file:
                file_contents_as_string= current_file.read().replace('\n', '\\n').replace('"', '\\"')
            f.write('#define ' + macro_name + ' "data:,' + file_contents_as_string + '"\n\n')
