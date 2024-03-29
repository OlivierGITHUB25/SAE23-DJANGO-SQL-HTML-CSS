# Generated by Django 4.0.5 on 2022-06-16 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idcours', models.AutoField(db_column='idCours', primary_key=True, serialize=False)),
                ('titre_cours', models.CharField(blank=True, db_column='titre cours', max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('durée', models.TimeField(blank=True, db_column='Durée', null=True)),
            ],
            options={
                'db_table': 'Cours',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enseignants',
            fields=[
                ('idenseignants', models.AutoField(db_column='idEnseignants', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=45, null=True)),
                ('prenom', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=144, null=True)),
            ],
            options={
                'db_table': 'Enseignants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiants',
            fields=[
                ('idetudiants', models.AutoField(db_column='idEtudiants', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=45, null=True)),
                ('prenom', models.CharField(blank=True, db_column='Prenom', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=144, null=True)),
                ('photo', models.TextField(blank=True, db_column='Photo', null=True)),
            ],
            options={
                'db_table': 'Etudiants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupesEtudiant',
            fields=[
                ('idgroupesetudiant', models.AutoField(db_column='idgroupes_etudiant', primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, db_column='Nom', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Groupes-etudiant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Absences',
            fields=[
                ('idabsences', models.AutoField(db_column='idabsences', primary_key=True, serialize=False)),
                ('justification', models.TextField(blank=True, null=True)),
                ('justifie', models.CharField(blank=True, max_length=7, null=True)),
                ('cours', models.ForeignKey(db_column='Cours', on_delete=django.db.models.deletion.DO_NOTHING, to='absence.cours')),
                ('etudiant', models.ForeignKey(db_column='Etudiant', on_delete=django.db.models.deletion.DO_NOTHING, to='absence.etudiants')),
            ],
            options={
                'db_table': 'absences',
                'managed': True,
                'unique_together': {('idabsences', 'etudiant', 'cours')},
            },
        ),
    ]
