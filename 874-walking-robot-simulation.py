class Solution:
    def robotSim(self, commands, obstacles):
        loc = [0, 0]
        direction_list = ["forward", "right", "backward", "left"]
        direction_index = 0
        largest = 0
        obs_set = set()
        for obs in obstacles:
            obs_set.add(tuple(obs))
        for command in commands:
            # direction handling
            if command < 0:
                if command == -2:
                    direction_index -= 1
                elif command == -1:
                    direction_index += 1

                if direction_index < 0:
                    direction_index += 4
                elif direction_index >= 4:
                    direction_index -= 4
            else:
                direction = direction_list[direction_index]
                for _ in range(command):
                    # move along the direction
                    target_loc = loc[:]
                    if direction == "forward":
                        target_loc[1] += 1
                    elif direction == "right":
                        target_loc[0] += 1
                    elif direction == "backward":
                        target_loc[1] -= 1
                    elif direction == "left":
                        target_loc[0] -= 1
                    
                    if tuple(target_loc) not in obs_set:
                        loc = target_loc[:]
                    
            # calculate distance
            cur_dist = loc[0] ** 2 + loc[1] ** 2
            if cur_dist > largest:
                largest = cur_dist
        return largest

s = Solution()
s.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])