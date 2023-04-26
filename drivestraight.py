from EncoderConstants import EncoderConstants as EC
from EncoderConstants import MotorConstants as MC

class StraightDriver:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        self.lastRecDistance = 0
        self.distanceGap = 0

    def run(self):
        if self.drivetrain.getAvgDistanceTravelled() >= EC.intendedDistance:
            print("STOPPED MOVING")
            return

        lTravel = self.drivetrain.getLEncoderDistance()
        rTravel = self.drivetrain.getREncoderDistance()
        self.distanceGap = self.drivetrain.getAvgDistanceTravelled() - self.lastRecDistance
        print(f"Left traveled:{lTravel}, Right traveled:{rTravel}, Avg traveled:{self.drivetrain.getAvgDistanceTravelled()}")
        if lTravel == rTravel:
            self.drivetrain.move(0, MC.forwardAmount)
        elif lTravel > rTravel:
            print("LGREATER")
            self.drivetrain.move(MC.invRotateAmount, MC.forwardAmount)
        elif lTravel < rTravel:
            print("RGREATER")
            self.drivetrain.move(MC.rotateAmount, MC.forwardAmount)
        self.lastRecDistance = self.drivetrain.getAvgDistanceTravelled()



