# A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
# Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    count = 0
    typeList = []
    # print("ticket sales: ", ticket_sales)
    # print("ticket_sales.items: ", ticket_sales.items())
    for ticket_type, ticket in ticket_sales.items():
        # print(ticket_sales[ticket])
        typeList.append(ticket_type)
        count += ticket
    # print("Ticket Types:", typeList)
    return count
    pass

# Example Usage:

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
