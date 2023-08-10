-- This file contains trigger
-- whenever INSERT operation is done to the order table it subtracts quantity from items
CREATE TRIGGER decreate_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
