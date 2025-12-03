from time import perf_counter_ns

class Timer():
    def __init__(self):
        self.time_starts = {}
        self.time_ends = {}

    def start_timing(self, name: str) -> None:
        self.time_starts[name] = perf_counter_ns()
    
    def end_timing(self, name: str) -> None:
        self.time_ends[name] = perf_counter_ns()

    def print_times(self):
        deltas = {}
        unfinished = []
        for name in self.time_starts.keys():
            start_time = self.time_starts[name]
            if name in self.time_ends.keys():
                deltas[name] = self.time_ends[name] - start_time
            else:
                unfinished.append(name)
        
        max_length_name = 10
        max_length_time_s = 15

        print_values = []

        first_start = min([self.time_starts[name] for name in self.time_starts.keys()])
        last_finish = max([self.time_ends[name] for name in self.time_ends.keys()])

        total_time = last_finish - first_start
        total_time_s = str(total_time/1000000000)
        total_time_ms = str(total_time/1000000)

        max_length_time_s = max(max_length_time_s, len(total_time_s))

        for name in deltas.keys():
            print_values.append((name, str(deltas[name]/1000000000), str(deltas[name]/1000000)))

            max_length_name = max(max_length_name, len(print_values[-1][0]))
            max_length_time_s = max(max_length_time_s, len(print_values[-1][1]))

        print_values.append(("Total Time", total_time_s, total_time_ms))

        print(f"\nName {' '*(max_length_name - 4)}| Time Elapsed (s) {' '*(max_length_time_s - 15)}| Time Elapsed (ms)")
        for name, time_s, time_ms in print_values:
            print(f"{name} {' '*(max_length_name - len(name))}| {time_s}s {' '*(max_length_time_s - len(time_s))}| {time_ms}ms")

        if unfinished:
            print("\nUnfinished:")
            for name in unfinished:
                print(name)
        print("")