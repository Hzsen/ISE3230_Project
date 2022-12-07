# Project Report

author: Ryan Mark.90, Zen.Shen He.2148 

instructor: Professor Sam  Davanloo 

 ISE 3230 

December 7, 2022

##  Introduction 

Every day, small businesses are tasked with managing inventory, investing in capital, and finding the best way to maximize profits. Much of the time, owners are using their best judgment on how to buy inventory and manage the earnings they receive. The beginning of a business can be the most difficult time to figure out how to best use your limited resources. In our project, we would help a small business formulate the best way to plan inventory to maximize profits with multiple constraints over a 12-month period. IN our store, AB Clothing (ABC), we are a new sweatshirt store that is struggling to allocate resources and buy the optimal number of sweatshirts to sell. 

To start, we have decided ABC will have $1000 and zero sweatshirts to begin the business. One of the problems ABC needs to solve is how to buy sweatshirts. Their supplier implements a bundle pricing option so they get better deals for more sweatshirts they buy. Additionally, ABC has projected demand for each month for the next 12 months. Because this demand projection is not perfect, ABC likes to store at least ten sweatshirts at any given time. Finally, ABC does not have the space to store more than 100 sweatshirts from one month to the next.

Our goal is to create a Linear Program that helps ABC maximize their profits via savings on purchasing sweatshirts in bulk while accounting for numerous constraints on their storage, funds, and demand.

## Solution Ideas

To create a linear program to help ABC maximize their profits, we need to first identify the decision variables, objective function, and constraints.

The decision variables in this problem are the number of sweatshirts ABC buys each month. We can represent these variables as $x_1, x_2, ..., x_{12}$, where $x_i$ represents the number of sweatshirts ABC buys in month $i$.

The objective function is the total profit ABC makes. This profit is the difference between the total revenue from selling sweatshirts and the total cost of buying the sweatshirts. We need to find a way to model the relationship between the number of sweatshirts ABC buys and their total profit.

The constraints in this problem include the bundle pricing option from the supplier, the storage capacity, and the demand projection for each month.

We can represent the bundle pricing option as a set of inequalities that define the cost of buying a certain number of sweatshirts. For example, if the supplier offers a discount for buying more than 10 sweatshirts, we can represent this as the following inequality:

$cost(x) \leq 10 * price + (x - 10) * discounted_price$

Where $cost(x)$ is the total cost of buying $x$ sweatshirts, $price$ is the regular price of a sweatshirt, and $discounted_price$ is the discounted price of a sweatshirt.

The storage capacity constraint can be represented as an inequality that defines the maximum number of sweatshirts ABC can store at any given time:

$\sum_{i=1}^{12} x_i - \sum_{i=1}^{12} demand_i \leq 100$

Where $demand_i$ is the demand for sweatshirts in month $i$.

Finally, the demand projection constraint can be represented as a set of inequalities that defines the minimum number of sweatshirts ABC needs to have in stock in each month:

$x_i \geq demand_i + 10$

Where $x_i$ is the number of sweatshirts ABC buys in month $i$ and $demand_i$ is the demand for sweatshirts in month $i$.

To formulate the linear program, we can use the decision variables, objective function, and constraints we have defined above. The linear program can be written as follows:

Maximize $profit = \sum_{i=1}^{12} revenue_i - cost(x_i)$

Subject to:

$cost(x_i) \leq 10 * price + (x_i - 10) * discounted_price$

$\sum_{i=1}^{12} x_i - \sum_{i=1}^{12} demand_i \leq 100$

$x_i \geq demand_i + 10$

Where $profit$ is the total profit ABC makes, $revenue_i$ is the revenue from selling sweatshirts in month $i$, $cost(x_i)$ is the total cost of buying $x_i$ sweatshirts in month $i$, and $x_i$ is the number of sweatshirts ABC buys in month $i$.

This linear program can be solved using a linear programming solver to find the optimal number of sweatshirts ABC should buy in each month to maximize their profit.

## Details

#### Mathematical expressions

This scenario offers the following variables:

Let $n_i$ be net cash after month $i$,

