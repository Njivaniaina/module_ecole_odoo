# Gestion École - Odoo 17

Ce module permet de gérer les aspects fondamentaux d'une école (Étudiants, Cours, Notes) au sein de l'ERP Odoo.

## Fonctionnalités principales

*   **Gestion des Étudiants** : Suivi des informations personnelles, génération automatique de matricules et calcul de la moyenne générale.
*   **Gestion des Cours** : Cycle de vie d'un cours (Brouillon, Ouvert, Clôturé), inscriptions d'étudiants (Many2many).
*   **Gestion des Notes** : Enregistrement des résultats académiques avec évaluation automatique (Excellent, Bien, Passable, etc.).
*   **Données de Démonstration** : Inclut des exemples d'étudiants, de cours et de notes pour tester rapidement le module.

## Installation

### Prérequis
- Odoo 17 ou supérieur.
- Accès au répertoire `addons` de votre installation Odoo.

### Étapes d'installation
1.  Copiez le dossier `ecole` dans votre dossier `addons` d'Odoo.
2.  Redémarrez votre serveur Odoo.
3.  Activez le **Mode Développeur** dans les paramètres d'Odoo.
4.  Allez dans le menu **Applications**.
5.  Cliquez sur **Mettre à jour la liste des applications**.
6.  Recherchez "Gestion École" et cliquez sur **Installer**.

### Mise à jour via terminal (recommandé pour le développement)
Si vous modifiez le code, vous pouvez mettre à jour le module avec cette commande :
```bash
./odoo-bin -u ecole -d VOTRE_BASE_DE_DONNEES
```

## Utilisation

Une fois installé, un nouveau menu **École** apparaît.
- Utilisez le menu **Étudiants** pour créer vos fiches élèves.
- Utilisez le menu **Cours** pour préparer vos sessions et inscrire les élèves.
- Les notes peuvent être saisies depuis l'onglet dédié ou directement via le menu **Notes**.

## Auteur
Développé par Fenosoa (Mis à jour vers Odoo 17).
