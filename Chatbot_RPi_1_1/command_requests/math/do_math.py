from command_requests.request_base import RequestBase
import re

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# def do_math(string):
#     operation_start_index = []
#     operation_end_index = []
#     for i in enumerate(string):
#         if i[1] in ["-", "("] or i[1] in numbers:
#             operation_start_index = i
#             # print(i)
#             break
#
#     reversed_string = "".join(reversed(string))
#     for i in enumerate(reversed_string):
#         if i[1] in [")"] or i[1] in numbers:
#             operation_end_index = [len(string)-i[0]-1 , (string[len(string)-i[0]-1])]
#             # print(operation_end_index)
#             break
#
#     new_string = string[operation_start_index[0]:operation_end_index[0]+1]
#     return(eval(new_string))

class SimpleMathRequest(RequestBase):
    def __init__(self):
        super().__init__()

    def execute(self, string=''):
        operation_start_index = []
        operation_end_index = []
        for i in enumerate(string):
            if i[1] in ["-", "("] or i[1] in numbers:
                operation_start_index = i
                # print(i)
                break

        reversed_string = "".join(reversed(string))
        for i in enumerate(reversed_string):
            if i[1] in [")"] or i[1] in numbers:
                operation_end_index = [len(string) - i[0] - 1, (string[len(string) - i[0] - 1])]
                # print(operation_end_index)
                break

        new_string = string[operation_start_index[0]:operation_end_index[0] + 1]
        return (eval(new_string))