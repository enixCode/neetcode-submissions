class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda fleet: fleet[0], reverse=True)
        new_fleets = [fleets[0]]
        # print(fleets, fleets[1:])
        for i, fleet in enumerate(fleets[1:]):
            prev_time = (target - new_fleets[-1][0])/new_fleets[-1][1]
            time = (target - fleet[0])/fleet[1]
            # print(new_fleets[-1])
            # print(fleet)
            if prev_time >= time:
                # print("merge")
                pass
            else:
                new_fleets.append(fleet)
                # print("add")
        return len(new_fleets)
