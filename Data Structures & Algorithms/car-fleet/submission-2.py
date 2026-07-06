class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = []

        for p,s in zip(position, speed):
            time = (target - p) /  s
            cars.append((p,time))
            
            
        cars = sorted(cars, reverse = True)
        fleet = 0 
        last_time = 0

        for i,curr_time in cars:
            if curr_time > last_time:
                fleet += 1
                last_time = curr_time
                
        return fleet
            