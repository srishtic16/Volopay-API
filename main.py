from flask import Flask, jsonify
import csv
from collections import defaultdict


app = Flask(__name__)

 
# opening the CSV file
with open(r"C:\Users\HP\Downloads\data (1).csv", mode ='r') as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  data=list(csvFile)
 
#deleting the heading row
data.pop(0)


#converting date to a usable format of "list"
for x in data :
   year= int(x[1][:4])
   mon=int(x[1][5:7])
   day=int(x[1][8:10])
   hour=int(x[1][11:13])
   minutes=int(x[1][14:16])
   sec=int(x[1][17:19])

   x[1]=[year, mon, day, hour, minutes, sec]


#sort data in descending order of dates and time
data=sorted(data, key=lambda x:  [x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], x[1][5]], reverse=True)



@app.route('/')
def hello_world():
    return 'Hello, World!'


''' First API : gives the total items or seats sold for a given period of time '''

@app.route('/total_items/<string:startdate>/<string:enddate>/<string:dept>')
def total_items(startdate, enddate, dept):
   seats=0
  
   startdate = [int(startdate[:4]), int(startdate[5:7]), int(startdate[8:10])]
   enddate =  [int(enddate[:4]), int(enddate[5:7]), int(enddate[8:10])]
  
   for i in data:
      
      if (startdate <=i[1][:3]<= enddate) :
        #print(startdate, enddate, i[1][:3], enddate>=i[1][:3]>=startdate)
        if i[3] == dept:
            seats+=int(i[5])

   return str(seats)

'''Second API : gives the nth most sold items by quantity and/or price factor'''

@app.route('/nth_most_total_item/<string:item_by>/<string:startdate>/<string:enddate>/<int:n>')
def nth_most_total_item(item_by, startdate, enddate, n):
   
   dic= defaultdict(lambda : 0)

   startdate = [int(startdate[:4]), int(startdate[5:7]), int(startdate[8:10])]
   enddate =  [int(enddate[:4]), int(enddate[5:7]), int(enddate[8:10])]

   

   if item_by == "quantity":
      for i in range(len(data)):
         if enddate<=data[i][1][:3]>=startdate:
            s_index=i
         elif data[i][1][:3]<startdate:
            e_index=i
            break

      for i in range(s_index, e_index+1):
         dic[data[i][4]]+=int(data[i][5])

      most_sold = [[i, dic[i]] for i in dic]
      sorted_most_sold= sorted(most_sold, key= lambda x: x[1], reverse= True)

      return sorted_most_sold[1][0]
   
   elif item_by == "price":

      for i in range(len(data)):
         if enddate<=data[i][1][:3]>=startdate:
            s_index=i
         elif data[i][1][:3]<startdate:
            e_index=i
            break


      for i in range(s_index, e_index+1):
         dic[data[i][4]]+=int(data[i][5])*int(data[i][6])

      most_sold = [[i, dic[i]] for i in dic]
      sorted_most_sold= sorted(most_sold, key= lambda x: x[1], reverse= True)

      return sorted_most_sold[1][0]
   
''' Third API : gives percentage of items sold department wise from start date to end date'''

@app.route('/percentage_of_department_wise_sold_items/<string:startdate>/<string:enddate>/')
def percentage_of_department_wise_sold_items(startdate, enddate):

   set_dept=set()
   dept_wise_percent=defaultdict(lambda:0)
   
   startdate1 = [int(startdate[:4]), int(startdate[5:7]), int(startdate[8:10])]
   enddate1 =  [int(enddate[:4]), int(enddate[5:7]), int(enddate[8:10])]

   for i in data:
      set_dept.add(i[3])
   total_seats=0

   

   for i in data:
      if startdate1<=i[1]<=enddate1:
         total_seats+=int(i[5])

   for i in set_dept:
      dept_wise_percent[i]=(int(total_items(startdate, enddate,i))/total_seats)*100

   return jsonify(dept_wise_percent)

''' Fourth API : gives a list of sales of all 12 months in a year for a product'''

@app.route('/monthly_sales/<string:product>/<string:year>/')
def monthly_sales(product, year):
      sales=[0 for i in range(12)]
      
      for i in data:
         if i[1][0]==int(year):
            if product==i[4]:
               sales[i[1][1]-1]+=int(i[5])
      

      return sales


if __name__== "__main__":
    app.run(debug==True)
