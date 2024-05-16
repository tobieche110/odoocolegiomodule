# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class Colegio(http.Controller):
    
    @http.route('/api/alumnos_inscriptos/<int:programa_id_param>', type='http', auth='public', methods=['GET'])
    def get_alumnos_inscritos(self, programa_id_param):
        # Busco en la url el id del programa
        programa_id = programa_id_param
        # Accedo a la BDD como SU y traigo los registros que matcheen los id del programa
        alumnos = request.env['colegio.inscripcion'].sudo().search([('programa_id', '=', programa_id)])
        alumnos_list = []
        # Itero los alumnos y con el id puedo acceder a sus campos
        for alumno in alumnos:
            alumno_data = {
                'nombre': alumno.alumno_id.nombre,
                'apellido': alumno.alumno_id.apellido,
                'legajo': alumno.alumno_id.legajo,
                'fecha_nacimiento': alumno.alumno_id.fecha_nacimiento.strftime("%d/%m/%Y"),
                'email': alumno.alumno_id.email,
                'telefono': alumno.alumno_id.telefono,
                'pais': alumno.alumno_id.pais
            }
            # Agrego el objeto del alumno a una lista de alumnos
            alumnos_list.append(alumno_data)

        # Retorno la lista de alumnos como JSON
        return json.dumps(alumnos_list)
    