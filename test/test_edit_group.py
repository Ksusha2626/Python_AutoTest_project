from model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_group = db.get_group_list()
    index = random.choice(range(len(old_group)))
    id = old_group[index].id
    group = Group(name="111", id=id)
    app.group.edit_group_by_id(id, group)
    new_group = db.get_group_list()
    assert len(old_group) == len(new_group)
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.rstrip())
        assert sorted(list(map(clean, new_group)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                  key=Group.id_or_max)
