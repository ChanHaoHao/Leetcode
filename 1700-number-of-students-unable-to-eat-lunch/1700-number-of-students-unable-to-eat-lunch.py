class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # turning the students into deque to use popleft
        deque_students = deque()
        [deque_students.append(i) for i in students]

        while sandwiches:
            # check if there are still students that can accept the sandwich at the top (the first sandwich)
            # weird thing that the stack pops 0 instead of -1
            if (sandwiches[0]==1 and sum(deque_students)==0) or (sandwiches[0]==0 and sum(deque_students)==len(deque_students)):
                return len(deque_students)

            current_sandwich = sandwiches.pop(0)
            current_student = deque_students.popleft()
            # get till the student accepts the sandwich
            while current_sandwich!=current_student:
                deque_students.append(current_student)
                current_student = deque_students.popleft()

        return 0
            