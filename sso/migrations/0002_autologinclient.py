# Generated by Django 4.2.2 on 2023-07-26 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sso", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AutologinClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enable_autologin",
                    models.BooleanField(
                        default=True,
                        help_text="En cas de succès du login sur un client autologin, activer la connexion automatique pour tous les autres clients autologin",
                        verbose_name="Activer l’autologin ?",
                    ),
                ),
                (
                    "autologin_url",
                    models.URLField(
                        blank=True,
                        help_text="URL à insérer dans l’iframe qui servira à faire l'autologin",
                        verbose_name="URL pour l’autologin",
                    ),
                ),
                (
                    "oidc_client",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oidc_provider.client",
                    ),
                ),
            ],
        ),
    ]
