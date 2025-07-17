 # Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'STUDENT'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # <-- this MUST be a list

    name = fields.Char(string="Name", required=True, tracking=True)
    roll_number = fields.Integer(string="Roll Number")
    standard = fields.Char(string="Class/Standard")
    active = fields.Boolean(default=True)

    s_name = fields.Char()
    mo_number = fields.Integer()
    status = fields.Selection([
    ('draft', 'Draft'),
    ('inprogress', 'Inprogress'),
    ('done', 'Done'),
    ('cancle','Cancle')
    ], string="Status", default='draft', tracking=True)


    description = fields.Text(string = "Description")
    content = fields.Html(string = "Content")
    file_data = fields.Binary(string='File', attachment=True)
    country_id = fields.Many2one('res.country',string = "Country")
    country_ids = fields.Many2many('res.country',string = "countries")    
    birth_date = fields.Date('DOB')
    age = fields.Integer()

    #onchange method:-
    quantity = fields.Integer()
    price = fields.Float()
    total = fields.Float()

    @api.onchange('quantity','price')

    def onchange_total(self):
        self.total = self.quantity * self.price



    # compute method:-
    total_compute = fields.Float(compute = 'compute_total')

    @api.depends('quantity','price')

    def compute_total(self):
        for record in self:
            record.total_compute = record.quantity * record.price


  #onchange method:
    @api.onchange('birth_date')
    def calulate_age(self):
        # today_date = self.fields.today()
        # self.birth_date

        self.age = 20

    full_name = fields.Char('Full Name', compute="compute_date_method")
    @api.depends('name','s_name')

    def compute_date_method(self):
        #  Full name
       for record in self:
           record.full_name = f"{record.name or ''} {record.s_name or ''}".strip()  
      


      #button

    def state_change_done(self):
    
        for record in self:
            record.status ='draft'

    def state_change_inprogress(self):

        for record in self:
            record.status = 'done'


    def state_change_cancle(self):

        for record in self:
            record.status = 'draft'

    def state_change_draftc(self):

        for record in self:
            record.status = 'cancle'

    def state_change_drafti(self):

        for record in self:
            record.status = 'inprogress'


    

    def check_orm(self):
        for rec in self:
            search_var = self.env['student.student'].search([('name', '=', 'sonal')])
            print('search var-------------------',search_var)



    def action_done(self):
        # Your logic here
        for record in self:
            record.status = 'done'


    def send_email(self):
        print("sendind a mail")