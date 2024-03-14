from typing import Any, List


def make_latex_table(table: List[List[Any]] = None, need_base=False):
    if not table:
        yield None

    start_common = "\\begin{center}\n\\begin{tabular}{ |" + 'c|' * len(table[0]) + " } \n \\hline\n"
    end_common = "\\end{tabular}\n\\end{center}\n"

    if need_base:
        yield "\\documentclass{article}\n\\begin{document}\n" + start_common
    else:
        yield start_common

    for row in table:
        yield f" {' & '.join(map(str, row))} \\\\\n \\hline\n"

    if need_base:
        yield end_common + "\\end{document}\n"
    else:
        yield end_common


def create_base_latex_and_insert_image(img_path: str):
    yield "\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n"
    yield "\\includegraphics[width=\\textwidth]{" + img_path + "}\n"
    yield "\\end{document}\n"

