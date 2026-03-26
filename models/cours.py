from odoo import models, fields, api

class Cours(models.Model):
    _name = 'ecole.cours'
    _description = 'Cours'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Intitulé du cours', required=True)
    code = fields.Char(string='Code cours', readonly=True, copy=False)
    
    description = fields.Text(string='Description')
    
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    
    capacite = fields.Integer(string='Capacité max', default=30)
    
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('ouvert', 'Ouvert'),
        ('cloture', 'Clôturé'),
    ], string='État', default='brouillon', tracking=True)

    # Relation avec les étudiants (Many2many)
    etudiant_ids = fields.Many2many(
        'ecole.etudiant',
        'ecole_cours_etudiant_rel',
        'cours_id',
        'etudiant_id',
        string='Étudiants inscrits'
    )

    nb_etudiants = fields.Integer(
        string='Nombre d\'étudiants',
        compute='_compute_nb_etudiants',
        store=True
    )

    @api.depends('etudiant_ids')
    def _compute_nb_etudiants(self):
        for cours in self:
            cours.nb_etudiants = len(cours.etudiant_ids)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('code'):
                vals['code'] = self.env['ir.sequence'].next_by_code('ecole.cours')
        return super().create(vals_list)

    def action_ouvrir(self):
        self.etat = 'ouvert'

    def action_cloturer(self):
        self.etat = 'cloture'

    def action_brouillon(self):
        self.etat = 'brouillon'