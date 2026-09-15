from jarbin_toolkit_jartest import JarTest, Context


from .JT import JT_JTK
from .JT import JT_JTK_Action
from .JT import JT_JTK_Config
from .JT import JT_JTK_Console
from .JT import JT_JTK_Error
from .JT import JT_JTK_JarTest
from .JT import JT_JTK_Log
from .JT import JT_JTK_Time

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT = JarTest(
    context=Context(
        output={
            "show_context": True
        },
        env={
            "TEST_WIDE_ENV": "123"
        },
        command=[
            ("echo 'hello world!'", None)
        ]
    )
)
JTT.fetch()
JTT.update_context()
JTT.run()
