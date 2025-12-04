import asyncio
from subprocess import Popen, DEVNULL
from .PackageManager import PackageManager
from .OutlookerRecord import OutlookerRecord
from .Engine import Engine


class OutlookerEngine(Engine):
    async def run(self):
        res = await asyncio.gather(
            self._isFlatpakInstalled(),
            self._isSnapInstalled(),
            self._figureOutPackageManager(),
            self.dummy(),
        )
        return OutlookerRecord(res[0], res[1], res[2])

    async def dummy(self):
        await asyncio.sleep(1)

    async def _isSnapInstalled(self):
        with Popen(
            "flatpak-spawn --host which snap", shell=True, stdout=DEVNULL
        ) as process:
            process.wait()
            return process.returncode == 0

    async def _isFlatpakInstalled(self):
        with Popen(
            "flatpak-spawn --host which flatpak", shell=True, stdout=DEVNULL
        ) as process:
            process.wait()
            return process.returncode == 0

    async def _figureOutPackageManager(self):
        packMng = None
        with Popen(
            "flatpak-spawn --host which apt", shell=True, stdout=DEVNULL
        ) as process:
            process.wait()
            if process.returncode == 0:
                packMng = PackageManager.APT
        with Popen(
            "flatpak-spawn --host which dnf", shell=True, stdout=DEVNULL
        ) as process:
            process.wait()
            if process.returncode == 0:
                packMng = PackageManager.RPM
        with Popen(
            "flatpak-spawn --host which pacman", shell=True, stdout=DEVNULL
        ) as process:
            process.wait()
            if process.returncode == 0:
                packMng = PackageManager.PACMAN
        return packMng
