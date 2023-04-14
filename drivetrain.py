import wpilib as wp
from wpilib import Spark, Encoder
import wpilib.drive as drive

class Drivetrain:
    def __init__(self):
        self.lMotor = Spark(0)
        self.rMotor = Spark(1)
        self.lEncoder = Encoder(4, 5)
        self.rEncoder = Encoder(6, 7)
        self.drivetrain = drive.DifferentialDrive(self.lMotor, self.rMotor)

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(rotate, forward)

    def getLEncoderDistance(self):
        return self.lEncoder.getDistance()

    def getREncoderDistance(self):
        return self.rEncoder.getDistance()

    def zeroEncoders(self):
        self.lEncoder.reset()
        self.rEncoder.reset()


