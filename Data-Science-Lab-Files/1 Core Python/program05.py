#5. Given the nested dictionary grab the word "hello". d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
def find_hello(d):
    target_word = d['k1'][3]['tricky'][3]['target'][3]
    return target_word

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
result = find_hello(d)
print(result)
