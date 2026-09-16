from jarbin_toolkit_action import Action

def hw(a=0):
    print("Hello World!", a)

hw_a = Action("Print 'Hello World!'", hw)

print(hw_a)
hw_a()
