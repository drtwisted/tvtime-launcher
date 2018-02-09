import os
from commands import getoutput


def _run_command(self, cmd, split=False, wait=True):
    if wait:
        res = getoutput(str(cmd))
        print("Result is:\n{}".format(res))
        if split:
            return res.split('\n')
        else:
            return res
    else:
        os.system(cmd)
        res = self._get_pid()
        return res
