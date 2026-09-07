from jarbin_toolkit_jartest import JarTest, Context


from tests.JT import JT_JTK
from tests.JT import JT_JTK_Action
from tests.JT import JT_JTK_Config
from tests.JT import JT_JTK_Console
from tests.JT import JT_JTK_Error
from tests.JT import JT_JTK_JarTest
from tests.JT import JT_JTK_Log
from tests.JT import JT_JTK_Time

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
        command=["echo 'hello world!'"]
    )
)
JTT.fetch()
JTT.run()
