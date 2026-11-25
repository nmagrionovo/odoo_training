from odoo import fields, models
from dateutil.relativedelta import relativedelta






class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    visible = fields.Boolean(default=True)
    name = fields.Char(required=True)
    description = fields.Text(string='Description')

    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Received"),
            ("accepted", "Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required = True,
        copy = False,   #Indica che in caso di duplicazione del record questa proprietà non viene riportata
        default = "new"
    )

    def _default_date_availability(self):
        return fields.Date.today() + relativedelta(months=3)

    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability', default = _default_date_availability, copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], help='Garden orientation')