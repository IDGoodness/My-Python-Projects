def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
      return "Error: Too many problems."
  
  for pro in problems:
    #print('happy', pro)
    x = pro.split(" ")[0]
    y = pro.split(" ")[2]
    op = pro.split(" ")[1]
    first, second, third , last = '','','',''
    
    try:
      int(x)
      int(y)
    except:
      return "Error: Numbers must only contain digits."

    sume = ' '
    if (op == '+' or op == '-'):           
      if (op == '+'):
        sume = str(int(x) + int(y))
      else:
        sume = str(int(x) - int(y))
    else:
      return "Error: Operator must be '+' or '-'."
    if (len(x)>= 5 or len(y)>=5):
      return "Error: Numbers cannot be more than four digits."
        
      #print('dae', sume)
        
    mr = max(len(x), len(y)) + 2
    first += x.rjust(mr) + "    "
    second += op.ljust(1) + y.rjust(mr - 1) + "    "
    third += "-" * mr + "    "
    last += sume.rjust(mr) + "    "

    if solve:
      arranged_problems = first[:-4] + "\n" + second[:-4] + "\n" + third[:-4] + "\n" + last[:-4]
    else:
      arranged_problems = first[:-4] + "\n" + second[:-4] + "\n" + third[:-4]
    return(arranged_problems)
        

        
        
        


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print("d")
