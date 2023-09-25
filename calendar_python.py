import pandas as pd


# returns True if the year is leap
def is_year_leap(year):
    if year >= 1582:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        if year % 4 == 0:
            return True
        return False

# returns the day corresponding to the date
def get_day(d,m,y):
    ldays = [31,29,31,30,31,30,31,31,30,31,30,31]
    nldays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m > 12:
        return None
        
    elif not is_year_leap(y):
        if nldays[m-1] < d:
            return None
            
    elif ldays[m-1] < d:
            return None
        
    if m == 1 or m == 2:
        m = m+12
        y -= 1
    
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    n = d + 2*m + (3*(m+1)//5) + y + (y//4) - (y//100) + (y//400) + 2
    val = n%7
    return days[val]


# returns 2D array of a specific month's date like: [[' ', ' ', ' ', ' ', ' ', 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30]]

def m_calendar(m,y):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    nldays = [31,28,31,30,31,30,31,31,30,31,30,31]
    li = []
    temp = []
    i = 0
    d = 1
    mdays = 0
    
    if is_year_leap(y) and m == 2:
        mdays = 29
        
    else:
        mdays = nldays[m-1]
            
    res = get_day(d,m,y)
    while res != days[i]:
        temp.append(' ')
        i+=1
    while d<=mdays:
        for k in range(7-i):
            if d>mdays:
                temp.append(' ')
            else:
                temp.append(d)
                d+=1
                i=0
        li.append(temp)
        temp = []
    return li

# returns the dataframe with days columns and blank index
def clean_cal(df):
    days = {0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
    ind = {0:"", 1:"", 2:"", 3:"", 4:"", 5:""}
    df.rename(columns = days, inplace = True)
    df.rename(index = ind, inplace = True)
    return df


m = int(input("Enter Month: "))
y = int(input("Enter Year: "))
cldr = m_calendar(m,y)
df = pd.DataFrame(cldr)
df = clean_cal(df)
print(df) # printing the calendar
