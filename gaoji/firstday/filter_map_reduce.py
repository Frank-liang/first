l = ['Adv','qwe','Erv','wewrr']
l1 = filter(lambda x: True if x[0].islower() else False, l)
l2 = map(lambda x : len(x),l1)
result = reduce(lambda x,y: x+y,l2)
