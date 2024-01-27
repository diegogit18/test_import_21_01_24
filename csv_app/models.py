from django.db import models

class Stock(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_symbol = models.CharField(max_length=8)

    def __str__(self):
        return str(self.stock_symbol)

class Period(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs/', max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='csv') #una stock puo avere molte csv
    period = models.ManyToManyField(Period)

    def __str__(self):
        return str(self.file_name)

class Analysis(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='analyses')
    period = models.ManyToManyField(Period)

    def __str__(self):
        return str(self.title)

class FinancialData(models.Model):
    year = models.IntegerField()
    revenue = models.FloatField()
    revenue_growth_rate = models.FloatField()
    pre_tax_op_margin = models.FloatField()
    pre_tax_op_income = models.FloatField()
    taxes = models.FloatField()
    after_tax_op_income = models.FloatField()
    taxes_val = models.FloatField()
    chge_revenues = models.FloatField()
    sales_to_capital = models.FloatField()
    reinvestment = models.FloatField()
    fcff = models.FloatField()
    invested_capital = models.FloatField()
    implied_roic = models.FloatField()
    cost_of_capital = models.FloatField()
    cum_cost_of_capital = models.FloatField()
    preset_value = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    period = models.ManyToManyField(Period)

        
    def __str__(self):
        return str(self.year)  # Return a string representation of the object
    