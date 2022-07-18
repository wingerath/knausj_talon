tag: user.tabs
-
go tab (open | new): app.tab_open()
go tab (last | previous): app.tab_previous()
go tab next: app.tab_next()
go tab close: user.tab_close_wrapper()
go tab (reopen|restore): app.tab_reopen()
go tab <number>: user.tab_jump(number)
go tab final: user.tab_final()
tab duplicate: user.tab_duplicate()
