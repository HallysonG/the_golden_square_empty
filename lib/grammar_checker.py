def grammar_checker(string):
    if string[-1] != "." or string[-1] != "!" or string[-1] != "?":
        return "This doesn't look like it's grammatically correct!"
    elif string[0].islower():
        return "This doesn't look like it's grammatically correct!"
    else:
        return "This looks like it's grammatically correct!"