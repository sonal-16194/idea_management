from odoo import models, fields 

class idea_create(models.Model):
    _name = 'idea_create.idea_create'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Idea Create'


    name = fields.Char(string = 'Subject', required = True ,tracking = True)
    category_name= fields.Many2one('idea.idea', string='Category')
    idea_manager = fields.Many2one('res.users',string = "Idea Manager")
    other_members = fields.Many2many('res.users',relation='idea_create_other_members_rel',string = "Other Member")
    suggested_by = fields.Many2many('res.users',relation='idea_create_other_members_rel',string = "Suggested By")
    responsible_members = fields.Many2many('res.users',relation='idea_create_other_members_rel',string = "Responsible Members")
    description = fields.Text(string = "Description")
    created_at = fields.Datetime(string='Created At', default=fields.Datetime.now)
    state = fields.Selection([
    
    ('pending','Pending'),
    ('confirmed','Confirmed'),
    ('approved','Approved'),
    ('cancelled', 'Cancelled'),
    ],)
    cancel_reason = fields.Text(string='Cancellation Reason')
            


    task_ids = fields.One2many('project.task', 'idea_create_id', string="Related Tasks")

    # cancle button

    class CancelReasonWizard(models.TransientModel):
        _name = 'cancel.reason.wizard'
        _description = 'Cancel Reason Wizard'

        reason = fields.Text('Cancellation Reason', required=True)

        def confirm_cancel(self):
            active_model = self.env.context.get('active_model')
            active_ids = self.env.context.get('active_ids')
            records = self.env[active_model].browse(active_ids)

            for record in records:
                record.cancel_reason = self.reason
                record.state = 'cancelled'
                record.message_post(body=f"Cancelled with reason: {self.reason}")

     # approve button

    def  approve(self):
    
        for record in self:
            record.state ='approved'
            record.message_post(
                body="The idea has moved to Approved.",
                subject="Idea Approved",
            )
        # pending state button

    def  request_to_confirmation(self):
    
        for record in self:
            record.state ='pending'
            record.message_post(
                body="The idea has moved to Pending.",
                subject="Idea Pending",
                
            )


        # confirmed state button

    def  request_to_approved(self):
    
        for record in self:
            record.state ='confirmed'
            record.message_post(
                body="The idea has moved to confirmed.",
                subject="Idea Confirmed",
            )

        # cancle state button

    def  request_to_cancle(self):
    
        for record in self:
            record.state ='cancle'

            
                  

