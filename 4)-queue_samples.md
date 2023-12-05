Let's say we have a queue of our taxes to pay 😟💸. Pythonically talking: 

` my_taxes = Queue(month, amount) `

and we need to keep track of 3 months of our taxes:  

In january we pay: 100 
` my_taxes.enqueue(jan, 100)`

In February we pay: 200 
` my_taxes.enqueue(feb, 100)`

In March we pay: 300
` my_taxes.enqueue(mar, 300)`

the next month that we pay, we need to delete the oldest month in our records

so, in our taxes queue we have, 

`❌100, 200, 300`   
and january must to be deleted from our records, because it was the first 


so...   
`my_taxes.dequeue(jan, 100)`

so we can add the next month of the year, that is April

`my_taxes.enqueue(apr, 300)`

so our queue finally looks like this:   
`200, 300, ✅300`


## Operations
and how we make them possible: 

- ✅
**enqueue(value)** = queue.append(value)

- ❌**dequeue(value)** = queue.pop(value)

- 📏**size** length = len(queue)

- **empty** if len(queue) == 0