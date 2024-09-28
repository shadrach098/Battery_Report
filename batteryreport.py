from plyer import notification
from bruceIQ import BatteryStatus
import psutil,threading
import psutil as ps,os,time
from datetime import datetime
def batteryC():
    count=0
    batter=0
    batt=0
    start=0
    start2=0  
    os.system('cls')
    psutil.sensors_battery().percent
    now=datetime.now()
    time.sleep(0.5)   
    print("AC Monitoring Has Started\r")
    print('User : '+str(psutil.users()[0][0]).title()+"\r")
    print(f"Current Battery Percent : {str(psutil.sensors_battery().percent)}%\r")
    print(f'Date : {now.strftime("%a/%d/%m/%Y")}\r' )
    print(f"Time : {now.strftime("%H:%M:%p")}\r")
   
    
    while True:
        
        battery=psutil.sensors_battery()
        percet=battery.percent
        if percet<=25 and start==0:
            start+=1
            notification.notify(
                title="Battery Percentage",
                message="Hi "+str(psutil.users()[0][0]).title() +" You Have  "+str(percet)+"% Battery remaining Please Charge",
                timeout=15,
                ticker="BRUCE",
                toast=True
            )
            
                
        name=(ps.users()[0][0])
        if ps.sensors_battery()[2]==True and count==0 and (ps.sensors_battery()[0])!=100:
            count+=1
            notification.notify(
                title="AC Status",
                message="Hi "+str(psutil.users()[0][0]).title() +" Laptop Is Charging"+" You Have  "+str(percet)+"% Battery remaining",
                timeout=15,
                ticker="BRUCE",
                toast=True
            )
        elif  ps.sensors_battery()[2]==False and count==1 and (ps.sensors_battery()[0])!=100:
            count=0
            notification.notify(
                title="AC Status",
                message="Hi "+str(psutil.users()[0][0]).title() +" Laptop Charging Paused"+" You Have  "+str(percet)+"% Battery remaining",
                timeout=15
            )  
            
    
        if (ps.sensors_battery()[0])== 100 :
            if (ps.sensors_battery()[2])==True and batt==0:
                batt+=1
                battery='🔌Power Still Connected ⚡'
                notification.notify(
                title="Battery Activity",
                message=(f" {name} Charging Completed Battery is 100%🔋 fully Charged. Battery Status: {battery}"),
                timeout=15
            ) 
            elif(ps.sensors_battery()[2])==False and batt==1:
                batt=0
                battery="🔌Power has been Unplugged" 
                notification.notify(
                title="Battery Activity",
                message=(f" {name} Charging Completed Battery is 100%🔋 fully Charged. Battery Status: {battery}"),
                timeout=15
            )  
              
                
                
        elif (ps.sensors_battery()[0]) <=50:
            if (ps.sensors_battery()[2])==True and start2==0:
                start2+=1
                battery='🔌Power Plugged, Battery Is Charging⚡'
                notification.notify(
                    title="Battery Activity",
                    message=(f" {name} Your Battery is Charging {(ps.sensors_battery()[0])}%🪫 Available Now . Battery Status: {battery}"),
                    timeout=15
                )
                
            
            elif(ps.sensors_battery()[2])==False and start2==1:
                start2=0
                battery="🔌Power Unplugged, Battery is not charging" 
                notification.notify(
                    title="Battery Activity",
                    message=(f" {name} Your Battery is Down to {(ps.sensors_battery()[0])}%🪫 remaining. Battery Battery is passed usable Percentage"),
                    timeout=15
                ) 
             
        
        if (ps.sensors_battery()[2])==True and (ps.sensors_battery()[0]) ==80 and batter==0:
            batter+=1
            notification.notify(
                    title="Battery Activity",
                    message=(f" {name} Your Battery is Up to {(ps.sensors_battery()[0])}%🔋 Available Now . Laptop Can Be used now without A power connector Safely"),
                    timeout=15
                )         
                    
Thread=threading.Thread(target=batteryC,daemon=True)

Thread.start() 

while True:
    pass


