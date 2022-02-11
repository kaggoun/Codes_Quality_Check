import glob
import sys
import os
from line_profiler import LineProfiler
import random
from pathlib import Path


folder_script=[]
list_files=[]


for f in glob.glob('/home/kevin/PycharmProjects/pythonProject/test1/test2/test3/**/*.py', recursive=True):
    print(f)
    folder_script.append(f)
    list_files.append(f.split("/")[-1])

# with open(f,"r") as fp:
#    lines = fp.readlines()
#    cnt = 1
#    while lines:
#        print("Line {}: {}".format(cnt, lines.strip()))
#        lines = fp.readline()
#        cnt += 1#        if "def" in lines:
#           print(cnt)

i = 0
with open(f,"rt") as filename:
     contents = filename.readlines()
     print(contents)
     list_index_def=[]
     for i in range(len(contents)):
         if "def" in contents[i]:
             print(contents[i]+"OK")
             list_index_def.append(i)
             contents.insert(i, "@Profile\n")

print(list_index_def)

# print(list)
# for i in range(len(list)):
#     if "def" in list[i]:
#         print(list[i] + "OK")
        # list.insert(i - 1, "@Profile\n")

with open(f, "w") as filename:
     contents = "".join(contents)
     filename.write(contents)

# with open(f, "w") as filename:
#     content = "".join(contents)
#     filename.write(content)

# with open(f, "w") as filename:
#      contents = "".join(contents)
#      print(contents)
#      filename.write(contents)



# data.insert(data.index("def"), 'spromt')
#
# with open(f, "w") as outputfile:
#     outputfile.write('\n'.join(data))


#REcupere toutes les fonctions d'un script dans out.txt
# with open(f) as f:
#     lines = f.readlines()
#     lines = [l for l in lines if "def" in l]
#     with open("out.txt", "w") as f1:
#         f1.writelines(lines)
#         print(f1)
# #
#
# for i in range(0,len(list_files)):
#     print(i)
#     open(list_files[i][0:-3] + ".txt", "w+")
#     print(list_files[i][0:-3] )
#     open(folder_script[i][0:-3] + ".txt", "w+")
#     print(folder_script[i])
#     f= os.system("flake8 --statistics "+ list_files[i] + " > " + list_files[i][0:-3]+".txt")
#
#    # os.system("kernprof -l -v " + list_files[i] + " > " + list_files[i][0:-3])
#     # os.system("python -m line_profiler " + list_files[i] + " > " + list_files[i][0:-3])

#
#     if lines[len(lines)] == "def" & lines[len(lines)-1] == "\n":

#         f.write("@Profile")
#


#         if lines[len(lines) - 1] == '\n':
#             file.write("newRow")
#
#
#
#
# print("Run successful")
