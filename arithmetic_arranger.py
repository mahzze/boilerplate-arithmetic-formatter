def arithmetic_arranger(problems, show_result = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    arranged_problems = "" 
    top_line = "" 
    down_line = "" 
    dash_line = ""

    for problem in problems:
        inputs = problem.split()

        # error checking 
        if len(inputs[0]) > 4 or len(inputs[2]) > 4: 
            return 'Error: Numbers cannot be more than four digits.'

        if inputs[1] != "-" and inputs[1] != "+":
            return "Error: Operator must be '+' or '-'."
        
        try:
            inputs[0] = int(inputs[0])
            inputs[2] = int(inputs[2])
        except:
            return 'Error: Numbers must only contain digits.' 
        
        
    for i in range(0, len(problems)):
        arranged_problems = arranged_problems+problems[i]+"\n"
        val1, operator, val2 = problems[i].split()
        len_diff = len(str(val1)) - len(str(val2))
        if len_diff < 0:
            len_diff = len_diff * -1
            top_line = top_line + space_filler(len_diff + 2) + val1 
            down_line = down_line + operator + " " + val2 
            dash_line = space_filler(len(str(val2)) + 2, "-")
        else:
            top_line = top_line + "  " + val1
            down_line = down_line + operator + " " + space_filler(len_diff) + val2 
            dash_line = space_filler(len(str(val1)) + 2, "-")

        if i+1 < len(problems):
            top_line  = top_line  + "    "
            down_line = down_line + "    "
            dash_line = dash_line + "    "
    arranged_problems = "\n".join([top_line, down_line, dash_line])

    return arranged_problems

def space_filler(number, char = " "):
    filling = ""
    idx = 0
    while idx < number:
        filling = filling + char
        idx = idx + 1
    return filling 

print(arithmetic_arranger(["3 - 100" ], False))
