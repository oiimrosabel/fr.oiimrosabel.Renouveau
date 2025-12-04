from gi.repository import Gtk

from .FlatpakRecord import FlatpakRecord
from .Terminal import Terminal
from .FlatpakCommands import FlatpakCommands
from .Engine import Engine
from subprocess import Popen, PIPE, CalledProcessError
from .CommandType import UpdateCommandType, ExtendedCommandType
from .TerminalStyle import TerminalStyle
from .UpdateExpanderRow import UpdateExpanderRow
from .UpdateRow import UpdateRow
from .UpdateState import UpdateState
                   


class FlatpakEngine(Engine):
    _terminal: Terminal
    _record: FlatpakRecord
    _children: list[UpdateRow]
    _states: list[bool]
    _row: UpdateExpanderRow
    _commands = FlatpakCommands()

    def __init__(self, record: FlatpakRecord, terminal: Terminal, row: UpdateExpanderRow):
        self._terminal = terminal
        self._record = record
        self._row = row
        
        self._states = [x for x in record.__dict__.values()][1:]
        box = row.get_child().get_last_child()
        print(type(box), box.__dict__)
        self._children = [box.get_first_row() for x in range(len(self._states))]
        print(self._children)

    async def run(self):
        self._row.setState(UpdateState.ONGOING)
        self._terminal.write(
            ">>> Starting Flatpak's update >>>", style=TerminalStyle.INF, separate=True
        )
        if self._record.flatpakEnabled:
            await self._runCommand(self._commands.getCommand(UpdateCommandType.REG))
        if self._record.cleanUnused:
            await self._runCommand(self._commands.getCommand(ExtendedCommandType.AUTO))
        if self._record.cleanOrphan:
            await self._runCommand(
                self._commands.getCommand(ExtendedCommandType.ORPHAN)
            )
        self._terminal.write(
            "<<< Finishing Flatpak's update <<<", TerminalStyle.INF, separate=True
        )

    async def _runCommand(self, cmd):
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
                self._terminal.write(line)
            process.wait()
            if process.returncode != 0:
                raise CalledProcessError(process.returncode, cmd)
                
    def _initRows(self):
        pass
