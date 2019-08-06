from model.group import Group
import random
import pytest


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    with pytest.allure.step('Получение список групп'):
        old_group = db.get_group_list()
    with pytest.allure.step('Выбираем группу'):
        index = random.choice(range(len(old_group)))
    id = old_group[index].id
    group = Group(name="111", id=id)
    with pytest.allure.step('Изменяем выбранную группу'):
        app.group.edit_group_by_id(id, group)
    with pytest.allure.step('Получение новый список групп'):
        new_group = db.get_group_list()
    with pytest.allure.step('Проверяем соответствие списков'):
        assert len(old_group) == len(new_group)
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.rstrip())

        assert sorted(list(map(clean, new_group)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                  key=Group.id_or_max)
