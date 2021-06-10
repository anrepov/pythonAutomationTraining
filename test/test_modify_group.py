# -*- coding: utf-8 -*-
import random

from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if db.get_group_list() == 0:
        app.group.create(Group("test"))

    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)

    new_group = Group(id=old_group.id, name=old_group.name + "_mod")
    app.group.modify_by_id(new_group, old_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    if check_ui:
        for group in new_groups:
            index = new_groups.index(group)
            new_groups[index] = Group(id=group.id, name=group.name.strip())

        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
