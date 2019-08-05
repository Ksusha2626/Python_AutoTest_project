from pytest_bdd import given, when, then
from fixture.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group, app, check_ui):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())
        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                   key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New_group"))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())

        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                   key=Group.id_or_max)


@given('a modified group with <name>, <header> and <footer>')
def group_for_modify(name, header, footer, random_group):
    return Group(name=name, header=header, footer=footer, id=random_group.id)


@when('I modify the group in the list')
def modify_group(app, random_group, group_for_modify):
    app.group.edit_group_by_id(random_group.id, group_for_modify)


@then('the new group list is equal to the old list with the modified group')
def verify_group_modified(app, db, non_empty_group_list, random_group, group_for_modify, check_ui):
    old_groups = non_empty_group_list
    old_groups.remove(random_group)
    old_groups.append(group_for_modify)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())

        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                   key=Group.id_or_max)