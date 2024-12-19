name = 'Wesley dos Anjos'

colors = {
    'clear' : '\033[m',
    'blue' : '\033[34m',
    'yellow' : '\033[33m',
    'blackwhite' : '\033[7;30m'
}

print('Olá ! Muito prazer em te conhecer, {}{}{} !!!'.format('\033[4;34m', name, '\033[m'))

print('Olá ! Muito prazer em te conhecer, {}{}{} !!!'.format(colors['clear'], name, colors['clear']))
print('Olá ! Muito prazer em te conhecer, {}{}{} !!!'.format(colors['blackwhite'], name, colors['clear']))