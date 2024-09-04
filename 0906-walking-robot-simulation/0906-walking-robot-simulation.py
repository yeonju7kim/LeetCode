class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        maximum_answer = 0
        current_position = [0,0]
        obstacles_dictionary = defaultdict(lambda: defaultdict(int))
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        direction_index = 0
        for obstacle in obstacles:
            obstacles_dictionary[obstacle[0]][obstacle[1]] = 1
        for c in commands:
            if c == -2:
                direction_index = (direction_index + 3) % 4
            elif c == -1:
                direction_index = (direction_index + 1) % 4
            else:
                pass_flag = False
                if direction[direction_index][0] == 0:
                    increment = 1 if direction[direction_index][1] > 0 else -1
                    for i in range(increment, c * direction[direction_index][1] + increment, increment):
                        if obstacles_dictionary[current_position[0]][current_position[1] + i] == 1:
                            current_position[1] = current_position[1] + i + 1 if direction[direction_index][1] < 0 else current_position[1] + i - 1
                            pass_flag = True
                            break
                    if not pass_flag:
                        current_position[1] = current_position[1] + c * direction[direction_index][1]
                else:
                    increment = 1 if direction[direction_index][0] > 0 else -1
                    for i in range(increment, c * direction[direction_index][0] + increment, increment):
                        if obstacles_dictionary[current_position[0] + i][current_position[1]] == 1:
                            current_position[0] = current_position[0] + i + 1 if direction[direction_index][0] < 0 else current_position[0] + i - 1
                            pass_flag = True
                            break
                    if not pass_flag:
                        current_position[0] = current_position[0] + c * direction[direction_index][0]
            maximum_answer = max(maximum_answer, pow(current_position[0], 2) + pow(current_position[1], 2))
                        
        return maximum_answer