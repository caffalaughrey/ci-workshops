import TravisCIWorkshop


def test_hello_world_works():
    assert TravisCIWorkshop.say_hello() == "Hello world!"


def test_goodbye_world_works():
    assert TravisCIWorkshop.say_goodbye() == "Goodbye, cruel world!"
