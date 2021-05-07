# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test"))
    app.group.modify_first(Group("name_mod", "header_mod", "footer_mod"))
