from stack import Stack


def balncer(bkts):
    bkts_seq = Stack()

    bkt_dict = {')': '(',
                '}': '{',
                ']': '['
                }

    for bkt in bkts:
        if bkt in bkt_dict.values():
            bkts_seq.push(bkt)
        elif bkt in bkt_dict.keys():
            if bkt_dict[bkt] == bkts_seq.peek():
                bkts_seq.pop()
            else:
                bkts_seq.push(None)
                break
    return 'Сбалансированно' if bkts_seq.isEmpty() else 'Несбалансированно'


if __name__ == '__main__':
    test_strings = ['{{[()]}}', '(((([{}]))))', '[([])((([[[]]])))]{()}',
                    '}{}', '{{[(])]}}', '[[{())}]', '{{{{{{{', '}}}}}}}}',
                    '(){}[]'
                    ]

    for test_str in test_strings:
        print(balncer(test_str))
