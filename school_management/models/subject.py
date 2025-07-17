from odoo import models, fields ,api


class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'SUBJECT'

#genral info tab
   
    name = fields.Char(required=True)

#marks tab
    marks = fields.Integer()    
    persantage = fields.Float() 

#Detailed tab
    date = fields.Date()
    result = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail')
    ], string='Result')
    practicle = fields.Boolean(string = 'Pass OR Fail', default = True)


    def change_orm(self):
        for rec in self:
            search_marks = self.env['subject.subject'].search([('marks', '>', 50)])
            print("search_marks===========================",search_marks)

    #search_count

            marks_count = self.env['subject.subject'].search_count([('result', '=', 'fail')])
            print("marks_count========================",marks_count)

    #ref method

            #subject_ref = self.env.ref('')
            #print("subject_ref==================",subject_ref)

    # browse method

            marks_browse = self.env['subject.subject'].browse([2, 4])
            for record in marks_browse:
                print("marks_browse==================", record.name)
                #print("marks_browse==================",marks_browse[i])


    #create() method

            vals = {
                'name' :'chemistry',
                'marks' : '76',
            }

            new_subject = self.env['subject.subject'].create(vals)   

           
            print("new_subject==========================",new_subject.name)

    # write() method 
            record_update = self.env['subject.subject'].browse(16)
            if record_update.exists():
                vals = {
                    'persantage' : '87'

                }
                record_update.write(vals)


    # copy() method
            #record_update = self.env['subject.subject'].browse(5)
           # record_update.copy()

    
    #unlink() methos

            record_update = self.env['subject.subject'].browse(6)
            record_update.unlink()