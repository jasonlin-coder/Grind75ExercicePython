from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        len_tasks = len(tasks)
        if n == 0:
            return len_tasks
        result = 0
        period = n + 1
        counter_tasks = sorted([(j) for _,j in Counter(tasks).items()], reverse=True)
        types_tasks = len(counter_tasks)
        while types_tasks > period:
            diff_task = counter_tasks[period - 1] - counter_tasks[period] + 1
            for i in range(period):
                counter_tasks[i] -= diff_task
            counter_tasks.sort(reverse=True)
            result += period * diff_task
            while counter_tasks and counter_tasks[-1] == 0:
                counter_tasks.pop()
                types_tasks -= 1
        if types_tasks == 0:
            return result
        task_in_final_period = types_tasks
        biggest_task = counter_tasks[0]
        for i in range(types_tasks - 1,0,-1):
            if counter_tasks[i] == biggest_task:
                break
            task_in_final_period -= 1
        return result + (biggest_task - 1) * period + task_in_final_period    