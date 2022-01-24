# -*- coding: utf-8 -*-
from odoo import models


class PurchaseDetailsXlsx(models.AbstractModel):
    _name = 'report.report_purchase_request_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, order):
        sheet = workbook.add_worksheet('Purchase_Request')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center'})
        center = workbook.add_format({'align': 'center'})
        purchase_req_no = 0
        row = 2
        row_1 = 2
        row_2 = 2
        row_3 = 16
        row_4 = 16
        row_5 = 16
        col = 2
        sheet.set_column('C:D', 20)
        sheet.set_column('E:F', 20)
        sheet.set_column('G:H', 20)
        sheet.set_column('I:J', 20)
        sheet.set_column('K:L', 20)

        for obj in order:
            purchase_req_no += 1
            sheet.merge_range(row, col, row, col + 3, f'Purchase Request Details {purchase_req_no}', format_1)
            # Right columns
            row_1 += 2
            sheet.write(row_1, col, 'Name', format_1)
            sheet.write(row_1, col + 1, obj.name, center)

            row_1 += 2
            sheet.write(row_1, col, 'Requested by', format_1)
            sheet.write(row_1, col + 1, obj.requested_by_id.name, center)

            row_1 += 2
            sheet.write(row_1, col, 'Total Price', format_1)
            sheet.write(row_1, col + 1, obj.total_price, center)

            # Left columns
            row_2 += 2
            sheet.write(row_2, col + 2, 'Start Date', format_1)
            sheet.write(row_2, col + 3, str(obj.start_date), center)

            row_2 += 2
            sheet.write(row_2, col + 2, 'End Date', format_1)
            sheet.write(row_2, col + 3, str(obj.end_date), center)

            row_2 += 2
            sheet.write(row_2, col + 2, 'Rejection Reason', format_1)
            sheet.write(row_2, col + 3, obj.rejection_reason, center)

            if obj.order_lines:
                for order in obj.order_lines:
                    # Right columns
                    row_1 += 2
                    sheet.write(row_1, col, 'Product Name', format_1)
                    sheet.write(row_1, col + 1, order.product_id.name, center)
                    # Left columns
                    row_2 += 2
                    sheet.write(row_1, col + 2, 'Description', format_1)
                    sheet.write(row_1, col + 3, order.description, center)

                    sheet.write(row_1, col + 4, 'Quantity', format_1)
                    sheet.write(row_1, col + 5, order.quantity, center)

                    sheet.write(row_1, col + 6, 'Cost Price', format_1)
                    sheet.write(row_1, col + 7, order.cost_price, center)

                    sheet.write(row_1, col + 8, 'Total', format_1)
                    sheet.write(row_1, col + 9, order.total, center)

            row += 15
            row_1 += 3
            row_2 += 3