$t_i$ be quantity in stock after month $i$,

$x_i$ be quantity of T-shirt bought at price \$30 in month $i$,

$y_i$ be quantity of T-shirt bought at price \$25 in month $i$,

$z_i$ be quantity of T-shirt bought at price \$20 in month $i$,

$d_i$ be demand of T-shirt for month $i$,

$i\in[1,12],i\in\N$.


$$
\begin{aligned}
Maximize\;z&=n_{11}+40d_{12}-25y_{12}-20z_{12}\\
s.t.\;t_1&=x_1+y_1+z_1-d_1\\
t_2&=t_1+x_2+y_2+z_2-d_2\\
t_3&=t_2+x_3+y_3+z_3-d_3\\
t_4&=t_3+x_4+y_4+z_4-d_4\\
t_5&=t_4+x_5+y_5+z_5-d_5\\
t_6&=t_5+x_6+y_6+z_6-d_6\\
t_7&=t_6+x_7+y_7+z_7-d_7\\
t_8&=t_7+x_8+y_8+z_8-d_8\\
t_9&=t_8+x_9+y_9+z_9-d_9\\
t_{10}&=t_9+x_{10}+y_{10}+z_{10}-d_{10}\\
t_{11}&=t_{10}+x_{11}+y_{11}+z_{11}-d_{11}\\
t_{12}&=t_{11}+x_{12}+y_{12}+z_{12}-d_{12}\\
10&\leq t_1,...,t_{12}\leq100\\
0&\leq x_1,...,x_{12}\leq24\\
25&\leq y_1,...,y_{12}\leq49\\
50&\leq z_1,...,z_{12}
\end{aligned}
$$

$$
\begin{aligned}
n_0&=1000\\
n_1&=n_0+40d_1-30x_1-25y_1-20z_1\\
n_2&=n_1+40d_2-30x_2-25y_2-20z_2\\
n_3&=n_2+40d_3-30x_3-25y_3-20z_3\\
n_4&=n_3+40d_4-30x_4-25y_4-20z_4\\
n_5&=n_4+40d_5-30x_5-25y_5-20z_5\\
n_6&=n_5+40d_6-30x_6-25y_6-20z_6\\
n_7&=n_6+40d_7-30x_7-25y_7-20z_7\\
n_8&=n_7+40d_8-30x_8-25y_8-20z_8\\
n_9&=n_8+40d_9-30x_9-25y_9-20z_9\\
n_{10}&=n_9+40d_{10}-30x_{10}-25y_{10}-20z_{10}\\
n_{11}&=n_{10}+40d_{11}-30x_{11}-25y_{11}-20z_{11}\\
n_1&,...,n_{11}\geq0
\end{aligned}
$$

#### Code with Description

