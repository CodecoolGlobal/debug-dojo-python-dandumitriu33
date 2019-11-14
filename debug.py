import os


def filetree(root, path="", exep=[".py", '.md']):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Print root name if this is the first call:
    if path == "":
        print("")
        print(os.path.realpath(root).split("/")[-1])

    # Get files in current folder:
    files = sorted(os.listdir(root))
    files_filtered = [item for item in files if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in exep)]
    nfiles = len(files_filtered)

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(nfiles):
        if i == nfiles - 1:
            newpath = path + "    "
            arrow = "`-- "
        print("{:s}{:s}{:s}".format(path, arrow, files_filtered[i]))
        # Recursive call to print the content of sub-folders:
        filetree("{:s}/{:s}".format(root, files_filtered[i]), newpath, exep)


def main():
    filetree(".")


if __name__ == '__main__':
    main()
