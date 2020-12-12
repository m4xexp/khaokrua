from DBHelper import DBHelper
from helper_functions import *
#This file will contain all API functions calls exposed to outside world for users to use

# function about Product
def create_product(products, code, name, units):
    result = products.create(code, name, units)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Create Success.')
    return result #send result for caller program to use

def read_product(products, code):
    result = products.read(code) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_product(products, code, newName, newUnits):
    result = products.update(code, newName, newUnits) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Update Success.')
    return result #send result for caller program to use

def delete_product(products, code):
    result = products.delete(code)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Product Delete Success.')
    return result #send result for caller program to use

def report_list_products(products):
    result = products.dump()
    #printDictInCSVFormat(result, ('Code',), ('Name', 'Units'))
    print (result)
    return result #send result for caller program to use

# function about Customer 
def create_customer(customers, customerCode, customerName, address, creditLimit, country):
    result = customers.create(customerCode, customerName, address, creditLimit, country)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Create Success.')
    return result #send result for caller program to use

def read_customer(customers, customerCode):
    result = customers.read(customerCode) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_customer(customers, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
    result = customers.update(customerCode, newCustomerName, newAddress, newCreditLimit, newCountry) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Update Success.')
    return result #send result for caller program to use

def delete_customer(customers, customerCode):
    result = customers.delete(customerCode)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Customer Delete Success.')
    return result #send result for caller program to use

def report_list_all_customers(customers):
    result = customers.dump()
    printDictInCSVFormat(result, ('Customer Code',), ('Name', 'Address','Credit Limit', 'Country'))
    return result #send result for caller program to use

# function about PaymentMethod
def create_payment_method(paymentMethods, code, name):
    result = paymentMethods.create(code, name)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('PaymentMethod Create Success.')
    return result #send result for caller program to use

def read_payment_method(paymentMethods, code):
    result = paymentMethods.read(code) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_payment_method(paymentMethods, code, newName):
    result = paymentMethods.update(code, newName) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('PaymentMethod Update Success.')
    return result #send result for caller program to use

def delete_payment_method(paymentMethods, code):
    result = paymentMethods.delete(code)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('PaymentMethod Delete Success.')
    return result #send result for caller program to use

def report_list_payment_method(paymentMethods):
    result = paymentMethods.dump()
    #printDictInCSVFormat(result, ('Code',), ('Name', 'Units'))
    print (result)
    return result #send result for caller program to use

# function about Invoice 
def create_invoice(invoices, invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList):
    if invoiceDate == None:
        invoiceDate = 'null'
    else:
        invoiceDate = "'" + invoiceDate + "'"
    if dueDate == None:
        dueDate = 'null'
    else:
        dueDate = "'" + dueDate + "'"
    result = invoices.create(invoiceNo, invoiceDate, customerCode, dueDate, invoiceLineTuplesList)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Create Success.')
    return result #send result for caller program to use

def read_invoice(invoices, invoiceNo):
    result = invoices.read(invoiceNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_invoice(invoices, invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList):
    if newInvoiceDate == None:
        newInvoiceDate = 'null'
    else:
        newInvoiceDate = "'" + newInvoiceDate + "'"
    if newDueDate == None:
        newDueDate = 'null'
    else:
        newDueDate = "'" + newDueDate + "'"
    result = invoices.update(invoiceNo, newInvoiceDate, newCustomerCode, newDueDate, newInvoiceLineTuplesList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Update Success.')
    return result #send result for caller program to use

def delete_invoice(invoices, invoiceNo):
    result = invoices.delete(invoiceNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Delete Success.')
    return result #send result for caller program to use

def update_invoice_line(invoices, invoiceNo, productCode, newQuantity, newUnitPrice):
    result = invoices.update_invoice_line(invoiceNo, productCode, newQuantity, newUnitPrice) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Update Success.')
    return result #send result for caller program to use

def delete_invoice_line(invoices, invoiceNo, productCode):
    result = invoices.delete_invoice_line(invoiceNo, productCode) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Invoice Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_invoices(invoices, customers, products):
    # Will dump all invoices data and return 1 dictionary as a result (with header and line item joined).  
    # Please show the customer name and product name also. 
    # A helper function such as def print_tabular_dictionary(tabularDictionary) can then be called to print this in a tabular (table-like) form with column headings and data. 

    db = DBHelper()
    data, columns = db.fetch ('SELECT i.invoice_no as "Invoice No", i.date as "Date" '
                              ' , i.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , i.due_date as "Due Date", i.total as "Total", i.vat as "VAT", i.amount_due as "Amount Due" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , ili.quantity as "Quantity", ili.unit_price as "Unit Price", ili.extended_price as "Extended Price" '
                              ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code '
                              '  JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '  JOIN product p ON ili.product_code = p.code '
                              ' ')
    #print (result)
    result = row_as_dict(data, columns)
    printDictInCSVFormat(result, ('receipt No',), ('Date', 'Customer Code', 'Customer Name','Due Date','Total','VAT','Amount Due'
                                                , 'Product Code', 'Product Name', 'Quantity', 'Unit Price', 'Extended Price'))
    return result #send result for caller program to use


def report_products_sold(invoices, products, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of in products sold in the given date range in tabular format of: Product Code, Product Name, Total Quantity Sold, Total Value Sold. Here, (product code) will be unique. 
    # And 2) a second dictionary of the footer will also be returned containing: t the end also show the sum of Total Value Sold.  
    db = DBHelper()
    data, columns = db.fetch ('SELECT p.code as "Code", ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY p.code, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Product Code','Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Value Sold',))
    return result, result2

def report_customer_products_sold_list(invoices, products, customers, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list of customers and list the products sold to them in the given date range in this format:  Customer Code, Customer Name, Product Code,  Product Name, Invoice No, Invoice Date, Quantity Sold, Value Sold. Here, (customer code, product code, invoice no) will be unique.  
    # And 2) a second footer dictionary showing:  At the end also show the sum of Quantity Sold and sum of Value Sold.
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.customer_code, c.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , i.invoice_no as "Invoice No" '
                              ' , SUM(ili.quantity) as "Quantity Sold", SUM(ili.extended_price) as "Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY i.customer_code, c.customer_code, c.name, i.invoice_no, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.quantity) as "Quantity Sold", SUM(ili.extended_price) as "Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Invoice No', 'Quantity Sold', 'Value Sold'))
    printDictInCSVFormat(result2, (None), ('Quantity Sold','Value Sold'))
    return result.values(), result2

def report_customer_products_sold_total(invoices, products, customers, dateStart, dateEnd):
    # Will return 2 dictionaries: 
    # 1) a dictionary as list customers and the total number and value of products sold to them in the given date range in this format:  Customer Code, Customer Name, Product Code,  Product Name, Total Quantity Sold, Total Value Sold. Here (customer code, product code) will be unique.
    # And 2) a second footer dictionary showing: t the end also show the sum of Total Quantity Sold, sum of Total Value Sold.
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.customer_code, c.customer_code as "Customer Code", c.name as "Customer Name" '
                              ' , ili.product_code as "Product Code", p.name as "Product Name" '
                              ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' GROUP BY i.customer_code, c.customer_code, c.name, i.invoice_no, ili.product_code, p.name ')
    result = row_as_dict(data, columns)
    data, columns = db.fetch ('SELECT 0 as "Footer", SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.extended_price) as "Total Value Sold" '
                              ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                              '   JOIN customer c ON i.customer_code = c.customer_code '
                              '   JOIN product p ON ili.product_code = p.code '
                              ' WHERE i.date between \'' + dateStart + '\' and \'' + dateEnd + '\' '
                              ' ')
    result2 = row_as_dict(data, columns)

    printDictInCSVFormat(result, (None), ('Customer Code','Customer Name', 'Product Code', 'Product Name', 'Total Quantity Sold', 'Total Value Sold'))
    printDictInCSVFormat(result2, (None), ('Total Quantity Sold','Total Value Sold'))
    return result.values(), result2


# function about Receipt
def create_receipt(receipts, receiptNo, date, customerCode, paymentCode, paymentRef, remarks, receiptLineTuplesList):
    if date == None:
        date = 'null'
    else:
        date = "'" + date + "'"
    if paymentCode == None:
        paymentCode = 'null'
    else:
        paymentCode = "'" + paymentCode + "'"
    if paymentRef == None:
        paymentRef = 'null'
    else:
        paymentRef = "'" + paymentRef + "'"
    if remarks == None:
        remarks = 'null'
    else:
        remarks = "'" + remarks + "'"
    result = receipts.create(receiptNo, date, customerCode, paymentCode, paymentRef, remarks, receiptLineTuplesList)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Create Success.')
    return result #send result for caller program to use

def read_receipt(receipts, receiptNo):
    result = receipts.read(receiptNo) #returns tuple of (error dict, data dict)
    if result[0]['Is Error']: #in case error
        print(result[0]['Error Message'])
    else:
        print(result[1])
    return result #send result for caller program to use

def update_receipt(receipts, receiptNo, newReceiptDate, newCustomerCode, newPaymentCode, newPaymentRef, newRemarks, newReceiptLineTuplesList): #
    if newReceiptDate == None:
        newReceiptDate = 'null'
    else:
        newReceiptDate = "'" + newReceiptDate + "'"
    if newPaymentCode == None:
        newPaymentCode = 'null'
    else:
        newPaymentCode = "'" + newPaymentCode + "'"
    if newPaymentRef == None:
        newPaymentRef = 'null'
    else:
        newPaymentRef = "'" + newPaymentRef + "'"
    if newRemarks == None:
        newRemarks = 'null'
    else:
        newRemarks = "'" + newRemarks + "'"
    result = receipts.update(receiptNo, newReceiptDate, newCustomerCode, newPaymentCode, newPaymentRef, newRemarks, newReceiptLineTuplesList) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Update Success.')
    return result #send result for caller program to use

def delete_receipt(receipts, receiptNo):
    result = receipts.delete(receiptNo)#returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Delete Success.')
    return result #send result for caller program to use

def update_receipt_line(receipts, receiptNo, invoiceNo, newAmountPaidHere):
    result = receipts.update_receipt_line(receiptNo, invoiceNo, newAmountPaidHere) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Line Item Update Success.')
    return result #send result for caller program to use

def delete_receipt_line(receipts, receiptNo, invoiceNo):
    result = receipts.delete_receipt_line(receiptNo, invoiceNo) #returns error dictionary
    if result['Is Error']: #if error
        print(result['Error Message'])
    else:
        print('Receipt Line Item Delete Success.')
    return result #send result for caller program to use

def report_list_all_receipts(receipts, invoices, customers):
    # Will dump all receipts data and return 1 dictionary as a result (with header and line item joined).  
    # Please show the customer name and product name also. 
    # A helper function such as def print_tabular_dictionary(tabularDictionary) can then be called to print this in a tabular (table-like) form with column headings and data. 

    db = DBHelper()
    data, columns = db.fetch ('SELECT r.receipt_no as "Receipt No", r.date as "Date" '
                              ' , r.customer_code as "Customer Code", c.name as "Customer Name", r.payment_code as "Payment Method", r.payment_ref as "Payment Reference" '
                              ' , r.remarks as "Remarks", r.total_received as "Total Received"'
                              ' , rli.invoice_no as "Invoice No"'
                              ' , i.date as "Invoice Date", rli.amount_paid_here as "Amount Paid Here"'
                              '  FROM receipt r '
                              '  JOIN customer c ON r.customer_code = c.customer_code '
                              '  JOIN receipt_line_item rli ON r.receipt_no = rli.receipt_no '
                              '  JOIN invoice i ON rli.invoice_no = i.invoice_no ' )
                              
    #print (result)
    printFunc(data, columns)
    return data #result #send result for caller program to use

def report_unpaid_invoices (invoices, customers, receipts):
    db = DBHelper()
    data, columns = db.fetch('SELECT "Invoice No", i.date as "Invoice Date" '
		                     '  , c.name as "Customer Name", i.amount_due AS "Invoice Amount Due" '
		                     '  , "Invoice Amount Received", i.amount_due - "Invoice Amount Received" AS "Invoice Amount Not Paid" '
                             ' FROM( SELECT rli.invoice_no as "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received" '
	                         '  FROM receipt_line_item as rli '
	                         '  GROUP BY rli.invoice_no ) as li '
                             '  JOIN invoice as i '
	                         '   ON li."Invoice No" = i.invoice_no '
                             ' INNER JOIN customer as c '
	                         '   ON i.customer_code = c.customer_code')
    result = row_as_dict(data, columns)

    data1, columns1 = db.fetch ('SELECT SUM(i.amount_due - "Invoice Amount Received") AS "Total Dept" '
                              'FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received" '
	                          '  FROM receipt_line_item as rli '
	                          ' GROUP BY rli.invoice_no ) as li '
                              ' INNER JOIN invoice as i '
	                          '  ON li."Invoice No" = i.invoice_no ')
  
    result = row_as_dict(data, columns)
    printDictInCSVFormat(result, ('Invoice No',), ('Invoice Date', 'Customer Name', 'Invoice Amount Due', 'Invoice Amount Received', 'Invoice Amount Not Paid'))
    print(columns1[0]+':',data1[0][0])



    