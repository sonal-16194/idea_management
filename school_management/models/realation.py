from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class School2(models.Model):
    _name = 'school2.school2'
    _description = 'School2'

    name = fields.Char(string='School Name')
    student_ids = fields.One2many('school2.student2', 'school2_id', string="Students")


class Student2(models.Model):
    _name = 'school2.student2'
    _description = 'Student2'

    s_name = fields.Char(string="Student Name")  
    age = fields.Integer(string="Age")
    school2_id = fields.Many2one('school2.school2', string="School")


