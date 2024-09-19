class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def getStart(list_in):
            return list_in[0]

        sorted_intervals = sorted(intervals, key=getStart)
        print(sorted_intervals)

        final_intervals = [sorted_intervals[0]]

        for elt in sorted_intervals[1:]:
            final_int = final_intervals[-1]
            if getStart(elt) <= final_int[1]:
                final_int[1] = max(elt[1], final_int[1])
            else:
                final_intervals.append(elt)
        return final_intervals