def arithmetic_arranger(problems, true=False): 
  lsts = list()
  arranged_problems = ""
  if len(problems) > 5 :
    return "Error: Too many problems."  
  for problem in problems:
    lst = problem.split()
    if lst[1] not in ('+', '-'):
      return "Error: Operator must be '+' or '-'."
    if not (lst[0].isdigit() and lst[2].isdigit()):
      return "Error: Numbers must only contain digits."
    if len(lst[0]) > 4 or len(lst[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    tam = max(len(lst[0]), len(lst[2])) + 2
    if not lsts:
      lsts.append(lst[0].rjust(tam))
      lsts.append(lst[1] + lst[2].rjust(tam-1))
      lsts.append('-'*tam)
      if true :
        if lst[1] == '+' :
          n = int(lst[0]) + int(lst[2])
        else:
          n = int(lst[0]) - int(lst[2])
        lsts.append(str(n).rjust(tam))
    else:
      lsts[0] = lsts[0] + "    " + lst[0].rjust(tam)
      lsts[1] = lsts[1] + "    " + lst[1] + lst[2].rjust(tam-1)
      lsts[2] = lsts[2] + "    " + '-'*tam
      if true :
        if lst[1] == '+' :
          n = int(lst[0]) + int(lst[2])
        else:
          n = int(lst[0]) - int(lst[2])
        lsts[3] = lsts[3] + "    " + str(n).rjust(tam)    
  for i in range(len(lsts)-1):
    arranged_problems = arranged_problems + lsts[i] + "\n"
  arranged_problems = arranged_problems + lsts[len(lsts)-1]
  return arranged_problems