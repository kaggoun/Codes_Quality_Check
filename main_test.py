import glob
import sys
import os
from pathlib import Path

list = ['\n', 'def my_function():\n', '    print("Hello from a function")\n', '\n', 'def greet(name):\n', '    """\n',
        '    This function greets to\n', '    the person passed in as\n', '    a parameter\n', '    """\n',
        '    print("Hello, " + name + ". Good morning!")\n']

path = '/home/kevin/PycharmProjects/pythonProject/test1/test2/test3/**/*.py'


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
        print(f)
        print(path)
        folder_script.append(f)
        list_files.append(f.split("/")[-1])

    return list_files


print(collect_files(path))

# file_name = Path(f).stem


list_index_def = []

# Recupere et identifie les index comportant la mention "def
list_index_def = [idx for idx, i in enumerate(list) if "def" in i]
print(list_index_def)
# Recupere et identifie les index comportant des espaces
list_index_space = [i - 1 for i in list_index_def]
print(list_index_space)

print(list_index_def)


# A partir d'un fichier, insertion "@Profile" aux index identifiés dans list_index_def
for j in range(0, len(list_index_def)):
    print(j)
    print(list_index_def)

    with open("/home/kevin/PycharmProjects/Codes_Quality_Check/test1/test2/test3/test3.py", "rt") as filename:
        contents = filename.readlines()
        print(contents)
        if contents[0] == "\n":
            contents.insert(j, "from line_profiler import LineProfiler")

            try:
                from line_profiler import LineProfiler

                lprofiler = LineProfiler()


            except ImportError:
                def profile(func):
                    return func
        list_index_def_2 = [idx for idx, i in enumerate(contents) if "def" in i]
        list_index_space_2= [i - 1 for i in list_index_def_2]
        contents.insert(list_index_def_2[j], "@Profile\n")
        contents.insert(list_index_space_2[j], "\n")

    # A partir d'un fichier, écriture du contenu
    with open("/home/kevin/PycharmProjects/Codes_Quality_Check/test1/test2/test3/test3.py", "w") as filename:
        contents = "".join(contents)
        filename.write(contents)

#    os.system("python -m line_profiler "+file_name+".py.lprof")
# list.insert(i - 1, "@Profile\n")

# l=0
# open with(list,'r') as f:
#     lines=f.readlines()
#     for l in lines:
#         if 'def' in l:

