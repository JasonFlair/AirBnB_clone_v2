def do_create(self, args):
    """ Create an object of any class"""
    try:
        if not args:
            raise SyntaxError()
        arg_list = args.split(" ")
        kw = {}
        for arg in arg_list[1:]:
            keyword_split = arg.split("=")
            keyword_split[1] = eval(keyword_split[1])
            if type(keyword_split[1]) is str:
                keyword_split[1].replace("_", " ").replace('"', '\\"')
            kw[keyword_split[0]] = keyword_split[1]
    except SyntaxError:
        print("** class name missing **")
    except NameError:
        print("** class doesn't exist **")
    new_instance = HBNBCommand.classes[arg_list[0]](**kw)
    new_instance.save()
    print(new_instance.id)