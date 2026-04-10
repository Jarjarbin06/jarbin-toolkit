#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
###    ----get.py----     ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import sys
import io
from contextlib import redirect_stdout as _redirect_stdout, redirect_stderr as _redirect_stderr


class Get:

    @staticmethod
    def _redirect(func, *args, **kwargs):

        out_buffer = io.StringIO()
        err_buffer = io.StringIO()

        with _redirect_stdout(out_buffer), _redirect_stderr(err_buffer):
            func(*args, **kwargs)

        return out_buffer.getvalue(), err_buffer.getvalue()

    @staticmethod
    def redirect_stdout_stderr(func, *args, **kwargs) -> str:
        out, err = Get._redirect(func, *args, **kwargs)
        return out + err

    @staticmethod
    def redirect_stdout(func, *args, **kwargs) -> str:
        out, _ = Get._redirect(func, *args, **kwargs)
        return out

    @staticmethod
    def redirect_stderr(func, *args, **kwargs) -> str:
        _, err = Get._redirect(func, *args, **kwargs)
        return err
