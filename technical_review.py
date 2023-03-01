# parse the cells tag and add "-*" at the end of a tag beginning with "figure"
import sys
import nbformat


def add_figure_tag(notebook):
    for cell in notebook.cells:
        tags = cell.get("metadata", {}).get("tags", [])
        if tags:
            for tag in tags:
                if tag.startswith("figure"):
                    print("add -* to the tag: {}".format(tag))
                    tags.append(tag + "-*")
                    tags.remove(tag)
                    break
    return notebook



# main function
def main():
    # get the notebook file name
    notebook_file = sys.argv[1]
    # read the notebook file
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)
    # add the figure tag
    nb = add_figure_tag(nb)
    # write the notebook file
    with open(notebook_file, 'w') as f:
        nbformat.write(nb, f)


#call the main function
if __name__ == '__main__':
    main()

#call the script from the terminal
#!python technical_review.py paper.ipynb

#call the script from the notebook
#%run technical_review.py paper.ipynb