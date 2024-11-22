from unittest import TestCase

from tools.commands import AllowedCommands, Command


class TestCommand(TestCase):

    def test_create_command(self):
        for command in AllowedCommands:
            with self.subTest(f"Команда {command.name}"):
                cmd = Command(command.value)

                self.assertEqual(cmd.value, command.value)
