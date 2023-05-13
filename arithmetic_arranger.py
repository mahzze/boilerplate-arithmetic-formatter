def arithmetic_arranger(problems, show_result = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    arranged_problems, top_line, down_line, dash_line = ""
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
             
    return arranged_problems

