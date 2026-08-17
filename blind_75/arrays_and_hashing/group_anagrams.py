def groupAnagrams(strs):
    group_dict = {}
    for str in strs:
        sorted_str = "".join(sorted(str))

        if sorted_str in group_dict:
            group_dict[sorted_str].append(str)

        else:
            group_dict[sorted_str] = [str]

    flatten_list = []
    for key, val in group_dict.items():
        flatten_list.append(val)

    return flatten_list

strs = ["act","pots","tops","cat","stop","hat"]

result = groupAnagrams(strs)
print(result)