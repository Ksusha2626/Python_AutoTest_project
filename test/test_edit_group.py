from model.group import Group
from random import randrange


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    group = Group(name="111")
    group.id = old_group[index].id
    app.group.edit_group_by_index(index, group)
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
