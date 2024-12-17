class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # create a max heap to store the change of pass_rate when a student is added
        pq = [(pass_stud/total_stud-(pass_stud+1)/(total_stud+1), pass_stud, total_stud) for pass_stud, total_stud in classes]
        heapq.heapify(pq)

        # for each extra student, put them into the largest change
        for x in range(extraStudents):
            _, pass_stud, total_stud = heapq.heappop(pq)
            heapq.heappush(pq, ((pass_stud+1)/(total_stud+1)-(pass_stud+2)/(total_stud+2), pass_stud+1, total_stud+1))

        avg_rate = 0
        for _, pass_stud, total_stud in pq:
            avg_rate += pass_stud/total_stud
        avg_rate /= len(pq)

        return avg_rate