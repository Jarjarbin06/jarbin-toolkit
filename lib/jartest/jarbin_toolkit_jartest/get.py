#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
###    ----get.py----     ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import subprocess
import io
from contextlib import redirect_stdout as _redirect_stdout, redirect_stderr as _redirect_stderr
from typing import Any, Mapping
from httpx import request as _request, Response


class Get:

    class Redirect:

        @staticmethod
        def _redirect(
                func,
                *args,
                **kwargs
            ) -> tuple[str, str, Any]:
            out_buffer = io.StringIO()
            err_buffer = io.StringIO()
            with _redirect_stdout(out_buffer), _redirect_stderr(err_buffer):
                ret = func(*args, **kwargs)
            return out_buffer.getvalue(), err_buffer.getvalue(), ret

        @staticmethod
        def all_std(
                func,
                *args,
                **kwargs
            ) -> tuple[str, str, Any]:
            out, err, ret = Get.Redirect._redirect(func, *args, **kwargs)
            return out, err, ret

        @staticmethod
        def stdout(
                func,
                *args,
                **kwargs
            ) -> tuple[str, Any]:
            out, _, ret = Get.Redirect._redirect(func, *args, **kwargs)
            return out, ret

        @staticmethod
        def stderr(
                func,
                *args,
                **kwargs
            ) -> tuple[str, Any]:
            _, err, ret = Get.Redirect._redirect(func, *args, **kwargs)
            return err, ret

        @staticmethod
        def _run_cmd(
                args: list[str]
            ) -> tuple[str, str, int]:
            proc = subprocess.run(
                args,
                capture_output=True,
                text=True
            )
            return proc.stdout, proc.stderr, proc.returncode

        @staticmethod
        def cmd_all_std(
                *args: str
            ) -> tuple[str, str, int]:
            out, err, code = Get.Redirect._run_cmd(list(args))
            return out, err, code

        @staticmethod
        def cmd_stdout(
                *args: str
            ) -> tuple[str, int]:
            out, _, code = Get.Redirect._run_cmd(list(args))
            return out, code

        @staticmethod
        def cmd_stderr(
                *args: str
            ) -> tuple[str, int]:
            _, err, code = Get.Redirect._run_cmd(list(args))
            return err, code

    class HTTP:

        @staticmethod
        def request(
                method: str,
                url: str,
                *,
                params: Any = None,
                content: Any = None,
                data: Any = None,
                files: Any = None,
                json: Any = None,
                headers: Any = None,
                cookies: Any = None,
                auth: Any = None,
                proxy: Any = None,
                timeout: float = 5.0,
                follow_redirects: bool = False,
                verify: bool = True,
                trust_env: bool = True
            ) -> Response:
            return _request(
        method,
            url,
                params=params,
                content=content,
                data=data,
                files=files,
                json=json,
                headers=headers,
                cookies=cookies,
                auth=auth,
                proxy=proxy,
                timeout=timeout,
                follow_redirects=follow_redirects,
                verify=verify,
                trust_env=trust_env
            )

        @staticmethod
        def get(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("GET", url, **kwargs)

        @staticmethod
        def post(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("POST", url, **kwargs)

        @staticmethod
        def put(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("PUT", url, **kwargs)

        @staticmethod
        def patch(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("PATCH", url, **kwargs)

        @staticmethod
        def delete(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("DELETE", url, **kwargs)

        @staticmethod
        def head(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("HEAD", url, **kwargs)

        @staticmethod
        def options(
                url: str,
                **kwargs
            ) -> Response:
            return Get.HTTP.request("OPTIONS", url, **kwargs)