```python
import cvxpy as cp

n = cp.Variable(12, integer = True)      #n[i] = the net profit before month i
t = cp.Variable(12, integer = True)      #t[i] = number of tshirts in storage after month i
x = cp.Variable(12, integer = True)      #x[i] = number of tshirts bought at highest price after month i
y = cp.Variable(12, integer = True)      #y[i] = number of tshirts bought at middle price after month i
z = cp.Variable(12, integer = True)      #z[i] = number of tshirts bought at lowest price after month i
d = cp.Variable(12, integer = True)      #d[i] = demand of tshirts for month i+1
u = cp.Variable((12,2), boolean = True)  #Two binary variables for each month so only one min purchase amt is used
w = cp.Variable((12,2), boolean = True)  #Two binary variables for each month so only one min purchase amt is used

# Prices of shirts -- Can be changed to fit your problem
salePrice = int(40)              #Price we sell shirt for (to customers)
smallBundle = int(30)            #Price of smallest bundle (<25 shirts)
middleBundle = int(25)           #Price of middle bundle (25 => & > 50 shirts)
largeBundle = int(20)            #Price of largest bundle (>=50 shirts)
minInventory = int(10)           #Smallest number of desired inventory at any time 
maxInventory = int(100)          #Inventory capacity
cashToStart = int(1000)          #Cash before start of month 1

constraints = []

# Demand for tshirts by month -- Can be changed to fit your problem
constraints.append(d[0] == 25)          #Demand for month 1
constraints.append(d[1] == 14)          #Demand for month 1
constraints.append(d[2] == 33)          #Demand for month 1
constraints.append(d[3] == 40)          #Demand for month 1
constraints.append(d[4] == 36)          #Demand for month 1
constraints.append(d[5] == 70)          #Demand for month 1
constraints.append(d[6] == 51)          #Demand for month 1
constraints.append(d[7] == 49)          #Demand for month 1
constraints.append(d[8] == 12)          #Demand for month 1
constraints.append(d[9] == 88)          #Demand for month 1
constraints.append(d[10] == 72)         #Demand for month 1
constraints.append(d[11] == 25)         #Demand for month 1
constraints.append(n[0] == cashToStart)               #Net Cash to start

#Inventory constraints
constraints.append(t[0] == x[0] + y[0] + z[0] - d[0])              # tshirt inventory after month 1
constraints.append(t[1] == x[1] + y[1] + z[1] - d[1])              # tshirt inventory after month 2
constraints.append(t[2] == x[2] + y[2] + z[2] - d[2])              # tshirt inventory after month 2
constraints.append(t[3] == x[3] + y[3] + z[3] - d[3])              # tshirt inventory after month 2
constraints.append(t[4] == x[4] + y[4] + z[4] - d[4])              # tshirt inventory after month 2
constraints.append(t[5] == x[5] + y[5] + z[5] - d[5])              # tshirt inventory after month 2
constraints.append(t[6] == x[6] + y[6] + z[6] - d[6])              # tshirt inventory after month 2
constraints.append(t[7] == x[7] + y[7] + z[7] - d[7])              # tshirt inventory after month 2
constraints.append(t[8] == x[8] + y[8] + z[8] - d[8])              # tshirt inventory after month 2
constraints.append(t[9] == x[9] + y[9] + z[9] - d[9])              # tshirt inventory after month 2
constraints.append(t[10] == x[10] + y[10] + z[10] - d[10])              # tshirt inventory after month 2
constraints.append(t[11] == x[11] + y[11] + z[11] - d[11])              # tshirt inventory after month 2

#Net Cash constraints
constraints.append(n[1] == n[0] + salePrice*d[0] - small*x[0] - middle*y[0] - large*z[0])       #Net Cash after month 1
constraints.append(n[2] == n[1] + salePrice*d[1] - small*x[1] - middle*y[1] - large*z[1])       #Net Cash after month 2
constraints.append(n[3] == n[2] + salePrice*d[2] - small*x[2] - middle*y[2] - large*z[2])       #Net Cash after month 3
constraints.append(n[4] == n[3] + salePrice*d[3] - small*x[3] - middle*y[3] - large*z[3])       #Net Cash after month 4
constraints.append(n[5] == n[4] + salePrice*d[4] - small*x[4] - middle*y[4] - large*z[4])       #Net Cash after month 5
constraints.append(n[6] == n[5] + salePrice*d[5] - small*x[5] - middle*y[5] - large*z[5])       #Net Cash after month 6
constraints.append(n[7] == n[6] + salePrice*d[6] - small*x[6] - middle*y[6] - large*z[6])       #Net Cash after month 7
constraints.append(n[8] == n[7] + salePrice*d[7] - small*x[7] - middle*y[7] - large*z[7])       #Net Cash after month 8
constraints.append(n[9] == n[8] + salePrice*d[8] - small*x[8] - middle*y[8] - large*z[8])       #Net Cash after month 9
constraints.append(n[10] == n[9] + salePrice*d[9] - small*x[9] - middle*y[9] - large*z[9])      #Net Cash after month 10
constraints.append(n[11] == n[10] + salePrice*d[10] - small*x[10] - middle*y[10] - large*z[10]) #Net Cash after month 11

## Variable Limits
constraints.append(t[0] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[0] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[1] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[1] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[2] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[2] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[3] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[3] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[4] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[4] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[5] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[5] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[6] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[6] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[7] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[7] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[8] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[8] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[9] >= minInventory)        #Cannot have less than 10 tshirts
constraints.append(t[9] <= maxInventory)       #Cannot have more than 100 tshirts
constraints.append(t[10] >= minInventory)       #Cannot have less than 10 tshirts
constraints.append(t[10] <= maxInventory)      #Cannot have more than 100 tshirts
constraints.append(t[11] >= minInventory)       #Cannot have less than 10 tshirts
constraints.append(t[11] <= maxInventory)      #Cannot have more than 100 tshirts

#Small bundle constraints
constraints.append(x[0] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[0] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[1] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[1] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[2] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[2] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[3] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[3] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[4] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[4] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[5] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[5] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[6] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[6] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[7] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[7] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[8] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[8] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[9] >= 0)         #Cannot buy less than 0 tshirts
constraints.append(x[9] <= 24)        #Would not buy 25+ tshirts at this price
constraints.append(x[10] >= 0)        #Cannot buy less than 0 tshirts
constraints.append(x[10] <= 24)       #Would not buy 25+ tshirts at this price
constraints.append(x[11] >= 0)        #Cannot buy less than 0 tshirts
constraints.append(x[11] <= 24)       #Would not buy 25+ tshirts at this price

#Middle bundle constraints
constraints.append(y[0] >= 0*u[0,0] + 25*u[0,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[0] <= 0*u[0,0] + 49*u[0,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[0,0] + u[0,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[1] >= 0*u[1,0] + 25*u[1,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[1] <= 0*u[1,0] + 49*u[1,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[1,0] + u[1,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[2] >= 0*u[2,0] + 25*u[2,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[2] <= 0*u[2,0] + 49*u[2,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[2,0] + u[2,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[3] >= 0*u[3,0] + 25*u[3,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[3] <= 0*u[3,0] + 49*u[3,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[3,0] + u[3,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[4] >= 0*u[4,0] + 25*u[4,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[4] <= 0*u[4,0] + 49*u[4,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[4,0] + u[4,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[5] >= 0*u[5,0] + 25*u[5,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[5] <= 0*u[5,0] + 49*u[5,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[5,0] + u[5,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[6] >= 0*u[6,0] + 25*u[6,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[6] <= 0*u[6,0] + 49*u[6,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[6,0] + u[6,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[7] >= 0*u[7,0] + 25*u[7,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[7] <= 0*u[7,0] + 49*u[7,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[7,0] + u[7,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[8] >= 0*u[8,0] + 25*u[8,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[8] <= 0*u[8,0] + 49*u[8,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[8,0] + u[8,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[9] >= 0*u[9,0] + 25*u[9,1])       #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[9] <= 0*u[9,0] + 49*u[9,1])                   #Max shirts bought for this bundle is 49 or 0
constraints.append(u[9,0] + u[9,1] == 1)                #Binary choice for either 0 or 25 as min
constraints.append(y[10] >= 0*u[10,0] + 25*u[10,1])    #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[10] <= 0*u[10,0] + 49*u[10,1])                 #Max shirts bought for this bundle is 49 or 0
constraints.append(u[10,0] + u[10,1] == 1)              #Binary choice for either 0 or 25 as min
constraints.append(y[11] >= 0*u[11,0] + 25*u[11,1])    #Min shirts bought for this bundle is 0 or >= 25
constraints.append(y[11] <= 0*u[11,0] + 49*u[11,1])     #Max shirts bought for this bundle is 49 or 0
constraints.append(u[11,0] + u[11,1] == 1)              #Binary choice for either 0 or 25 as min

#Large bundle constraints
constraints.append(z[0] >= 0*w[0,0] + 50*w[0,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[0] <= 0*w[0,0] + maxInventory*w[0,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[0,0] + w[0,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[1] >= 0*w[1,0] + 50*w[1,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[1] <= 0*w[1,0] + maxInventory*w[1,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[1,0] + w[1,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[2] >= 0*w[2,0] + 50*w[2,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[2] <= 0*w[2,0] + maxInventory*w[2,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[2,0] + w[2,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[3] >= 0*w[3,0] + 50*w[3,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[3] <= 0*w[3,0] + maxInventory*w[3,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[3,0] + w[3,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[4] >= 0*w[4,0] + 50*w[4,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[4] <= 0*w[4,0] + maxInventory*w[4,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[4,0] + w[4,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[5] >= 0*w[5,0] + 40*w[5,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[5] <= 0*w[5,0] + maxInventory*w[5,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[5,0] + w[5,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[6] >= 0*w[6,0] + 40*w[6,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[6] <= 0*w[6,0] + maxInventory*w[6,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[6,0] + w[6,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[7] >= 0*w[7,0] + 40*w[7,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[7] <= 0*w[7,0] + maxInventory*w[7,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[7,0] + w[7,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[8] >= 0*w[8,0] + 40*w[8,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[8] <= 0*w[8,0] + maxInventory*w[8,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[8,0] + w[8,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[9] >= 0*w[9,0] + 40*w[9,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[9] <= 0*w[9,0] + maxInventory*w[9,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[9,0] + w[9,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[10] >= 0*w[10,0] + 40*w[10,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[10] <= 0*w[10,0] + maxInventory*w[10,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[10,0] + w[10,1] == 1)                    #Binary choice for either 0 or 50 as min
constraints.append(z[11] >= 0*w[11,0] + 40*w[11,1])           #Min shirts bought for this bundle is 0 or >= 50
constraints.append(z[11] <= 0*w[11,0] + maxInventory*w[11,1])  #Max shirts is 0 if not chosen or maximum we can hold
constraints.append(w[11,0] + w[11,1] == 1)                    #Binary choice for either 0 or 50 as min

#Money constraints
constraints.append(n[0] >= 0)         #Cannot have negative money
constraints.append(n[1] >= 0)         #Cannot have negative money
constraints.append(n[2] >= 0)         #Cannot have negative money
constraints.append(n[3] >= 0)         #Cannot have negative money
constraints.append(n[4] >= 0)         #Cannot have negative money
constraints.append(n[5] >= 0)         #Cannot have negative money
constraints.append(n[6] >= 0)         #Cannot have negative money
constraints.append(n[7] >= 0)         #Cannot have negative money
constraints.append(n[8] >= 0)         #Cannot have negative money
constraints.append(n[9] >= 0)         #Cannot have negative money
constraints.append(n[10] >= 0)        #Cannot have negative money
constraints.append(n[11] >= 0)        #Cannot have negative money

obj_func = n[11] + 40*d[11] - 30*x[11] - 25*y[11] - 20*z[11]

problem = cp.Problem(cp.Maximize(obj_func), constraints)
problem.solve(solver=cp.GUROBI, verbose = True, qcp = True)

print("obj_func = ")
print(obj_func.value)
print("n = ")
print(n.value)
print("t = ")
print(t.value)
print("x = ")
print(x.value)
print("y = ")
print(y.value)
print("z = ")
print(z.value)
print("d = ")
print(d.value)
```

