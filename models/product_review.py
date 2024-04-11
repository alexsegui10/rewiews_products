from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductReview(models.Model):
    _name = 'product.review'
    _description = 'Reseña de Producto'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Título', compute='_compute_name')
    description = fields.Text(string='Descripción de la Reseña', required=True)
    rating = fields.Selection([(str(num), str(num)) for num in range(1, 6)],
                              string='Número de Estrellas', required=True)
    date = fields.Date(string='Fecha de la Reseña', default=fields.Date.context_today, readonly=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user, readonly=True)

    @api.depends('user_id')
    def _compute_name(self):
        for review in self:
            review.name = 'Reseña (%s)' % review.user_id.name

    @api.model
    def create(self, vals):
        product = self.env['product.product'].browse(vals.get('product_id'))
        if not self.env['sale.order.line'].search([('product_id', '=', product.id), ('order_id.partner_id', '=', self.env.user.partner_id.id)]):
            raise ValidationError("Solo puedes reseñar productos que hayas comprado.")
        return super(ProductReview, self).create(vals)

    def write(self, vals):
        if 'user_id' in vals and vals['user_id'] != self.env.uid:
            raise ValidationError("Solo puedes editar tus propias reseñas.")
        return super(ProductReview, self).write(vals)
