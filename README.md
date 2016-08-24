Annotated suffix tree construction using naive algorithm and normalized string to AST scoring

t = Tree(suffix)
t.add('XABXAC', 2.0)
t.add('BABXAC')
print t.score('XA', scale = 'root', norm = 'string')