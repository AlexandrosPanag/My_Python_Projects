def align_text(line,width):
    extra_spaces = width - len(line)
    sp = ' '
    if not sp in line: return line
    while extra_spaces > 0:
        line = line.replace(' ', '  ',)
        extra_spaces = width - len(line)
        sp+=' '
    return line

def formatted_print(text, width=70, align = False):
    para = text.split('\n')
    to_print = ''
    for p in para:
        words = p.split()
        line = ''
        while len(words) > 0 :
            while len(words) > 0 and len(line + words[0]) < width :
                line = ' '.join([line, words.pop(0)]).strip()
            if align and len(words) > 0:
                line = align_text(line, width)
            to_print += line + '\n'
            line = ''
    return to_print

while True:
    text = input('text:')
    if text =='':break
    width = int(input('width:'))
    print(formatted_print(text,width, True))