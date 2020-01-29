from enum import Enum, auto
import time


class States(Enum):
    INACTIVE = auto()
    ACTIVE = auto()
    PAUSE = auto()
    EXIT = auto()


class Game:
    def __init__(self):
        self._state = States.INACTIVE

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state


system = Game()
system.set_state(States.INACTIVE)

while True:

    if system.get_state() == States.INACTIVE:
        print("INACTIVE MODE")
        val = int(input("Press (2) to begin command or (4) to Exit command: "))
        time.sleep(1)
        print('-' * 30 + '**Transition State**' + '-' * 30)
        time.sleep(1)
        if val == 2:
            print("Active State")
            system.set_state(States.ACTIVE)
        elif val == 4:
            print("Exited from command")
            system.set_state(States.EXIT)
            break

    if system.get_state() == States.ACTIVE:

        print("In ACTIVE STATE")
        val = int(input("Press (3) to Pause Command or (1) to Inactive: "))
        time.sleep(1)
        print('-' * 30 + '**Transition State**' + '-' * 30)
        time.sleep(1)
        if val == 3:
            print("system is Paused.")
            system.set_state(States.PAUSE)
        elif val == 1:
            print("Deactivatng system")
            system.set_state(States.INACTIVE)

    if system.get_state() == States.PAUSE:
        print("Paused the State")
        val = int(input("Press (2) to Active or (1) to Inactive "))
        time.sleep(1)
        print('-' * 30 + '**Transition State**' + '-' * 30)
        time.sleep(1)
        if val == 1:
            system.set_state(States.INACTIVE)
        elif val == 2:
            system.set_state(States.ACTIVE)
