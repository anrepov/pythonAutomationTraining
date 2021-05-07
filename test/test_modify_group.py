# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first(Group("name_mod", "header_mod", "footer_mod"))
