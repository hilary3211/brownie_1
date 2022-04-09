from brownie import (
    accounts,
    config,
    SimpleStorage,
    network,
)  # importing the neccessary libs


def deploy_ss():  # defining a function to deploy the smart contract
    account = get_account()
    simplestorage = SimpleStorage.deploy({"from": account})  # deploys the contract
    stored_value = (
        simplestorage.retrive()
    )  # calling a function in the simplestorage smart contract
    print(stored_value)
    transaction = simplestorage.store(
        22, {"from": account}
    )  # calling a function in the simplestorage smart contract
    transaction.wait(1)
    update_sv = (
        simplestorage.retrive()
    )  # calling a function in the simplestorage smart contract
    print(update_sv)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_ss()
