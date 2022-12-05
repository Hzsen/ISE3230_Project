# Simple Optimization of apparel supply chain

author: Ryan Mark.90, Zen.Shen He.2148 

instructor: Sam  Davanloo 

 ISE 3230 

##  Project Proposal 

Every day, small businesses are tasked with managing inventory, investing in capital, and finding the best way to reduce the cost of obtaining the minimum.  Much of the time, owners are using their best judgment on how to buy inventory and manage the earnings they receive.  The beginning of a business can be the most difficult time to figure out how to best use your limited resources.  

In our project, we would help a small business formulate the best way to plan inventory to maximize profits with multiple constraints over a 12 month period. In our store, AB Clothing (ABC), we are a new sweatshirt store that is struggling to allocate resources and buy the optimal number of sweatshirts to sell.  

To start, we have decided ABC will have $\$100,000$ and zero sweatshirts to begin the business. One of the problems ABC needs to solve is how to buy sweatshirts.  

Finally, ABC does not have the space to store more than 1000 sweatshirts from one month to the next. We need to sell these goods in several cities and keep shipping costs as low as possible. Our goal is to create a Linear Program that helps ABC We want to reduce the cost of obtaining the minimum while accounting for numerous constraints on their storage, funds, and demand. 

We need to select the right manufacturer, calculate storage costs and optimize inventory, and deliver the goods to each designated sales center while keeping costs as low as possible.

## Detail

### Manufacturers

1.Vietnam Manufacturing Plant

**Manufacturing Costs**: $\$1$

**Shipping costs per quarter**: $\$10,000$



2.Local manufacturing plant in Columbus

**Manufacturing Costs**: $\$5$

**Shipping costs per quarter**: $\$1,000$



### Warehouses

1. in Columbus
   1. Storage costs: $0.8 per piece per month
   2. Storage cap: 500 pieces
2. in Cleveland
   1. Storage costs: $1 per piece per month
   2. Storage cap: 500 pieces

### Sales channels

1. online
2. local shop
   1. Columbus
   2. Cincinnati
   3. Cleveland
   4. Dayton
   5. Akron

#### Market demand by quarter

1. An order decision is made every quarter.
2. The demand is uncertain.
3. The order is placed before the demand can be known.
4. The order is placed only once a quarter.
5. There is a cost for ordering too much — the cost of papers that must be recycled.
6. There is also a cost for ordering too little — missed sales.

This scenario offers the following variables:

- x the quantity to order
- d the demand
- c the cost per unit


### Distance

The cost of road freight is \$2 per mile and fixed costs for Trucks \$500 per month.

road freight cap is 10000.

| **Distance From City** | **Distance To City** | **Distance (mi)** |
| ---------------------- | -------------------- | ----------------- |
| Columbus               | Cleveland            | 126               |
| Akron                  | Dayton               | 167               |
| Columbus               | Cincinnati           | 108               |
| Columbus               | Dayton               | 72                |
| Columbus               | Akron                | 126               |
| Akron                  | Cleveland            | 39                |
| Cincinnati             | Dayton               | 54                |
| Cincinnati             | Cleveland            | 249               |

