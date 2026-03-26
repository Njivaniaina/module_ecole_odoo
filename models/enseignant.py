from odoo import models, fields, api

class Enseignant(models.Model):
    _name = 'ecole.enseignant'
    _description = 'Enseignant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nom complet', required=True, tracking=True)
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
    
    specialite = fields.Selection([
        ('lettres', 'Lettres'),
        ('sciences', 'Sciences'),
        ('informatique', 'Informatique'),
        ('langues', 'Langues'),
    ], string='Spécialité')

    user_id = fields.Many2one(
        'res.users',
        string='Utilisateur Odoo',
        help='L\'utilisateur Odoo lié à cet enseignant pour la sécurité.'
    )

    # Relation One2many : un enseignant a plusieurs cours
    cours_ids = fields.One2many(
        'ecole.cours',       # Modèle cible
        'enseignant_id',    # Champ Many2one dans le modèle cible
        string='Cours dispensés'
    )

    nb_cours = fields.Integer(
        string='Nombre de cours',
        compute='_compute_nb_cours'
    )

    @api.depends('cours_ids')
    def _compute_nb_cours(self):
        for rec in self:
            rec.nb_cours = len(rec.cours_ids)

    def action_view_cours(self):
        self.ensure_one()
        return {
            'name': 'Cours dispensés',
            'type': 'ir.actions.act_window',
            'res_model': 'ecole.cours',
            'view_mode': 'tree,form',
            'domain': [('enseignant_id', '=', self.id)],
            'context': {'default_enseignant_id': self.id},
        }
