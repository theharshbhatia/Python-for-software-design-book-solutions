def eval_loop(s):
    print(eval(s))

while True:
    line = input('type "done" to exit')
    
    if  line == 'done':
        break
    
    else:
        eval_loop(line)
