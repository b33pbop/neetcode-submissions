class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1. a car cannot overtake another car only catch up and match the pace
        2. car fleet: single or group of cars driving next to each other
        3. speed of car fleet is the minimum speed of any car in the fleet
        4. once a car catch up at target mile it is part of the fleet

        Before the target is reached, we can keep expanding the car fleet
        We want vehicles that start at a smaller position, but can catch up with later cars

        [(0, 1), (5, 1), (10, 2), (3, 3), (8, 4)]
        [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]

        [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
        [(10, 2), (8, 4), (5, 1), (3, 3), (2, 2)], target = 12
        time = [1, 1, 7, 4, 5]

        target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        [(7, 1), (4, 2), (1, 2), (0, 1)]
        time = [3, 3, 4, 10]

        [(8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4)] target = 10
        time = [1, 1, 1, 2, 2, 2]
        """

        cars = list(zip(position, speed))

        cars.sort(reverse=True)
        time = []

        for car in cars:
            time_step = (target - car[0]) / car[1]

            if not time or time_step > time[-1]:
                time.append(time_step)

        return len(time)
