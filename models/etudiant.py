from odoo import models, fields, api

class Etudiant(models.Model):
    _name = 'ecole.etudiant'
    _description = 'Étudiant'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nom complet', required=True, tracking=True)
    matricule = fields.Char(string='Matricule', readonly=True, copy=False)
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
    date_naissance = fields.Date(string='Date de naissance')
    
    genre = fields.Selection([
        ('masculin', 'Masculin'),
        ('feminin', 'Féminin'),
    ], string='Genre')

    actif = fields.Boolean(string='Actif', default=True)
    
    notes = fields.Text(string='Notes')

    # Champs relationnels
    note_ids = fields.One2many(
        'ecole.note',
        'etudiant_id',
        string='Notes'
    )

    cours_ids = fields.Many2many(
        'ecole.cours',
        'ecole_cours_etudiant_rel',
        'etudiant_id',
        'cours_id',
        string='Cours suivis'
    )

    nb_cours = fields.Integer(
        string='Nombre de cours',
        compute='_compute_nb_cours',
        store=True
    )

    moyenne = fields.Float(
        string='Moyenne',
        compute='_compute_moyenne',
        store=True,
        digits=(5, 2)
    )

    # ← AJOUTER CES DEUX MÉTHODES
    @api.depends('cours_ids')
    def _compute_nb_cours(self):
        for etudiant in self:
            etudiant.nb_cours = len(etudiant.cours_ids)

    @api.depends('note_ids.note')
    def _compute_moyenne(self):
        for etudiant in self:
            notes = etudiant.note_ids.mapped('note')
            etudiant.moyenne = sum(notes) / len(notes) if notes else 0.0

    # Génération automatique du matricule
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('matricule'):
                vals['matricule'] = self.env['ir.sequence'].next_by_code('ecole.etudiant')
        return super().create(vals_list)