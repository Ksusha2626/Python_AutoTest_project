from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_group = app.group.get_group_list()
    group = Group(name="111")
    group.id = old_group[0].id
    app.group.edit_group(Group(name="111"))
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
    old_group[0] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
