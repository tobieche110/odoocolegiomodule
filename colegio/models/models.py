# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
    _name = "colegio.alumno" # Nombre de la tabla

    # Columnas de la tabla
    # Con nombre, apellido y legajo deberia ser suficiente para inscribir un alumno en este sistema
    # Los legajos no pueden repetirse
    nombre = fields.Char("Nombre", required=True)
    apellido = fields.Char("Apellido", required=True)
    fecha_nacimiento = fields.Date("Fecha de nacimiento")
    legajo = fields.Integer("Legajo", unique=True, required=True)
    email = fields.Char("Email")
    telefono = fields.Char("Telefono")
    direccion = fields.Char("Direccion")
    pais = fields.Char("Pais")

class Programa(models.Model):
    _name = "colegio.programa"

    nombre = fields.Char("Nombre", unique=True, required=True)
    descripcion = fields.Text("Descripcion")

class Inscripcion(models.Model):
    _name = "colegio.inscripcion"

    alumno_id = fields.Many2one("colegio.alumno", "Alumno", required=True)
    programa_id = fields.Many2one("colegio.programa", "Programa", required=True)

    # La idea de la siguiente linea era lograr que no pueda inscribirse el mismo alumno al mismo programa mas de una vez.
    _sql_constraints = [
        ('alumno_programa_unique', 'unique(alumno_id, programa_id)', 'El alumno no puede estar inscripto dos veces en el mismo programa.')
    ]


