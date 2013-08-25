#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

import time
import datetime
import pooler
from osv import osv
from osv import fields
from datetime import date


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'twitter' : fields.char('Twitter', size=255),
        'facebook' : fields.char('Facebook', size=255),
        'skype' : fields.char('Skype', size=255),
        'linkedin' : fields.char('Linkedin', size=255),
        'googleplus' : fields.char('Google+', size=255),
        'youtube' : fields.char('Youtube', size=255),
                }
res_partner()
