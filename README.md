# Module Odoo : Gestion École 🎓

Ce module est une application complète de gestion scolaire développée pour Odoo 17. Il a été conçu pour structurer et automatiser la gestion des étudiants, des enseignants, des cours, des inscriptions et des notes.

## 🚀 Fonctionnalités Clés

### 1. Gestion des Entités (Data Model)
- **Étudiants** : Création de profils étudiants avec informations de contact, matricule, et liste des cours inscrits.
- **Enseignants** : Fiches dédiées pour le corps professoral (spécialité, téléphone) avec liaison aux utilisateurs Odoo.
- **Cours** : Gestion des matières, affectation d'un enseignant, et suivi des étudiants inscrits (smart buttons).
- **Notes** : Saisie des résultats pour un étudiant dans un cours donné avec appréciation automatique ("Excellent", "Bien", "Passable", etc.) et contrôle (0-20).

### 2. Workflows & Validation Métier
- **Cycle de vie des cours** : Les cours possèdent un état (Brouillon -> Ouvert -> Clôturé) géré via une `statusbar`.
- **Mécanismes de blocage** : Impossible d'ouvrir un cours si aucun enseignant n'y est assigné (erreur bloquante de type `UserError`).
- **Verrouillage des données** : Les champs importants (comme le nom ou l'enseignant du cours) deviennent non modifiables (`readonly`) une fois le cours validé.

### 3. Sécurité Extrême (ACL & Rules)
- **Droits Globaux (ACL)** : Deux groupes de sécurité ont été créés : `ecole_group_user` (Enseignant) et `ecole_group_manager` (Directeur).
- **Filtrage des enregistrements (Record Rules)** :
  - *Directeur* : A accès à la totalité des dossiers de l'école.
  - *Enseignant* : Le formateur ne peut voir **que ses propres cours** et ses propres notes, masquant ainsi les autres matières pour garantir la confidentialité des données.

### 4. Rapports Analytiques (Dashboards)
- **Vues Pivot** : Analyse dynamique et tableaux croisés générés automatiquement pour visualiser les moyennes des notes par étudiant et par cours.
- **Vues Graphiques** : Mises en page en diagrammes (Barres, Lignes, Camembert) pour obtenir une vue instantanée du taux de remplissage des classes.

### 5. Automatisation (Emails) 📧
- **Avis de résultats** : Lors de la saisie ou de la confirmation d'une note, le module génère automatiquement un courriel personnalisé à l'étudiant via un modèle `mail.template` (Jinja/QWeb) comportant sa note, l'appréciation, et le nom du cours.

### 6. Portail Public & Édition PDF
- **Portail Étudiant Web** : Un contrôleur Python et un template HTML (`QWeb`) ajoutent la page web `/mes-notes`. Les étudiants (ou visiteurs) peuvent lister les résultats scolaires formatés dans un joli tableau Bootstrap directement sur le front-end du CMS Odoo.
- **Génération de PDF** : Impression du bulletin de notes complet avec logo en un clic au format A4 (`ir.actions.report`).

---

## 🛠️ Instructions d'Installation (Odoo 17)

1. Clonez ou copiez le dossier `ecole` dans le dossier `addons` de votre serveur Odoo (`/home/utilisateur/odoo/addons/`).
2. Assurez-vous d'avoir les dépendances Odoo dans votre environnement (ex: le module `mail` qui est requis dans `depends`).
3. Relancez votre serveur Odoo en forçant la mise à jour des modules :
   ```bash
   ./odoo-bin -c odoo.conf -u ecole -d VOTRE_BASE_DE_DONNEES
   ```
4. Dans Odoo, allez dans **Applications**, cherchez *Gestion École*, et cliquez sur **Installer** ou **Mettre à jour**.

---

*Développé comme projet modèle d'apprentissage Odoo MVC complet (Modèles, Vues, Contrôleurs).*
