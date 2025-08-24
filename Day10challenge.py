from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        # Sort characters to create a key
        key = "".join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
