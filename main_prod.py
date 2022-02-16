import glob
import sys
import os
from pathlib import Path



path = '/home/kevin/PycharmProjects/Codes_Quality_Check/**/*.py'

def collect_files(path):
    """
       collect all .py files from specified path
       Parameters
       ----------
      path: string
      path to python files
       Return
       ----------
       list_files: list
       list containing all names of python files
    """
    folder_script = []
    list_files = []

    for f in glob.glob(path, recursive=True):
        folder_script.append(f)
        list_files.append(f.split("/")[-1])

    return folder_script


data=collect_files(path)


def insert_def(data):
    """
       Insertion of "@Profile" if a python script contains a function

       Parameters
       ----------
       data:list
       path to python files

       Return
       ----------
       Write on each python script "@Profile"

    """
    for filename in data:
        with open(filename, "r") as f:
            text = f.readlines()
            #print(text)

            list_index_def = [idx for idx, i in enumerate(text) if "def" in i]

            #print(list_index_def)

            for j in range(0, len(list_index_def)):

                if text[0] == "\n":
                    text.insert(j, "import line_profiler\n"+"import atexit\n"+"profile = line_profiler.LineProfiler()\n"+"atexit.register(profile.print_stats)\n")

                    try:
                        from line_profiler import LineProfiler

                        lprofiler = LineProfiler()


                    except ImportError:

                        def profile(func):
                            return func

                list_index_def_2 = [idx for idx, i in enumerate(text) if "def" in i]

                #print(list_index_def_2)

                text.insert(list_index_def_2[j], "@profile\n")
        with open(filename, "w") as f:
            text = "".join(text)
            f.write(text)

    return filename

insert_def(data)



