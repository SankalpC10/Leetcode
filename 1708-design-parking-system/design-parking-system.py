class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots_available = [0,big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.spots_available[carType] == 0:
            return False
        self.spots_available[carType] -= 1
        return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)