# Volopay-API
The python file named as "main.py" contains the code for the four APIs given as the assignment by Volopay. 
To check the working of this file, the user can simply run the file in an interpreter application such as (VS Code, etc.) or Terminal.

Since this code runs is made through Flask and it runs on local host, user can simply test the API by using the given local host URL in the terminal

If running the code, in terminal - please first use this command :

flask --app main run --debug

For testing the first api /total_items:

    Use <localhost_url/total_items/start_date/end_date/department>
    
    example: "http://127.0.0.1:5000/total_items/2022-07-01/2022-09-30/Marketting"

    This will return the total seats sold in a department from start date to end date

For tesing the second api /nth_most_total_item:

    Use <localhost_url/nth_most_total_item/item_by/start_date/end_date/n>
    
    example: "http://127.0.0.1:5000/nth_most_total_item/quantity/2022-07-01/2022-09-30/3"

For third api /percentage_of_department_wise_sold_items:

     example : "http://127.0.0.1:5000/percentage_of_department_wise_sold_items/2023-04-01/2023-05-09/"
     
For foruth api :

     example: http://127.0.0.1:5000/monthly_sales/Apple/2022/
