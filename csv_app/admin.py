from django.contrib import admin
from .models import Stock, Period, Csv, FinancialData, Analysis
import csv

admin.site.register(Stock)
admin.site.register(Period)
#admin.site.register(Analysis)
admin.site.register(Csv)


class FinancialDataAdmin(admin.ModelAdmin):
    list_display = ('year', 'revenue', 'pre_tax_op_margin', 'after_tax_op_income', 'stock')

    actions = ['import_csv_data']

    def import_csv_data(self, request, queryset):
        import pdb; pdb.set_trace()
        for csv_instance in queryset:
            with open(csv_instance.file_name.path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                 # Skip the header row
                next(csv_reader, None)

                for row in csv_reader:
                    stock_symbol = row.get('stock_symbol')
                    print(f"Processing row with stock_symbol: {stock_symbol}")
                    if stock_symbol:
                        # Assuming that stock_symbol is unique in the Stock model
                        stock_instance, created = Stock.objects.get_or_create(stock_symbol=stock_symbol)
                        
                        FinancialData.objects.create(
                            year=int(row['year']),
                            revenue=float(row['Revenue']) if row['Revenue'] else None,
                            revenue_growth_rate=float(row['Revenue_growth_rate']) if row['Revenue_growth_rate'] else None,
                            pre_tax_op_margin=float(row['Pre_tax_op_margin']) if row['Pre_tax_op_margin'] else None,
                            pre_tax_op_income=float(row['Pre_tax_op_income']) if row['Pre_tax_op_income'] else None,
                            taxes=float(row['Taxes']) if row['Taxes'] else None,
                            after_tax_op_income=float(row['After_tax_op_income']) if row['After_tax_op_income'] else None,
                            taxes_val=float(row['Taxes_val']) if row['Taxes_val'] else None,
                            chge_revenues=float(row['Chge_revenues']) if row['Chge_revenues'] else None,
                            sales_to_capital=float(row['sales_to_capital']) if row['sales_to_capital'] else None,
                            reinvestment=float(row['reinvestment']) if row['reinvestment'] else None,
                            fcff=float(row['FCFF']) if row['FCFF'] else None,
                            invested_capital=float(row['Invested_capital']) if row['Invested_capital'] else None,
                            implied_roic=float(row['Implied_ROIC']) if row['Implied_ROIC'] else None,
                            cost_of_capital=float(row['Cost_of_capital']) if row['Cost_of_capital'] else None,
                            cum_cost_of_capital=float(row['Cum_cost_of_capital']) if row['Cum_cost_of_capital'] else None,
                            preset_value=float(row['Preset_value']) if row['Preset_value'] else None,
                            stock=stock_instance,
                        )
                    else:
                        # Handle the case where stock_symbol is missing in the CSV file
                        print("Warning: stock_symbol is missing in the CSV file.")

        self.message_user(request, f'Financial data imported from {csv_instance.file_name}.')

    import_csv_data.short_description = 'Import selected CSV data'

admin.site.register(FinancialData, FinancialDataAdmin)