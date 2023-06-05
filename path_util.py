# path_util script is taken from @jadenhensley on GitHub. is used for cross platform directory loading

import os
import re
import pathlib

def get_project_directory():
    SCRIPTPATH = os.path.realpath(__file__)
    # print("Script path: ", SCRIPTPATH)

    path = [""]
    i = 0

    if os.name == 'nt':
        backslash_count = SCRIPTPATH.count("\\")

        for char in SCRIPTPATH:
            if "\\" == char:
                i += 1
            # print(path)
            if i != backslash_count:
                path[0] += char

        # print(path)

        before = pathlib.PureWindowsPath(rf'{path}')
        before = pathlib.PurePosixPath(rf'{path}')
        after_path = before.as_posix().replace('[','').replace(']', '').replace("'",'')
        # .pop(']').pop('[')
        

    elif os.name == "posix":
        forwardslash_count = SCRIPTPATH.count("/")
        print(forwardslash_count)

        for char in SCRIPTPATH:
            if "/" == char:
                i += 1
            if i != forwardslash_count:
                path[0] += char
        after_path = path[0].replace('[','').replace(']', '').replace("'",'')
        print(after_path)
    return after_path

#get_project_directory()