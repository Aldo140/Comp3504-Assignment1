# Assignment-1-COMP-3504

Comp3504-Assignment1
an application to manage the inventory of different types of tools it sells.

The store owner wants to be able to modify the store's inventory by adding new tools and deleting tools. The owner also wants to be able to search the inventory for tools by tool name and by tool id. Currently, the information about tools available in the shop and suppliers is stored in two text files which are given: items.txt, and suppliers.txt. The order and type of data given in these files are: items.txt:
(id; name of tool; quantity in stock; price; supplier id)

Suppliers.txt:
(id; company name; address; sales person contact)

The owner would also like to check the quantity of each item in stock. If the quantity of each item in stock goes below 10 items, then the program should automatically generate an order line for that item. The order line will have the supplier information and the required quantity for that item (The default quantity ordered by each item = 30 minus the number of existing item). All items ordered each day should be included in an order with a randomly generated 5-digit id, and the date that was ordered. The order should be written to a text file called orders.txt. A sample order file is as follows:

###########################################################################################################
ORDER ID.:			10008
Date Ordered:			September 18, 2022

Item description:		Red Pen
Amount ordered:		39
Supplier:			GoodStationary Inc.

Item description:		A4 Papers
Amount ordered:		36
Supplier:			BestPapers

Total cost:			$1200
###########################################################################################################
ORDER ID.:			29780
Date Ordered:			September 26, 2022

Item description:		Push Pin
Amount ordered:		30		
Supplier:			WinManufacturing Inc.

Total cost:			$1200
###########################################################################################################
