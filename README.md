# DEV annotations

## Automation testing
execute command
> pytest

## Run from command
on 'exec' folder path, run command:
> PriceBasket Soup Soup Bread Apples

output example:
```
Subtotal 3.1
Bread 50% off: -€0.4
Apples 10% off: -€0.1
Total 2.6
Soup
Soup
Bread
Apples
```

## Run from Pycharm IDE
Add 'src.PriceBasket.py' path to script path field and add the follow parameters:
> Soup Milk Coffe

output example:
```
Item 'Coffe' doesn't exist on system items list
Subtotal 1.95
(no offers available)
Total 1.95
Soup
Milk
```


## Create executable file
Command:
> pyinstaller --onefile PriceBasket.py --distpath exec --workpath exec --specpath exec


