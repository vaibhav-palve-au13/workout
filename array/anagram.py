def sol(S):
    map={}
    for i in S:
        word = "".join(sorted(i))
        if word not in map:
            map[word]=[i]
        else:
            map[word].append(i)
    list=[]
    for i in map.values():
        list.append(i)
    return list
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol(strs))
     