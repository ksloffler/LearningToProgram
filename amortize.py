"""Amortization"""
import re
from decimal import Decimal

def main():
    """this is the main function"""
    file_name = input('Please choose a file name: ')
    loan_amount = input("please enter loan amount, example $20,000.00 ")
    interest_amount = input("please enter interest rate as a percent, such as 3.99% ")
    length_of_loan = input("please enter number of months ")
    begining_date = input("please enter begining date as month/year" +
                          ", example: 01/2010 ")
    mortgagee = input("please enter name of mortgagee: first name last name ")
    mortgagor = input("please enter name of mortgagor: first name last name ")
    mortgagee = mortgagee.title()
    mortgagor = mortgagor.title()
    print(loan_amount, interest_amount, length_of_loan, begining_date, mortgagee, mortgagor)

    loan_amount = float(re.sub("\$|,", "", loan_amount))

    interest_amount = float(interest_amount.replace("%", ""))/100

    length_of_loan = int(length_of_loan)

    date = re.split("/", begining_date)
    date = {'month':int(date[0]), 'year':int(date[1]), }

    payments = amortize(loan_amount, interest_amount, length_of_loan)
    csv_output = ['Mortgagee:, %s,\nMortgagor:, %s\n\n' % (mortgagee, mortgagor)]
    csv_output.append("payment #, payment, interest, principal, remaining, interest paid")

    for paynum, payment in enumerate(payments):
        csv_output.append("%s, %.2f, %.2f, %.2f, %.2f, %.2f" % (paynum, payment['payment_amt'], payment['interest'],
                                                      payment['principle'], payment['rAmt'], payment['total_interest']))

    open(file_name+".csv", "w+").write("\n".join(csv_output))
    
def amortize(amount, interest, months):
    """this function will create an
    amortization schedule"""
    remaining_amount = amount
    payment_amount = calculate_payment(amount, interest, months)
    print(payment_amount)

    payments_information = []
    total_interest = 0
    
    while months-1:
        interest_amt = calculate_interest(remaining_amount, interest)
        total_interest += interest_amt
        principle = payment_amount - interest_amt
        remaining_amount -= principle
        #print(payment_amount)
        #print(interest)
        #print(remaining_amount)
        #print(principle)
        #print(remaining_amount - principle)
        #create dictionary with payment information
        payment = {'interest':interest_amt, 'principle':principle,
                   'rAmt':remaining_amount, 'payment_amt':payment_amount,
                   'total_interest':total_interest}
        #append payment information dictionary to
        #payments_information
        payments_information.append(payment)
        months -= 1

    for pay_number, payment in enumerate(payments_information):
        print("Payment: %s\n\t--Payment:%s\n\t--Principal:%s\n\t--Interest:%s\n\t--Balance:%s\n\t--Total Interest Paid:%s\n\n" % (
              pay_number, payment_amount, payment['principle'], payment['interest'], payment['rAmt'], total_interest))
    #print('\n'.join([str(payment) for payment in payments_information]))

    return payments_information

def calculate_payment(amount, interest, months):
    """this function will calculate
    monthly payments"""
    if not interest:
        return amount/months
    
    return (((amount*interest)/12)*(1+interest/12)**months)/((1+interest/12)**months-1)

def calculate_interest(remaining_amount, interest):
    """this fundtion will calculate the
    remaining amount"""

    return remaining_amount*interest*(1/12)

if __name__ == "__main__":
    main()

 


