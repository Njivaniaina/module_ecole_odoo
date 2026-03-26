from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Note(models.Model):
    _name        = 'ecole.note'
    _description = 'Note'
    _order       = 'etudiant_id, cours_id'

    # Relations
    etudiant_id = fields.Many2one(
        'ecole.etudiant',
        string='Étudiant',
        required=True,
        ondelete='cascade'
    )
    cours_id = fields.Many2one(
        'ecole.cours',
        string='Cours',
        required=True,
        ondelete='cascade'
    )

    # Champs
    note        = fields.Float(string='Note', digits=(5, 2))
    appreciation = fields.Selection([
        ('excellent', 'Excellent'),
        ('bien',      'Bien'),
        ('passable',  'Passable'),
        ('insuffisant','Insuffisant'),
    ], string='Appréciation', compute='_compute_appreciation', store=True)

    commentaire = fields.Text(string='Commentaire')
    date        = fields.Date(string='Date', default=fields.Date.today)

    @api.depends('note')
    def _compute_appreciation(self):
        for rec in self:
            if rec.note >= 16:
                rec.appreciation = 'excellent'
            elif rec.note >= 12:
                rec.appreciation = 'bien'
            elif rec.note >= 10:
                rec.appreciation = 'passable'
            else:
                rec.appreciation = 'insuffisant'

    @api.constrains('note')
    def _check_note(self):
        for rec in self:
            if rec.note < 0 or rec.note > 20:
                raise ValidationError("La note doit être entre 0 et 20 !")

    @api.model_create_multi
    def create(self, vals_list):
        records = super(Note, self).create(vals_list)
        template = self.env.ref('ecole.email_template_note_result', raise_if_not_found=False)
        if template:
            for rec in records:
                if rec.etudiant_id.email:
                    template.send_mail(rec.id, force_send=False)
        return records