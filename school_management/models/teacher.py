# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields



class Teacher(models.Model):
    _name = 'teacher.teacher'

    name = fields.Char()
    s_name = fields.Char()
    mo_number = fields.Integer()
