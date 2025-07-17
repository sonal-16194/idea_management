from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    idea_create_id = fields.Many2one('idea_create.idea_create', string="Related Idea")
    idea_id = fields.Many2one('idea.idea', string="Idea Category")
