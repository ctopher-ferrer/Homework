# SECTION 07 HW 
<br>

# Section 7.1 
## Question 1: Using EVregistry, Write a query to select the `ModelYear`, `Make`, and `Model` off all of the vehicles in the registry.
```SQL

select ModelYear, Make, Model 
from evRegistry

```
## Question 2: Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, `ElectricVehicleType`. 
```SQL

select distinct ElectricVehicleType 
from evRegistry

```

## Question 3: Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry. 
```SQL

select *
from evRegistry
where ElectricVehicleType = 'Battery Electric Vehicle (BEV)'

```
## Question 4: Using the EVRegistry, wirte a query that returns the `Make` and `Model` of all of the EV's that have a BaseMSRP between 20000 and 35000?  
```SQL

select Make, Model, BaseMSRP
from evRegistry
where BaseMSRP >= 20000 and BaseMSRP <= 35000

```
# Section 7.2
## Question 1: Using EVRegistry, write a query to find a record  where the `City` attribute is NULL. Return all of the available columns. 
```SQL

select *
from evRegistry
where City is null

```
## Question 2: Write a query to find the `make`, `model`, and `ElectricVehicleType` where the VIN number has  that ends in '3E1EA1J'.
```SQL

select Make, Model, ElectricVehicleType, VIN
from evRegistry
where VIN like '%3E1EA1J'

```

## Question 3: Select the `ModelYear`, `make`, `model`, `ElectricVehicleType`, and `range` of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest. 
```SQL

select ModelYear, Make, Model, ElectricVehicleType, ElectricRange
from evRegistry
where Make in ('CHEVROLET','TESLA')
order by make, ModelYear DESC

```
## Question 4: Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records. 
```SQL

Select stationId, count(stationId) as 'Count'
from EVCharging
group by stationId
order by count(stationId) desc
LIMIT 5

```
## Question 5: Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. 
```SQL

Select userId, max(chargeTimeHrs) as 'maxTime', 
min(chargeTimeHrs) as 'minTime'
from EVCharging
where chargeTimeHrs > 0.5
group by userId
ORDER BY 2,3

```
# Section 7.3
## Question 1: Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.
```SQL

select weekday, round(AVG(chargeTimeHrs),2) as AvgChargingTime
from EVCharging
group by weekday
order by round(AVG(chargeTimeHrs),2) desc

```
ANSWER: Wednesday has the highest average charging time
<br>

## Question 2: Using, EV charging, Find the total power consumed from charging EV's by each User. Return the `userId` and name the calculated column, `totalPower`. Round the answer to 2 deciaml points and list the out put in highest to lowest order. Limit the order to the top 15 users. 
```SQL

select userId, round(sum(kwHTotal),2) as totalPower
from EVCharging
group by userId
order by round(sum(kwHTotal),2) DESC
limit 15

```

## Question 3: Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return `type Facility` and name the calculated column `numStation`. Order the result set from highest to lowest number of charging stations.  
```SQL

select b.typeFacility ,count(distinct a.stationId) as numStation
from factCharge as a
join dimFacility as b on b.FacilityKey = a.facilityID
group by b.typeFacility
order by count(a.stationId) desc

```
## Question 4: In your own words, Briefly explain Primary Keys and Foreign Keys. 
<br>
 Primary Keys are unique values that identify each row/record in a table. They are never NULL values. A Foreign Key is a reference to another tables Primary Key which can be used to join/connect the tables together.

<br>

## Question 5: Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. HINT: USE `HAVING`
```SQL

select userId, min(chargetimeHrs) as minTime, max(chargetimeHrs) as maxTime
from EVCharging
GROUP By userId
HAVING min(chargeTimeHrs) > 1

```