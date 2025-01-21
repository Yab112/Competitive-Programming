class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        last_timestamp = 0
        time_tracker = [0] * len(logs)
        stack = []

        for log in logs:
            log_id,action,timestamp = log.split(":")
            log_id,timestamp = int(log_id),int(timestamp)

            if action == "start":  
                if stack:  
                    time_tracker[stack[-1]] += timestamp - last_timestamp  
                stack.append(log_id)  
                last_timestamp = timestamp  
            else:  
                time_tracker[stack.pop()] += timestamp - last_timestamp + 1  
                last_timestamp = timestamp + 1
        return [i for i in time_tracker if i != 0]
