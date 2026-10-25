from pathlib import Path
from pytest_bdd import scenario, given, when, then, parsers

BEHAVIOR_DIR_NAME = "behavior_feature"

# Helper to discover Gherkin files
def file_discovery(file_name):
    base_dir = Path(__file__).resolve().parent.parent / BEHAVIOR_DIR_NAME
    return (base_dir / file_name).with_suffix(".feature")


@scenario(file_discovery("inventory_behavior"),
          "Use a potion")
def test_use_potion():
    pass

@given("the inventory contains 3 items",
       target_fixture="initial_inventory")
def init_inventory():
    inventory = {"potion", "sword", "shield"}
    return inventory

@when("the character uses the potion",
      target_fixture="result_inventory")
def use_potion(initial_inventory):
    temp_inventory = initial_inventory.copy()
    temp_inventory.remove("potion")
    return temp_inventory

@scenario(file_discovery("inventory_behavior"),
          "Find a treasure")
def test_find_treasure():
    pass


@when("the character finds a gem",
      target_fixture="copy_inventory")
def find_gem(initial_inventory):
    temp_inventory = initial_inventory.copy()
    return temp_inventory

@when("the character adds it to the inventory",
      target_fixture="result_inventory")
def add_gem(copy_inventory):
    copy_inventory.add("gem")
    return copy_inventory

@then(parsers.parse("{count:d} items should remain in the inventory"))
def check_remaining_items(result_inventory,count):
    assert len(result_inventory) == count

