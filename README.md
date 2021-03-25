# fertilizer-mixing

[useful calculator](https://www.omnicalculator.com/construction/fertilizer)

# Description

I want to make my own lawn fertilizer by purchasing bulk nitrogen, phosphorus, and potassium from an argriculture supplier. In order to do this I have to figure out how to scale the bulk components N-P-K ratios to the 4-1-2 ratio my lawn needs. This will ultimating end up as a script for easy tuning and formulation.

# Components ratios

## Nitrogen

My supplier has 45-0-0

## Phosphorus

My supplier has 0-20-0

## Potassium

My supplier has 0-0-60

If I were to mix these components one-to-one as is I would get a 45-20-60 or 2.25-1-3 ratio. \*Note: these are the same ratios but different concentrations this will effect coverage (more on that later). **N-P-K is percent per weight!\***

# Coverage

Coverage is usually described as pounds-of-nitrogen per 1,000 ft<sup>2</sup>.

At the time of writing this I believe my target coverage is .9 lbs per 1,000 ft<sup>2</sup>.

Given this coverage I can calculate the corresponding P and K coverages.
P should be 1/4 of .9 or .9/4 = .225 lbs per 1,000 ft<sup>2</sup>
K should be 1/2 of .9 or .9/2 = .45 lbs per 1,000 ft<sup>2</sup>

# Concentration

**I think this concentration is wrong**
P is 20/45 or .444 times less concentrated than N. We want it 1/4 or .25 times less.
K is 60/45 or 1.333 times more concentrated then N. We want it 2/4 or .5 times less
**Better concentration equations**
N concentration is 45/100 or .45 P by weight
P concentration is 20/100 or .20 P by weight
K concentration is 60/100 or .60 P by weight

# Formula

**_I'm not sure about this part!_**
N = .9 lbs per 1,000 ft<sup>2</sup>
P = .225/.44 = .511 lbs per 1,000 ft<sup>2</sup>
K = .45/1.333 = .338 lbs per 1,000 ft<sup>2</sup>
**Using new concentration**
N = .9/.45 = 2 lbs per 1,000 ft<sup>2</sup>
P = .225/.20 = 1.125 lbs per 1,000 ft<sup>2</sup>
K = .45/.60 = .75 lbs per 1,000 ft<sup>2</sup>

x = number of ft<sup>2</sup> to cover
n, p, k = pounds of component given an x

y = x/1000

n = .9 \* y
p = .511 \* y
k = .338 \* y

So if...
x = 5,000
y = 5,000/1,000 = 5

n = .9 \* 5 = 4.5 lbs
p = .511 \* 5 = 2.555 lbs
k = .338 \* 5 = 1.69 lbs
