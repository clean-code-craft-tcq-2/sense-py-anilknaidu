import math
from enum import Enum


######################################### CalculateStas ##########################################
#Below function calculates statistics (Average Maximum and Minimum) for given list of numbers.
##################################################################################################

def calculateStats(numbers):
  stats_dcn = {"avg":0,"min":0,"max":0} #Dictionary Initialization
  
  if(len(numbers) != 0):                                    #Check for non empty list
    if all(isinstance(x, (int, float)) for x in numbers):   #Check if there are non-numeric items in list
      print("Calculating Stats for",numbers)
      stats_dcn["avg"] = sum(numbers)/len(numbers)
      stats_dcn["max"] = max(numbers)
      stats_dcn["min"] = min(numbers)
      return stats_dcn                                      #Return Average, Max, Min
    else: raise ValueError("Non-numeric input detected")    #ValueError if Input has non-numeric items
  else: raise ValueError("No input numbers")                #ValueError if numbers list is empty



######################################### StatsAlerter ##########################################
#Below class is for computing Statistics for numbers and alerting User via LED and Email incase
#Max exceeds threshold.
#################################################################################################

class StatsAlerter(): 
  def __init__(self, MaxThreshold, alert_list):
    self.MaxThreshold = MaxThreshold                        
    self.alert_list = alert_list
  def checkAndAlert(self,numbers):                          #Method to check and alert user
    if(max(numbers)>self.MaxThreshold):                     #Check if Max of numbers list exceeds threshold
      for alerts in self.alert_list:
        alerts                                              #In case max exceeds threshold, Raise Alert request(s)
    else:
      print("Max within threshold limit")                   #No alerts here



######################################### EmailAlert ############################################
#Below class Raises Email alert and validates if email has been sent successfully.
#################################################################################################

class EmailAlert():
  emailAddress = "abc@xyz.com"                              #User Email
  emailStatusSent = False                                   #Initially no email sent
  
  def sendEmail(self):                      
    try:
      print("Invoking Outlook dispatch")                    #invokes Outlook function to send email to recipient
      #Email sending validation
      if(True):                                             #Validate if email was sent
        print("Email sent to :",self.emailAddress)
        self.emailStatusSent = True                         #Set email status as sent(True)
    except:
      print("Error sending Email;")                         #Incase no email sent emailStatusSent remains False

  def emailSent(self):
    return self.emailStatusSent   

######################################### LEDAlert ##############################################
#Below class Raises LED alert and validates if LED has been turned ON
#################################################################################################

class LEDAlert():

  class LedState(Enum):                                     #Subclass for Ledstate Enum
    OFF = 0
    ON = 1
  
  LedPin = 5                                                #HW level LED pin connection to turn ON
  LedStatus = LedState.OFF                                  #Led status is OFF initially
  
  def alert(self):                                      
    try:
      print("Invoking LowLevel Driver commads for LedPin=", self.LedPin)#Send request to LLD to turn ON LED
      
      #LED  validation
      if(True):                                             #LED Turned ON
        print("Led Turned on")
        self.LedStatus = self.LedState.ON                   #Update status to LED ON
      
    except:
      print("Error Turning LED On\n")

  def ledGlows(self):
    #print("Current status of LED: ",LedState.OFF)) 
    return(bool(self.LedStatus.value))                      #Return status of LED ON/OFF (True/False)
  
  

