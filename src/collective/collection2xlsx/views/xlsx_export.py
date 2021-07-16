# -*- coding: utf-8 -*-
import io
from datetime import datetime

import xlsxwriter
from plone.app.contenttypes import _
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter

# from collective.collection2xlsx import _


class XlsxExport(BrowserView):
    def __call__(self):
        self.listing_view = getMultiAdapter((self.context, self.request), name=u"view")
        self.fields = self.listing_view.tabular_fields()
        self.batch = self.listing_view.batch()
        rows = []
        headers = [_(self.tabular_field_label(f).capitalize()) for f in self.fields]
        rows.append(headers)
        data = []
        for item in self.batch:
            data_row = []
            for field in self.fields:
                _(data_row.append(self.tabular_fielddata(item, field).get("value")))
            data.append(data_row)
        rows.extend(data)
        return self.generate_xlsx(rows)

    def tabular_field_label(self, field):
        return self.listing_view.tabular_field_label(field)

    def tabular_fielddata(self, item, field):
        return self.listing_view.tabular_fielddata(item, field)

    def generate_xlsx(self, rows):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        row_index = 0
        for row in rows:
            col_index = 0
            for col in row:
                worksheet.write(row_index, col_index, col)
                col_index += 1
            row_index += 1

        workbook.close()
        output.seek(0)
        filename = self._filename()
        self.request.response.setHeader(
            "Content-Type",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        self.request.response.setHeader(
            "Content-Disposition", "inline;filename=%s" % filename
        )
        # self.request.response.setHeader("Content-Length", len(output))
        return output

    def _filename(self):
        filename = self.context.id
        now = datetime.now()
        filename += "_{0}{1}{2}_{3}{4}.xlsx".format(
            now.year, now.month, now.day, now.hour, now.minute
        )
        return filename
