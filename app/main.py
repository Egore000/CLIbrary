import sys

from domain.exceptions.base import ApplicationException
from router.router import router
from tools.commands import Command
from tools.messages import Message
from tools.services import greetings

sys.path.insert(0, "app/")


def main():
    greetings()

    while True:
        try:
            command = Command(input(Message.input))

            endpoint = router[command.value]
            endpoint()
        except ApplicationException as e:
            print(e.message)
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(Message.error, e)


if __name__ == "__main__":
    main()
