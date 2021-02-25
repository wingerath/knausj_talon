mode: user.latex
mode: command
and code.language: latex
-
active language: "LaTeX working"

# IDE commands
compile: key("ctrl-t")

keyword: user.simple_command("textkeyword")
emphasized: user.simple_command("textemph")


(cite|citation): user.simple_command("cite")
input: user.simple_command("input")
label: user.simple_command("label")
(ref|reference): user.simple_command("ref")

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
        \label{{fig:}}
    \end{{figure}}""")
    key("up shift-up shift-up shift-up tab down end left")

# lists
enumerate: user.list_environment("enumerate")
itemize: user.list_environment("itemize")
item: "\\item "
