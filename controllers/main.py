from odoo import http
from odoo.http import request

class EcolePortal(http.Controller):

    @http.route('/mes-notes', type='http', auth='public', website=True)
    def mes_notes(self, **kwargs):
        # Pour cet exemple simple, on récupère les notes sans authentification stricte 
        # (Dans un vrai projet, auth='user' et filtrer par l'utilisateur connecté)
        # Mais pour la démo, on affiche toutes les notes pour montrer le tableau
        notes = request.env['ecole.note'].sudo().search([])
        
        valeurs = {
            'notes': notes,
        }
        return request.render('ecole.portal_mes_notes', valeurs)
