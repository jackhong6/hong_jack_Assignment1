# CTA200H 2017 Problem Set 1, Question 6
# Jack Hong and Bill Kong

import numpy as np


class Spaceship():
    """Class representing a standard spaceship."""

    def __init__(self, name, laser=100., shield=100., hull=100., type='Spaceship'):
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull = hull
        self.type = type

    def shoot(self, target):
        """Shoot at another spaceship."""
        return target.hit(self.laser)

    def hit(self, laser):
        """Ship is hit by a laser. Return True if destroyed."""
        if self.shield > 0:
            self.shield = max(0, self.shield - laser)
        else:
            self.hull = max(0, self.hull - laser / 2)
            if self.hull == 0:
                return True

        return False


class Warship(Spaceship):
    """Class representing a warship."""

    def __init__(self, name, laser=100., missile=100., shield=100., hull=100., type='Warship'):
        Spaceship.__init__(self, name, laser, shield, hull, type)
        self.missile = missile

    def shoot(self, target):
        """Shoot at another spaceship."""
        if np.random.random() < 0.3:
            target.hit(self.missile)

        return target.hit(self.laser)


class Speeder(Spaceship):
    """Class representing a speeder."""

    def __init__(self, name, laser=100., shield=100., hull=100., type='Speeder'):
        Spaceship.__init__(self, name, laser, shield, hull, type)

    def hit(self, laser):
        if np.random.random() > 0:
            return Spaceship.hit(self, laser)
        else:
            return False


def main():
    s1 = Spaceship("USS UNDERPANTS")
    s2 = Spaceship("UNSC PILLAR OF AUTUMN")
    s3 = Spaceship("NORMANDY")
    w = Warship("BELLICOSE")
    s = Speeder("SPEEDY MCSPEEDY FACE")

    ships = [s1, s2, s3, w, s]

    for ship in ships:
        print("{:s} has entered the battle. ({:s})".format(ship.name, ship.type))

    print("\n=================================\n")

    while len(ships) > 1:
        for ship in ships:

            x = np.random.randint(0, len(ships))
            while ships[x] is ship:
                x = np.random.randint(0, len(ships))

            print("{:s} shot at {:s}".format(ship.name, ships[x].name))

            target_destroyed = ship.shoot(ships[x])
            if target_destroyed:
                print("{:s} has been destroyed!!!\n".format(ships[x].name))
                ships.remove(ships[x])

        if len(ships) == 1:
            print("\nAnd the winner is {:s}! ({:s})".format(ships[0].name, ships[0].type))


if __name__ == "__main__":
    main()
