print('Please enter the number of tickets to sell:')
tickets = int(input())
ticket_total = 0
buyers = 0
while ticket_total < tickets:
    print('Please enter the number of tickets to purchase:')
    ticket_buy = int(input())
    if ticket_buy > 0 and ticket_buy <= 4 and ticket_buy <= tickets:
        tickets = tickets - ticket_buy
        print(tickets, 'tickets remaining.')
        
    elif ticket_buy < 0 or ticket_buy >= 4 or ticket_buy > tickets:
        print("I'm sorry but I can't sell you that many.")
        
    if ticket_buy == ticket_buy:
        buyers += 1
        
    if ticket_buy < 1 or ticket_buy > 4:
        buyers -= 1
        
    if tickets == 0:
        print('Total buyers:', buyers)
