from django.db import models


class PriceManager(models.Manager):
    """
    Custom model manager for Price that orders all the price
    records by the field time_added (descending)

    Use it like this: Price.ordered.all() or Price.ordered.filter(...
    """

    def get_query_set(self):
        """
        overrides the basic list of objects to return one ordered by
        time_added (descending ie most recent first)
        """

        return super(PriceManager, self).get_query_set().order_by(
                "-time_added")


class Price(models.Model):
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=1)
    time_added = models.DateTimeField(auto_now_add=True)

    # model manager that's ordered by time_added descending
    ordered = PriceManager()

    objects = models.Manager()

    def __unicode__(self):
        return "%s: %f on %s" % (self.item, self.price, self.time_added)

    def get_previous_prices(self):
        """
        returns all previous price records with the same item 
        as this price instance
        """

        results = Price.ordered.filter(
                item__exact=self.item,
                time_added__lt=self.time_added)

        return results
    
    def get_previous_price(self):
        """
        returns the most recent price with the same item
        as this price instance
        """

        previous_prices = self.get_previous_prices()

        if previous_prices:
            return previous_prices[0] # most recent because of ordering

        return None # if no previous prices found

    def get_price_change(self):
        """
        returns the difference between the current price and
        the most recent price of the same item for this price
        instance
        """

        previous_price = self.get_previous_price()
        
        if previous_price:
            return self.price - previous_price.price

        return 0

    price_change = property(get_price_change, None)
