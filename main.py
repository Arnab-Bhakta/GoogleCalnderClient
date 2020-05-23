from gcalanderclient import gcalanderapi
from events import events
from datetime import datetime

print("called")

print( "input format DD MM YYYY      HH MM" )
event_name = input( 'event name         : ')
start_date = input( 'starting date (leave empty for today) : ' )
start_time = input( 'starting time : ')
end_date = input( 'ending date (leave empty for today)   : ' )
end_time = input( 'ending time : ')

if (start_date == ''):
    start_date = str(datetime.now().date())
else:
    start_date = start_date[6:10]+"-"+start_date[3:5]+"-"+start_date[0:2]

if (end_date == ''):
    end_date   = str(datetime.now().date())
else:
    end_date = end_date[6:10]+"-"+end_date[3:5]+"-"+end_date[0:2]

st = start_date+"T"+start_time[0:2]+":"+start_time[3:5]+":00"
et = end_date+"T"+end_time[0:2]+ ":" + end_time[3:5] +":00"

event =  events( event_name, st, et, 'ad', 'df' ).event
print ( event )
gcalanderapi().create_event( event )

print("done")
