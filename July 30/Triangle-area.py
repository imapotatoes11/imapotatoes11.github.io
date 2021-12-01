def checkTriangleArea(**params):
    if list(params.keys()) ==['sa' ,'sb' ,'sc']:
        s=(params['sa']+params['sb']+params['sc'])
        print(round((s*(s-params['sa'])*(s-params['sb'])*(s-params['sc']))**0.5,2))
    elif  list(params.keys()) ==['base','height']:
        print(round((params['base']*params['height'])/2,2))
    else:
        print("parameters combination not supported")


checkTriangleArea(sa=3 ,sb=4 ,sc=5)
checkTriangleArea(base=4 ,height=6)
checkTriangleArea(abc=234)