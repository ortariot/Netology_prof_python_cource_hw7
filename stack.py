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
        return False if not self.data else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)

    def show_stack(self):
        print(self.data)


def balncer(bkts):
    bkts_seq = Stack(bkts)
    size = bkts_seq.size()
    if size % 2 != 0:
        return 'Несбалансированно'
    mirror_bkts_seq = Stack()
    invert_bkt = {'(': ')', '{': '}', '[': '}',
                  ')': '(', '}': '{', ']': '['
                  }

    while bkts_seq.size() > size / 2:
        mirror_bkts_seq.push(invert_bkt[bkts_seq.pop()])
    while bkts_seq.isEmpty():
        if bkts_seq.pop() != mirror_bkts_seq.pop():
            return 'Несбалансированно'
    else:
        return 'Сбалансированно'


def true_balncer(bkts):
    bkts_seq = Stack()

    open_bkts = ['(', '{', '[']
    close_bkts = [')', '}', ']']

    for bkt in bkts:
        if bkt in open_bkts:
            bkts_seq.push(bkt)
        elif bkt in close_bkts:

        print(bkt)


# def simple_balancer(input):
#     invert_bkt = {'(': ')', '{': '}', '[': '}',
#                   ')': '(', '}': '{', ']': '['
#                   }
#     for num, alph in enumerate(input, 1):
#         if alph != invert_bkt[input[-num]]:
#             return 'Несбалансированно'
#         if num == len(input) / 2:
#             return 'Сбалансированно'


if __name__ == '__main__':
    # test_strings = ['{{[()]}}', '(((([{}]))))', '[([])((([[[]]])))]{()}',
    #                 '}{}', '{{[(])]}}', '[[{())}]'
    #                 ]

    # for test_str in test_strings:
    #     print(balncer(test_str))

    true_balncer('{{[()]}}')
