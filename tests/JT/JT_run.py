import os

from jarbin_toolkit_jartest import JarTest, Get, Show

import jarbin_toolkit as JTK
from jarbin_toolkit import Action
from jarbin_toolkit import Config
from jarbin_toolkit import Console
from jarbin_toolkit import Error
from jarbin_toolkit import Log
from jarbin_toolkit import Time

def JT_get_info():
    info = JTK.get_info()
    assert isinstance(info, dict), "invalid info type"
    assert "version" in info, "version is not in info"

def JT_benchmark_success():
    def sample():
        return 123

    result, elapsed, err = JTK.benchmark(sample)

    assert result == 123, "result invalid"
    assert err is None, "an error occured"
    assert elapsed >= 0, "elapsed time == 0"

def JT_benchmark_exception():
    def sample():
        raise RuntimeError("fail")

    result, elapsed, err = JTK.benchmark(sample)

    assert result is None, "not suppose to get result"
    assert isinstance(err, Exception), "err of the wrong type"

def JT_fail():
    try:
        JTK.fail("test error")
    except Exception as e:
        assert "test error" in str(e), "invalid string"

def JT_text():
    t = JTK.text("Hello", "World")
    assert hasattr(t, "bold"), "text not working properly"

def JT_action_call():
    called = {"v": False}

    def fn():
        called["v"] = True

    action = Action.Action("fn", fn)
    action()

    assert called["v"] is True, "called[v] must be True"

def JT_action_repr():
    action = Action.Action("print 'hello'", print, "hello")
    assert "Action" in repr(action), "invalid representation"

def JT_actions_container():
    result = []

    def add(x):
        result.append(x)

    actions = Action.Actions()
    actions += Action.Action("add 1", add, 1)
    actions += Action.Action("add 2", add, 2)

    assert len(actions) == 2, "invalid number of actions"

    actions()

    assert result == [1, 2], "result is not equal to expected"

def JT_actions_getitem():
    actions = Action.Actions()
    a = Action.Action("print 'A'", print, "A")
    actions += a

    assert actions[0] == a, "action not added"

TEST_PATH = "./tests/JT/"
TEST_NAME = "config_tmp"

def JT_config_set_get():
    cfg = Config(TEST_PATH, file_name=TEST_NAME, data={"App": {"x": "10"}})

    cfg.set("App", "y", 20)

    assert cfg.get("App", "x") == "10", "invalid x"
    assert cfg.get_int("App", "y") == 20, "invalid y"

def JT_config_types():
    cfg = Config(TEST_PATH, file_name=TEST_NAME, data={
        "T": {
            "i": "1",
            "f": "1.5",
            "b": "true"
        }
    })

    assert isinstance(cfg.get_int("T", "i"), int), "invalid i type"
    assert isinstance(cfg.get_float("T", "f"), float), "invalid f type"
    assert isinstance(cfg.get_bool("T", "b"), bool), "invalid b type"

def JT_config_delete():
    cfg = Config(TEST_PATH, file_name=TEST_NAME)
    cfg.delete()

    assert not os.path.exists(TEST_PATH + "/config.ini"), "config file not deleted"

def JT_console_print():
    output, _ = Get.Redirect.stdout(Console.Console.print, "Hello", auto_reset=False, end="")
    assert output == "Hello", "output is not valid"

def JT_text_formatting():
    Text = Console.Text.Text

    t = Text("hello")

    assert isinstance(t.bold(), Text), "apply not returning type according to argument type"
    assert isinstance(t.underline().s, str), "proprety 'str' not working"

def JT_progress_bar():
    pb = Console.Animation.ProgressBar(10)

    pb.update(5)
    output = pb.render()

    assert isinstance(output, Console.Text.Text), "output is of the wrong type"

def JT_cursor():
    Console.ANSI.Cursor.up(1)
    Console.ANSI.Cursor.down(1)
    Console.ANSI.Cursor.left(1)
    Console.ANSI.Cursor.right(1)

    assert True

def JT_line():
    Console.ANSI.Line.clear_line()
    Console.ANSI.Line.clear()

    assert True

def JT_error_base():
    e = Error.Error.ErrorRuntime("msg")
    assert "msg" in str(e), "message not an Exception"

def JT_error_with_link():
    e = Error.Error.ErrorRuntime("msg", link=("file.py", 10))
    assert "file.py" in str(e), "file not shown"

def JT_error_types():
    e = Error.Special.ErrorSpecialConfig("config error")
    assert isinstance(e, Exception), "e not an Exception"

TEST_PATH = "./tests/JT/"
TEST_NAME = "test_logs"

def JT_log_write():
    log = Log(TEST_PATH, TEST_NAME)

    log.log("INFO", "title", "message")
    log.comment("comment")

    log.close()

    assert os.path.exists(TEST_PATH + TEST_NAME + ".jar-log"), "failed to create log"

    log.delete()

    assert not os.path.exists(TEST_PATH + TEST_NAME + ".jar-log"), "failed to delete log"

def JT_log_filter():
    log = Log(TEST_PATH, TEST_NAME)

    log.log("INFO", "t1", "m1")
    log.log("ERROR", "t2", "m2")

    log.close()

    result = log.str_filtered("ERROR")

    assert "m2" in result and not "m1" in result, "failed to filter log"

    log.close()
    log.delete()

def JT_stopwatch_basic():
    sw = Time.StopWatch(True)
    Time.Time.wait(0.2)
    sw.stop()

    assert sw.elapsed() >= 0.2, "invalid elapsed time"

def JT_stopwatch_reset():
    sw = Time.StopWatch(True)
    sw.reset()
    assert sw.elapsed() >= 0, "invalid elapsed time"

def JT_wait():
    elapsed = Time.Time.wait(0.1)
    assert elapsed >= 0.1, "invalid elapsed time"


JTT = JarTest()
JTT.fetch()
JTT.run()
