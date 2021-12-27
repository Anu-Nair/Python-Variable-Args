def var_args(name, *args):  # example for variable arguments
    print(name, args)


def keyword_args(name, **args):  # Keyword arguments
    print(args["description"], args["feedback"])


var_args("mark", 15, None, "Hi")
keyword_args("Mark", description="loves Python", feedback=None, subscriber=True)