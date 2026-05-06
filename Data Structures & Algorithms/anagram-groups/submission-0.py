class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq list: word

        anagrams = {}
        freq = [0] * 26
        for word in strs:
            for j in range(len(word)):
                freq[ord(word[j]) - 97] += 1
            
            # convert to hashable type
            freq = tuple(freq)
            if freq in anagrams:
                anagrams[freq].append(word)
            else:
                anagrams[freq] = []
                anagrams[freq].append(word)

            freq = [0] * 26

        results = []
        for key, value in anagrams.items():
            results.append(value)

        return results
