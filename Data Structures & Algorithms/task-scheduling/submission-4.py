class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A A A B C
        # n = 3
        # most common task: A x3
        # A idle idle idle A idle idle idle A
        # (1+n)*(C-1) + 1
        # 
        # A A A B C D E F G H I J K L M N
        # A B C D A E F G A H I J K L M N
        #
        # A A A B B C C D D E E F F G G
        # A B C D A B C D A E F G idle E F G
        # A B C D E F G A B C D E F G A

        # max(formula, len(input))
        # 
        # A A A B B B C C C D D D E E E
        # A B C D E A B C D E A B C D E
        #
        # X X Y Y
        # X Y 
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        max_count = 0
        num_max = 0
        for task, count in counts.items():
            max_count = max(max_count, count)

        for task, count in counts.items():
            if count == max_count:
                num_max += 1

        min_bound = (1+n)*(max_count-1) + num_max
        high_bound = len(tasks)

        return max(min_bound, high_bound)