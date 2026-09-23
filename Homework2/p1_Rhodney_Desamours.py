def line_number(file1: str, file2: str) -> None:
    f_lines = []
    
    with open(file1) as f:
        for line in f:
            f_lines.append(line)
    
    with open(file2, 'w') as g:
        for i in range(len(f_lines)):
            g.write(f'{i + 1}. {f_lines[i]}')

def parse_functions(filename: str):
    # tuple elements: line number, function name, formal argument as string,
    # function code as string
    fin_tup = []
    numbered_file = f"{filename}.txt"
    
    line_number(filename, numbered_file)
    
    fun_line = 0
    fun_name = ''
    fun_arg = ''
    fun_code = ''
    
    with open(numbered_file) as f:
        lines = f.read().splitlines()
        
        for line in lines:
            if 'def' in line:
                fun_line = line[:line.find('.')]
                fun_name = line[line.find('def ') + 4:line.find('(')]
                fun_arg = line[line.find('(') + 1:line.find(')')]
                
                fun_code = line[line.find('def'):] + '\n'
                
                for li in lines[lines.index(line):]:
                    if li[li.find('.') + 1:li.find('.') + 4] == '    ':
                        fun_code += li[li.find('.' + 1):].strip() + '\n'
                    else:
                        break
                
                fin_tup.append((fun_line, fun_name, fun_arg, fun_code))
    
    return tuple(fin_tup)

def main():
    print(parse_functions('fun.py'))
         
if __name__ == '__main__':
    main()