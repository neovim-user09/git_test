from odoo import models, fields

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    lot_id = fields.Many2one(
        "stock.lot",
        "Roll No.",
        index=True,
        ondelete="restrict",
        check_company=True,

    )

    expiration_date = fields.Datetime(
        string="Expiration Date",
        related="lot_id.expiration_date",
        store=False,
        help="Expiration date of the lot/serial number"
    )