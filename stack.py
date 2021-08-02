class Stack:
    compatible_list = [list, set, str]

    def __init__(self, *args):
        self.data = self.__argsparser__(args)

    def __argsparser__(self, args):
        out = []
        if not args:
            return out
        else:
            for item in args:
                if type(item) in self.compatible_list:
                    out.extend(item)
                else:
                    out.append(item)
        return out

    def isEmpty(self):
        return True if not self.data else False

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[len(self.data) - 1] if self.data else None

    def size(self):
        return len(self.data)

    def show_stack(self):
        print(self.data)
