# Flairbnb

### Visualize the data: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
Three graphs were provided. This was done using the Python package PANDAS to parse the csv files and generate the data sets/graphs. Price vs Number Accommodated, Price vs. Month, and Frequency of Available Listings by Month were all graphed by using matplotlib. The code for this is found in /Python/DataAnalysis.py.

### Price estimation: Given the geo-location (latitude and longitude) of a new property, estimate the weekly average income the homeowner can make with Airbnb.
This was done using TensorFlow to create a multivariable equation for price estimates given a location. It uses latitude and longitude as inputs and price as the output. After millions of iterations of training, the equation that most closely matches the data points was ```price = 0.88093132*latitude + (-1.81391311)*longitude + 0.076020```. The code for this is found in /Python/MLOptimization.

### Bookings optimization: Given the geo-location (latitude and longitude) of a property, what is the ideal price per night that will yield maximum bookings or revenue?
This was done by subtracting a set amount of money from the price estimation. The logic was that if you undercut your competition by a certain amount, your listings will be more popular among consumers and thus maximize bookings.

### Animate: Add an animation to your visualization.
The carousel provides an animation between the highlights of the webpage. It takes a few seconds for the animation to show. The front end was created using Bootstrap and HTML/CSS/Javascript.

### Investment: If I have $100 million to invest, where in San Francisco should I buy properties so I can maximize my returns with Airbnb? When will I break even?
Calculated based on which location provides the most money per night, which was calculated using machine learning. The average cost per house was estimated using zillow.com. The $100 million was divided among houses and then the time it takes to break even was based upon how much money the houses will produce every day. However, to accommodate unforseen circumstances and time in between guests staying over, I rounded up to 17 years. 

### Popularity: Can you identify the neighborhood that averages the most positive reviews?
This was done using NLTK and its sentiment analysis. Each review was given a score that combined positive, neutral, and negative sentiments for an overall score. The review was mapped to its appropriate neighborhood. Then the average compound score and the proportion of positive reviews was calculated. The code for this is found in /Python/Sentiment
