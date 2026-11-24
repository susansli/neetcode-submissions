class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # instantiate a dict to track freqs
        # instantiate another dict to group by freqs

        freq_count = dict() # k: num, v: freq
        freq_groups = dict() # k: freq, v: set of nums

        # update freq_count
        # remove num from stale set in freq_groups
        # add num to updated set in freq_groups
        # loop through the freq_groups in reverse to construct 
        #  the array to return (this avoids sorting)

        for num in nums:
            prev_freq = 0

            if num not in freq_count:
                freq_count[num] = 1
            else:
                prev_freq = freq_count[num]
                freq_count[num] += 1

            if prev_freq > 0: # should already be in groups
                freq_groups[prev_freq].remove(num)

            if (prev_freq + 1) not in freq_groups:
                freq_groups[prev_freq + 1] = set()

            freq_groups[prev_freq + 1].add(num)
        
        top_k = list()
        
        for key, value in reversed(freq_groups.items()):
            if len(top_k) < k:
                top_k.extend(list(freq_groups[key]))
        
        return top_k







