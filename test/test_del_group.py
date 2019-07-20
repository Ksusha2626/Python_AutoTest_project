from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_group = db.get_group_list()
    group = random.choice(old_group)
    app.group.delete_group_by_id(group.id)
    new_group = db.get_group_list()
    assert len(old_group) - 1 == len(new_group)
    old_group.remove(group)
    assert old_group == new_group
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.rstrip())

        assert sorted(list(map(clean, new_group)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                  key=Group.id_or_max)
