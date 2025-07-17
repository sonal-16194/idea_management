from odoo import models, fields

class IdeaManagement(models.Model):
    _name = 'idea.idea'
    _description = "IDEA"
    _rec_name = 'category_name'

    responsible_users = fields.Many2one('res.users', string='Responsible User')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approve'),
        ('cancle', 'Cancle')
    ], default='draft', string='Status')

    category_name = fields.Selection([
        ('suggestion', 'Suggestion'),
        ('enhancement', 'Enhancement'),
        ('improvement', 'Improvement'),
        ('awareness', 'Awareness'),
        ('apperation', 'Apperation')
    ], string='Category Name', required=True, tracking=True)

    task_ids = fields.One2many('project.task', 'idea_id', string="Related Tasks")

    def name_get(self):
        result = []
        selection_dict = dict(self.fields_get(allfields=['category_name'])['category_name']['selection'])
        for rec in self:
            name = selection_dict.get(rec.category_name, rec.category_name)
            result.append((rec.id, name))
        return result
