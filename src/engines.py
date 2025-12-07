from abc import ABC, abstractmethod
from subprocess import Popen, PIPE, CalledProcessError
from gi.repository import GObject

from .Terminal import Terminal
from .UpdateExpanderRow import UpdateExpanderRow

from .records import FlatpakRecord, SnapRecord
from .commands import CommandRepository, FlatpakCommands, SnapCommands
from .enums import TerminalStyle, UpdateState


class Engine(ABC):
    _terminal: Terminal
    _record: GObject.Object
    _choices: list[tuple]
    _row: UpdateExpanderRow
    _commands: CommandRepository

    @abstractmethod
    def run(self):
        pass

    async def runCommand(self, cmd):
        cmd = f"flatpak-spawn --host {cmd}"
        self._terminal.write(f"$ {cmd}", style=TerminalStyle.COM, separate=True)
        with Popen(
            cmd,
            shell=True,
            bufsize=1,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
        ) as process:
            for line in process.stdout:
                self._terminal.write(line)
            for line in process.stderr:
                self._terminal.write(line, style=TerminalStyle.ERR)
            process.wait()
            if process.returncode != 0:
                raise CalledProcessError(process.returncode, cmd)


class FlatpakEngine(Engine):
    _terminal: Terminal
    _record: FlatpakRecord
    _choices: list[tuple]
    _row: UpdateExpanderRow
    _commands = FlatpakCommands()

    def __init__(
        self, record: FlatpakRecord, terminal: Terminal, row: UpdateExpanderRow
    ):
        self._terminal = terminal
        self._record = record
        self._row = row

        cmds = self._commands.availableCommands()
        print(cmds)
        states = [x for x in record.__dict__.values()][1:]
        children = row.getRows()
        self._choices = [(states[x], cmds[x], children[x]) for x in range(len(cmds))]
        self._initRows()

    async def run(self):
        self._row.setState(UpdateState.ONGOING)
        self._terminal.write(
            ">>> Starting Flatpak's update >>>", style=TerminalStyle.INF, separate=True
        )
        for e in self._choices:
            if e[0]:
                e[2].setState(UpdateState.ONGOING)
                try:
                    await self.runCommand(self._commands.getCommand(e[1]))
                    e[2].setState(UpdateState.SUCCESS)
                except CalledProcessError as e:
                    e[2].setState(UpdateState.FAIL)
                    self._row.setState(UpdateState.FAIL)
                    raise e
        self._terminal.write(
            "<<< Finishing Flatpak's update <<<", TerminalStyle.INF, separate=True
        )
        self._row.setState(UpdateState.SUCCESS)

    def _initRows(self):
        for e in self._choices:
            e[2].setState(UpdateState.SCHEDULED if e[0] else UpdateState.HIDDEN)


class SnapEngine(Engine):
    _terminal: Terminal
    _record: SnapRecord
    _choices: list[tuple]
    _row: UpdateExpanderRow
    _commands = SnapCommands()

    # TODO

    def __init__(self, record: SnapRecord, terminal: Terminal, row: UpdateExpanderRow):
        self._terminal = terminal
        self._record = record
        self._row = row

        cmds = self._commands.availableCommands()
        print(cmds)
        states = [x for x in record.__dict__.values()][1:]
        children = row.getRows()
        self._choices = [(states[x], cmds[x], children[x]) for x in range(len(cmds))]
        self._initRows()

    async def run(self):
        self._row.setState(UpdateState.ONGOING)
        self._terminal.write(
            ">>> Starting Snap's update >>>", style=TerminalStyle.INF, separate=True
        )
        for e in self._choices:
            if e[0]:
                e[2].setState(UpdateState.ONGOING)
                try:
                    await self.runCommand(self._commands.getCommand(e[1]))
                    e[2].setState(UpdateState.SUCCESS)
                except CalledProcessError as e:
                    e[2].setState(UpdateState.FAIL)
                    self._row.setState(UpdateState.FAIL)
                    raise e
        self._terminal.write(
            "<<< Finishing Snap's update <<<", TerminalStyle.INF, separate=True
        )
        self._row.setState(UpdateState.SUCCESS)

    def _initRows(self):
        for e in self._choices:
            e[2].setState(UpdateState.SCHEDULED if e[0] else UpdateState.HIDDEN)

