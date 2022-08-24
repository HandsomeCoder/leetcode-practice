# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

from collections import deque


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        next_coordinates = {
            0: lambda x, y: (x-1, y),
            90: lambda x, y: (x, y+1),
            180: lambda x, y: (x+1, y),
            270: lambda x, y: (x, y-1),
        }

        def add_degree(degree, add):
            degree += add
            if degree >= 360:
                degree -= 360
            elif degree < 0:
                degree += 360
            return degree

        def explore(robot, r, c, degree, rounds, visited):
            robot.clean()
            visited.add((r, c))

            for i in range(rounds):
                if i == 0:
                    robot.turnLeft()
                    degree = add_degree(degree, -90)
                else:
                    robot.turnRight()
                    degree = add_degree(degree, 90)

                nr, nc = next_coordinates[degree](r, c)
                if (nr, nc) in visited:
                    continue

                if robot.move():
                    explore(robot, nr, nc, degree, 3, visited)
                    robot.turnLeft()
                    robot.turnLeft()

            robot.turnRight()
            robot.move()

        explore(robot, 0, 0, 0, 4, set())
