### Make Jupyter notebook cells display output for ALL lines, not just the
### last line!

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Valid arguments:
# * "all"         Show results for all lines which give output.
# * "none"        Show no output.
# * "last"        If the cell ends in a loop, show results from each iteration
# * "last_expr"   DEFAULT. Show the very last thing only, e.g. result from final
#                 iteration of loop.