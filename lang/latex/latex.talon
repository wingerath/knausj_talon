mode: user.latex
mode: command
title:/TeXstudio$/
language:/.*/
-
active language: "LaTeX working"

LaTeX Frau Studentin: "\\mannOderFrau{{Student}}{{Herr}}{{Frau}} \\nachnameTitel{{Student}}"

# IDE commands
compile: key("ctrl-t")

keyword: user.simple_command("textkeyword")
emphasized: user.simple_command("textemph")

translation: insert('\\gerEn{{}}{{}}')
language switch: insert('\\ifthenelse{{\\isGer}}{{\n\n}}{{\n\n}}')

(cite reference|citation): user.simple_command("cite")
footnote: user.simple_command("footnote")
horizontal space: user.simple_command("hspace*")
vertical space: user.simple_command("vspace*")
input: user.simple_command("input")
label: user.simple_command("label")
(ref|reference): user.simple_command("ref")
underline: user.simple_command("underline")
you line: user.simple_command("uline")
use package: user.simple_command("usepackage")

hyperlink:
    insert('\\href{{https://}}{{}}')
    key("left")

section: user.simple_command("section")
subsection: user.simple_command("subsection")
subsubsection: user.simple_command("subsubsection")

# figures
figure:
    insert("""\\begin{{figure}}
        \\centering
        \\includegraphics[width=\\textwidth]{{}}
        \\caption{{}}
        \\label{{fig:}}
    \\end{{figure}}""")
    key("up shift-up shift-up shift-up tab down end left")
subfigure:
    insert("""\\begin{{figure}}
                   \\centering
                   \\begin{{subfigure}}[b]{{0.3\\textwidth}}
                       \\centering
                       \\includegraphics[width=\\textwidth]{{graph1}}
                       \\caption{{$y=x$}}
                       \\label{{fig:y equals x}}
                   \\end{{subfigure}}
                   \\hfill
                   \\begin{{subfigure}}[b]{{0.3\\textwidth}}
                       \\centering
                       \\includegraphics[width=\\textwidth]{{graph2}}
                       \\caption{{$y=3sinx$}}
                       \\label{{fig:three sin x}}
                   \\end{{subfigure}}
                   \\hfill
                   \\begin{{subfigure}}[b]{{0.3\\textwidth}}
                       \\centering
                       \\includegraphics[width=\\textwidth]{{graph3}}
                       \\caption{{$y=5/x$}}
                       \\label{{fig:five over x}}
                   \\end{{subfigure}}
                      \\caption{{Three simple graphs}}
                      \\label{{fig:three graphs}}
              \\end{{figure}}""")

# lists
enumerate: user.list_environment("enumerate")
itemize: user.list_environment("itemize")
item: "\\item "

# singular commands
line break: '{{\\linebreak}}'
