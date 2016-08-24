from math import log,exp
def constant(x):
    return 1.0
def linear(x):
    return float(x)
def root(x):
    return x**0.5
def square(x):
    return x*x
def logit(x):
    try:
        return log(x)-log(1-x)
    except:
        return .0
def sigmoid(x):
    return 1.0/(1.0+exp(-x))
def mylog(x):
    return log(x)
phi = {'constant':constant,
       'linear':linear,
       'square':square,
       'root':root,
       'log':mylog,
       'logit':logit,
       'sigmoid':sigmoid}
    