##### Running Result for the code

```markdown
===============================================================================
                                     CVXPY                                     
                                    v1.1.18                                    
===============================================================================
(CVXPY) Dec 05 10:02:00 PM: Your problem has 120 variables, 168 constraints, and 0 parameters.
(CVXPY) Dec 05 10:02:00 PM: It is compliant with the following grammars: DCP, DQCP
(CVXPY) Dec 05 10:02:00 PM: (If you need to solve this problem multiple times, but with different data, consider using parameters.)
(CVXPY) Dec 05 10:02:00 PM: CVXPY will first compile your problem; then, it will invoke a numerical solver to obtain a solution.
-------------------------------------------------------------------------------
                                  Compilation                                  
-------------------------------------------------------------------------------
(CVXPY) Dec 05 10:02:00 PM: Compiling problem (target solver=GUROBI).
(CVXPY) Dec 05 10:02:00 PM: Reduction chain: FlipObjective -> CvxAttr2Constr -> Qp2SymbolicQp -> QpMatrixStuffing -> GUROBI
(CVXPY) Dec 05 10:02:00 PM: Applying reduction FlipObjective
(CVXPY) Dec 05 10:02:00 PM: Applying reduction CvxAttr2Constr
(CVXPY) Dec 05 10:02:00 PM: Applying reduction Qp2SymbolicQp
(CVXPY) Dec 05 10:02:00 PM: Applying reduction QpMatrixStuffing
(CVXPY) Dec 05 10:02:01 PM: Applying reduction GUROBI
(CVXPY) Dec 05 10:02:01 PM: Finished problem compilation (took 3.253e-01 seconds).
-------------------------------------------------------------------------------
                                Numerical solver                               
-------------------------------------------------------------------------------
(CVXPY) Dec 05 10:02:01 PM: Invoking solver GUROBI  to obtain a solution.
Set parameter QCPDual to value 1
Gurobi Optimizer version 9.5.2 build v9.5.2rc0 (mac64[x86])
Thread count: 4 physical cores, 8 logical processors, using up to 8 threads
Optimize a model with 168 rows, 120 columns and 343 nonzeros
Model fingerprint: 0x8cc36e06
Variable types: 0 continuous, 120 integer (48 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+02]
  Objective range  [1e+00, 4e+01]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 1e+03]
Presolve removed 108 rows and 48 columns
Presolve time: 0.00s
Presolved: 60 rows, 72 columns, 172 nonzeros
Variable types: 0 continuous, 72 integer (19 binary)
Found heuristic solution: objective -6710.000000

Root relaxation: objective -8.800000e+03, 39 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 -8800.0000    0    5 -6710.0000 -8800.0000  31.1%     -    0s
H    0     0                    -7680.000000 -8800.0000  14.6%     -    0s
H    0     0                    -7725.000000 -8800.0000  13.9%     -    0s
H    0     0                    -7775.000000 -8800.0000  13.2%     -    0s
H    0     0                    -7870.000000 -8800.0000  11.8%     -    0s
H    0     0                    -7895.000000 -8800.0000  11.5%     -    0s
*    0     0               0    -8075.000000 -8075.0000  0.00%     -    0s

Cutting planes:
  Cover: 3
  Implied bound: 10
  MIR: 4
  StrongCG: 1
  Flow cover: 7

Explored 1 nodes (58 simplex iterations) in 0.05 seconds (0.00 work units)
Thread count was 8 (of 8 available processors)

Solution count 7: -8075 -7895 -7870 ... -6710
No other solutions better than -8075

Optimal solution found (tolerance 1.00e-04)
Best objective -8.075000000000e+03, best bound -8.075000000000e+03, gap 0.0000%
-------------------------------------------------------------------------------
                                    Summary                                    
-------------------------------------------------------------------------------
(CVXPY) Dec 05 10:02:01 PM: Problem status: optimal
(CVXPY) Dec 05 10:02:01 PM: Optimal value: 8.075e+03
(CVXPY) Dec 05 10:02:01 PM: Compilation took 3.253e-01 seconds
(CVXPY) Dec 05 10:02:01 PM: Solver (including time spent in interface) took 6.654e-02 seconds
obj_func = 
8075.0
n = 
[1000. 1125. 1060. 1380. 1980. 2420. 3620. 4440. 5220. 5075. 6635. 7875.]
t = 
[10. 11. 17. 10. 14. 10. 10. 10. 13. 10. 10. 15.]
x = 
[-0. -0. -0. -0. -0. -0. -0. -0.  0. -0. -0.  0.]
y = 
[35. 25. -0. -0. -0. -0. -0. -0. 25. -0. -0.  0.]
z = 
[ 0. -0. 50. 50. 50. 80. 61. 59. -0. 98. 82. 40.]
d = 
[25. 14. 33. 40. 36. 70. 51. 49. 12. 88. 72. 25.]
```

#### Optimality Analysis



## Appendix 

#### Appendix A:	

Link to the YouTube video

[Group 18 Final Project - YouTube](https://www.youtube.com/watch?v=69YxvaVlXcw)

#### Appendix B: 

Create Github with file and add link



#### Appendix C (Tasks):

- Ryan - Project Proposal
- Ryan - Python Code
- Ryan - YouTube Video
- Zhengshen Project Report
