### 1. Create a definitive problem statement to be solved with data analytics.  
I would like to review electric vehicle (EV) data and compare it to gas vehicles to see if they are cost effective as advertise for the average driver and if so, show their return of investment. With the dataset that I have, I want to do a cost analysis for all the available cars in the dataset in order to show how cost can vary from vehicle to vehicle.

### 2. Provide your datasets.
### Provide an explanation of the datasets you submit.
- ### Alternative_Fuel_Vehicles_US.csv: 
    - Has a breakdown of all EVs/hybrids and their estimated ranges.
- ### Kelley Blue Book API (http://developer.kbb.com/#!/data/1-Default)
    - Thinking about potentially using this API if I am unable to find alternative datasets to enrich/combine with my current dataset. I would use the API to obtain additional car specs and cost(s) to get a better idea of total cost and ROI.
### 3. Describe your plan on how to use this data to answer your problem 
statement. 

I will clean the data and remove commercial vehicles off the dataset.
I plan to use the dataset to calculate how much monthly you would pay with EVs monthly based on the average rates for charging for each individual vehicle. In the case of hybrid's or plug in hybrid's I will calculate cost based on range and add gas cost.

If I am able to find a dataset with additional cost(s) and specs for the vehicles, I will add a column to add those data points in.

I currently plan to import all the data into a SQL table which I would connect Tableau with. 