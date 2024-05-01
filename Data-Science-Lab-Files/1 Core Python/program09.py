#9. Use lambda expression and the filter() function to filter out the words from a list that dont start with the letter 's'.
## For example: seq = ['soup','dog','salad','cat','great'] should be filtered down to ['soup','salad'].
seq = ['soup','dog','salad','cat','great']
result = list(filter(lambda word: word[0] == 's', seq))
print(result)
