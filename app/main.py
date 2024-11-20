from domain.exceptions.base import ApplicationException
from tools.commands import Command
from tools.services import greetings
from router.router import router


def main():
    greetings()

    while True:
        try:
            command = Command(input(">> "))

            endpoint = router[command.value]
            endpoint()        
        except ApplicationException as e:
            print(e.message)


if __name__=='__main__':
    main()