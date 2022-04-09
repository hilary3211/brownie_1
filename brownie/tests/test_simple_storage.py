from brownie import accounts, SimpleStorage

# note all test functions have to start with test as well as the name of the .py file
# note brownie test -k test_update_store to test an individual function


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrive()
    expected = 0
    # assert
    assert starting_value == expected


def test_update_store():

    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 22
    simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrive()
