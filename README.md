Price Change
============

simple django project that demonstrates a model property
that depends on another model instance's property.

This project has a **Price** model in the *prices app*
that has a property called *price_change*. This property
depends on the previous Price instance's price property.

It makes use of a custom **model manager** that orders 
the prices according to the time they were added. The
model then has helper methods that retrieves the most
recent price that was added which has the same item
description as the current model instance.

For example to get the all the prices for an item that
were added before that item, (in a django shell) run:
```
>>> from prices.models import Price
>>> # assuming there's Price data
>>> price = Price.ordered.all()[0]
>>> price.get_previous_prices()
....
```

To get the most recent price:
```
>>> price.get_previous_price()
```

To get the price change:
```
>>> price.price_change
```

You can check how it's done [here](prices/models.py).

Installing
----------

**Clone the repo:**
```
$ git clone https://github.com/caninemwenja/price_change.git
```

**Create the database:**
```
$ cd price_change
$ ./manage.py syncdb # you can ignore the superuser stuff
```

**Run the dev server**
```
$ ./manage runserver
```
