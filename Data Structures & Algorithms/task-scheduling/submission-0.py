class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        q = collections.deque()
        time = 0
        for t in tasks: counts[ord(t) - ord("A")] += 1
        counts = [-1 * i for i in counts if i > 0]
        heapq.heapify(counts)

        while counts or q:
            time += 1
            if counts:
                val = heapq.heappop(counts) + 1
                if val < 0:
                    q.append([val, time + n])
                
           
            if q and q[0][1] == time:
                heapq.heappush(counts, q.popleft()[0])
        return time


        
