mode: dictation
-
#everything here should call auto_insert to preserve the state to correctly auto-capitalize/auto-space.
<user.text>: auto_insert(text)
enter: auto_insert("new-line")
{user.punctuation}: auto_insert(punctuation)
cap <user.text>:
    result = user.formatted_text(user.text, "CAPITALIZE_FIRST_WORD")
    auto_insert(result)
#navigation
go up <number_small> times:
    edit.up()
    repeat(number_small - 1)
go down <number_small> times:
    edit.down()
    repeat(number_small - 1)
go left <number_small> times:
    edit.left()
    repeat(number_small - 1)
go right <number_small> times:
    edit.right()
    repeat(number_small - 1)
go before <number_small> times:
    edit.word_left()
    repeat(number_small - 1)
go after <number_small> times:
    edit.word_right()
    repeat(number_small - 1)
go up: edit.up()
go down: edit.down()
go left: edit.left()
go right: edit.right()
go before: edit.word_left()
go after: edit.word_right()
go way left: edit.line_start()
go way right: edit.line_end()
#selection
mark up <number_small> times:
    edit.extend_line_up()
    repeat(number_small - 1)
mark down <number_small> times:
    edit.extend_line_down()
    repeat(number_small - 1)
mark left <number_small> times:
    edit.extend_left()
    repeat(number_small - 1)
mark right <number_small> times:
    edit.extend_right()
    repeat(number_small - 1)
mark before <number_small> times:
    edit.extend_word_left()
    repeat(number_small - 1)
mark after <number_small> times:
    edit.extend_word_right()
    repeat(number_small - 1)
mark left <number_small> times:
    edit.extend_left()
    repeat(number_small - 1)
mark right <number_small> times:
    edit.extend_right()
    repeat(number_small - 1)
mark up: edit.extend_line_up()
mark down: edit.extend_line_down()
mark before: edit.extend_word_left()
mark after: edit.extend_word_right()
mark left: edit.extend_left()
mark right: edit.extend_right()
mark way left: edit.extend_line_start()
mark way right: edit.extend_line_end()
#clear left <number_small> words:
#    edit.extend_word_left()
#    repeat(number_small - 1)
#    edit.delete()
#clear right <number_small> words:
#    edit.extend_word_right()
#    repeat(number_small - 1)
#    edit.delete()
#(clear left | wipe) <number_small> characters:
#    edit.extend_left()
#    repeat(number_small - 1)
#    edit.delete()
#(clear | clear right | delete) <number_small> characters:
#    edit.extend_right()
#    repeat(number_small - 1)
#    edit.delete()
#formatting
formatted <user.format_text>:
    user.auto_format_pause()
    auto_insert(format_text)
    user.auto_format_resume()
^format selection <user.formatters>$:
    user.formatters_reformat_selection(formatters)
#corrections
#scratch that: user.clear_last_utterance()
#scratch selection: edit.delete()
mark that: user.select_last_utterance()
spell that <user.letters>: auto_insert(letters)
spell that <user.formatters> <user.letters>:
    result = user.formatted_text(letters, formatters)
    user.auto_format_pause()
    auto_insert(result)
    user.auto_format_resume()
#escape, type things that would otherwise be commands
^escape <user.text>$:
    auto_insert(user.text)

wipe <number_small> times:
    key("backspace")
    repeat(number_small - 1)
wipe: key("backspace")


space: key("space")
undo: key("ctrl-z")
