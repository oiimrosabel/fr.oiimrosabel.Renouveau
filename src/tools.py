import asyncio
from subprocess import Popen, PIPE

from .enums import PackageManager, TerminalStyle
from .records import OutlookerRecord

from .Terminal import Terminal


class Prompter:
    _terminal: Terminal | None

    def __init__(self):
        self._terminal = None

    def linkTerminal(self, terminal: Terminal | None):
        self._terminal = terminal

    def _writeInTerminal(self, *args, **kwargs):
        if self._terminal is not None:
            self._terminal.write(*args, **kwargs)

    async def run(self, cmd: str):
        cmd = f"flatpak-spawn --host {cmd}"
        self._writeInTerminal(f"$ {cmd}", style=TerminalStyle.COM, separate=True)
        with Popen(
            cmd,
            shell=True,
            bufsize=1,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
        ) as process:
            for line in process.stdout:
                self._writeInTerminal(line)
            for line in process.stderr:
                self._writeInTerminal(line, style=TerminalStyle.ERR)
            process.wait()
            return process.returncode


class Outlooker:
    _prompter = Prompter()

    async def outlook(self):
        res = await asyncio.gather(
            self._isFlatpakInstalled(),
            self._isSnapInstalled(),
            self._figureOutPackageManager(),
            self.dummy(),
        )
        return OutlookerRecord(res[0], res[1], res[2])

    async def dummy(self):
        await asyncio.sleep(1)

    async def _isFlatpakInstalled(self):
        return await self._prompter.run("which flatpak") == 0

    async def _isSnapInstalled(self):
        return await self._prompter.run("which snap") == 0

    async def _figureOutPackageManager(self):
        if await self._prompter.run("which apt") == 0:
            return PackageManager.APT
        if await self._prompter.run("which dnf") == 0:
            return PackageManager.RPM
        if await self._prompter.run("which pacman") == 0:
            return PackageManager.PACMAN
        return None

