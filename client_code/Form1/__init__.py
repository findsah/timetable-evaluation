from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

from ..WelcomePage import WelcomePage
from ..ResultPage import ResultPage
from ..ContactUsPage import ContactUsPage

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('WelcomePage')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('ContactUsPage')

  def decoding_majorStudy(self):
    majorStudy = 0
    if self.drop_down_1.selected_value=="Accounting":
      majorStudy=0
    if self.drop_down_1.selected_value=="Marketing":
      majorStudy=1
    if self.drop_down_1.selected_value=="Finance":
      majorStudy=2
    if self.drop_down_1.selected_value=="Human Resource Management":
      majorStudy=3  
    if self.drop_down_1.selected_value=="Management information Systems":
      majorStudy=4
    if self.drop_down_1.selected_value=="Civil Engineering":
      majorStudy=5
    if self.drop_down_1.selected_value=="Indutrial Engineering":
      majorStudy=6
    if self.drop_down_1.selected_value=="Computer Engineering":
      majorStudy=7
    if self.drop_down_1.selected_value=="Electrical Engineering":
      majorStudy=8
    if self.drop_down_1.selected_value=="Mechanical Engineering":
      majorStudy=9
    if self.drop_down_1.selected_value=="Chemical Engineering":
      majorStudy=10
    if self.drop_down_1.selected_value=="Architectural Engineering":
      majorStudy=11
    if self.drop_down_1.selected_value=="Telecommunications and Network Technology":
      majorStudy=12
    if self.drop_down_1.selected_value=="Information Systems and Technology":
      majorStudy=13
    if self.drop_down_1.selected_value=="Master of Business Administration (MBA)":
      majorStudy=14
    if self.drop_down_1.selected_value=="Master of Science in Computer Engineering- AI":
      majorStudy=15
    if self.drop_down_1.selected_value=="Master of Science program in Electrical Engineering -Power, Energy Sources and Systems (PES)":
      majorStudy=16
    return majorStudy

  def decoding_creditCompleted(self):
    creditsCompleted = 0
    if self.radio_button_3.selected==True:
      creditsCompleted=0
    if self.radio_button_4.selected==True:
      creditsCompleted=1
    if self.radio_button_5.selected== True:
      creditsCompleted=2
    if self.radio_button_6.selected == True:
      creditsCompleted=3
    return creditsCompleted

  def decoding_timeOfDayMostSuited(self):
    timeOfDayMostSuited = 0
    if self.radio_button_7.selected == True:
      timeOfDayMostSuited=0

    if self.radio_button_8.selected == True:
      timeOfDayMostSuited=1
    if self.radio_button_9.selected==True:
      timeOfDayMostSuited=2
    return timeOfDayMostSuited
    
  def decoding_preferredWeeklyAttendance(self):
    preferredWeeklyAttendance=1
    if self.drop_down_2.selected_value =="1 day in a week":
      preferredWeeklyAttendance=1
    if self.drop_down_2.selected_value =="2 days in week":
      preferredWeeklyAttendance=2
    if self.drop_down_2.selected_value =="3 days in week":
      preferredWeeklyAttendance=3
    if self.drop_down_2.selected_value =="4 days in week":
      preferredWeeklyAttendance=4
    if self.drop_down_2.selected_value =="5 days in week":
      preferredWeeklyAttendance=5
    return preferredWeeklyAttendance

  def decoding_NbHoursDayMostProductive(self):
    NbHoursDayMostProductive = 0
    
    if self.radio_button_10.selected == True:
      NbHoursDayMostProductive = 0
    if self.radio_button_11.selected == True:
      NbHoursDayMostProductive = 3
    if self.radio_button_12.selected == True:
      NbHoursDayMostProductive = 5
    return NbHoursDayMostProductive

  def decoding_longBreaksBetweenClasses(self):

    longBreaksBetweenClasses=0

    if self.radio_button_16.selected == True:
      longBreaksBetweenClasses=0
    if self.radio_button_17.selected == True:
      longBreaksBetweenClasses=1
    if self.radio_button_18.selected == True:
      longBreaksBetweenClasses=2
    if self.radio_button_19.selected == True:
      longBreaksBetweenClasses=3
    return longBreaksBetweenClasses
    
  def decoding_Semester(self):
    Semester=0
    if self.radio_button_13.selected == True:
      Semester = 0
    if self.radio_button_14.selected == True:
      Semester = 1
    if self.radio_button_15.selected == True:
      Semester = 2
    return Semester
    
  def decoding_NbCreditsEnrolled(self):
    NbCreditsEnrolled =7
    if self.drop_down_3.selected_value=="6 – 8 credits":
      NbCreditsEnrolled=7
    if self.drop_down_3.selected_value=="9 - 12 credits":
      NbCreditsEnrolled=11
    if self.drop_down_3.selected_value=="13 - 15 credits":
      NbCreditsEnrolled=14
    if self.drop_down_3.selected_value=="16 - 18 credits":
      NbCreditsEnrolled=17
    return NbCreditsEnrolled
  def decoding_NbElectiveCredits(self):
    NbElectiveCredits=0
    if self.drop_down_4.selected_value=="None":
      NbElectiveCredits=0
    if self.drop_down_4.selected_value=="1":
      NbElectiveCredits=1
    if self.drop_down_4.selected_value=="2":
      NbElectiveCredits=2
    if self.drop_down_4.selected_value=="3":
      NbElectiveCredits=3
    if self.drop_down_4.selected_value=="4":
      NbElectiveCredits=4
    if self.drop_down_4.selected_value=="5":
      NbElectiveCredits=5
    if self.drop_down_4.selected_value=="6 or above":
      NbElectiveCredits=6
    return NbElectiveCredits

  def decoding_NbDaysAttendingClasses(self):
    NbDaysAttendingClasses=1
    if self.drop_down_7.selected_value == "1 day in a week":
      NbDaysAttendingClasses = 1
    if self.drop_down_7.selected_value == "2 days in a week":
      NbDaysAttendingClasses = 2
    if self.drop_down_7.selected_value == "3 days in a week":
      NbDaysAttendingClasses = 3
    if self.drop_down_7.selected_value == "4 days in a week":
      NbDaysAttendingClasses = 4
    if self.drop_down_7.selected_value == "5 days in a week":
      NbDaysAttendingClasses = 5
    return NbDaysAttendingClasses

  def decoding_LowNbHoursPerDay(self):
    LowNbHoursPerDay=0
    if self.radio_button_20.selected==True:
      LowNbHoursPerDay=0
    if self.radio_button_21.selected==True:
      LowNbHoursPerDay=3
    if self.radio_button_22.selected==True:
      LowNbHoursPerDay=5
    return LowNbHoursPerDay

  def decoding_maximumNbHoursPerDay(self):
    maximumNbHoursPerDay=0
    if self.radio_button_23.selected ==True:
      maximumNbHoursPerDay =0
    if self.radio_button_24.selected ==True:
      maximumNbHoursPerDay =3
    if self.radio_button_25.selected ==True:
      maximumNbHoursPerDay =5
    return maximumNbHoursPerDay
  def decoding_NbMorningClasses(self):
    NbMorningClasses=0
    if self.drop_down_8.selected_value=="None":
      NbMorningClasses=0
    if self.drop_down_8.selected_value=="1":
      NbMorningClasses=1
    if self.drop_down_8.selected_value=="2":
      NbMorningClasses=2
    if self.drop_down_8.selected_value=="3":
      NbMorningClasses=3
    if self.drop_down_8.selected_value=="4":
      NbMorningClasses=4
    if self.drop_down_8.selected_value=="5 or more":
      NbMorningClasses=5
    return NbMorningClasses
    
  def decoding_NbAfternoonClasses(self):
    NbAfternoonClasses=0
    if self.drop_down_9.selected_value=="None":
      NbAfternoonClasses=0
    if self.drop_down_9.selected_value=="1":
      NbAfternoonClasses=1
    if self.drop_down_9.selected_value=="2":
      NbAfternoonClasses=2
    if self.drop_down_9.selected_value=="3":
      NbAfternoonClasses=3
    if self.drop_down_9.selected_value=="4":
      NbAfternoonClasses=4
    if self.drop_down_9.selected_value=="5 or more":
      NbAfternoonClasses=5
    return NbAfternoonClasses

  def decoding_NbEveningClasses(self):
    NbEveningClasses=0
    if self.drop_down_10.selected_value=="None":
      NbEveningClasses=0
    if self.drop_down_10.selected_value=="1":
      NbEveningClasses=1
    if self.drop_down_10.selected_value=="2":
      NbEveningClasses=2
    if self.drop_down_10.selected_value=="3":
      NbEveningClasses=3
    if self.drop_down_10.selected_value=="4":
      NbEveningClasses=4
    if self.drop_down_10.selected_value=="5 or more":
      NbEveningClasses=5
    return NbEveningClasses

  def decoding_FailAnyCourses(self):
    FailAnyCourses=0

    if self.drop_down_5.selected_value=="None":
      FailAnyCourses=0
    else:
      FailAnyCourses=1
    return FailAnyCourses

  def decoding_GPAaffectedPositively(self):
    GPAaffectedPositively =0

    if self.radio_button_26.selected==True:
      GPAaffectedPositively =0
    if self.radio_button_27.selected==True:
      GPAaffectedPositively =1
    if self.radio_button_28.selected==True:
      GPAaffectedPositively =2
    return GPAaffectedPositively
    
  def decoding_nbInstructorsUnfamiliar(self):
    nbInstructorsUnfamiliar = 0
    if self.drop_down_11.selected_value=="None":
      nbInstructorsUnfamiliar =0
    if self.drop_down_11.selected_value=="1":
      nbInstructorsUnfamiliar =1
    if self.drop_down_11.selected_value=="2":
      nbInstructorsUnfamiliar =2
    if self.drop_down_11.selected_value=="3":
      nbInstructorsUnfamiliar =3
    if self.drop_down_11.selected_value=="4":
      nbInstructorsUnfamiliar =4
    if self.drop_down_11.selected_value=="5 or more":
      nbInstructorsUnfamiliar =5
    return nbInstructorsUnfamiliar

  def decoding_nbPrefInstructors(self):
    nbPrefInstructors = 0
    if self.drop_down_6.selected_value=="None":
      nbPrefInstructors =0
    if self.drop_down_6.selected_value=="1":
      nbPrefInstructors =1
    if self.drop_down_6.selected_value=="2":
      nbPrefInstructors =2
    if self.drop_down_6.selected_value=="3":
      nbPrefInstructors =3
    if self.drop_down_6.selected_value=="4":
      nbPrefInstructors =4
    if self.drop_down_6.selected_value=="5 or more":
      nbPrefInstructors=5
    return nbPrefInstructors

  def decoding_nbNONPrefInstructors(self):
    nbNONPrefInstructors = 0
    if self.drop_down_12.selected_value=="None":
      nbNONPrefInstructors =0
    if self.drop_down_12.selected_value=="1":
      nbNONPrefInstructors =1
    if self.drop_down_12.selected_value=="2":
      nbNONPrefInstructors =2
    if self.drop_down_12.selected_value=="3":
      nbNONPrefInstructors =3
    if self.drop_down_12.selected_value=="4":
      nbNONPrefInstructors =4
    if self.drop_down_12.selected_value=="5 or more":
      nbNONPrefInstructors=5
    return nbNONPrefInstructors

  def decoding_followPrimaryPath(self):

    followPrimaryPath=0
    if self.radio_button_1.selected==True:
      followPrimaryPath=0
    if self.radio_button_2.selected==True:
      followPrimaryPath=1
    return followPrimaryPath
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    majorStudy = self.decoding_majorStudy()
    creditCompleted = self.decoding_creditCompleted()
    timeOfDayMostSuited = self.decoding_timeOfDayMostSuited()
    preferredWeeklyAttendance = self.decoding_preferredWeeklyAttendance()
    NbHoursDayMostProductive = self.decoding_NbHoursDayMostProductive()
    longBreaksBetweenClasses = self.decoding_longBreaksBetweenClasses()
    Semester = self.decoding_Semester()
    NbCreditsEnrolled = self.decoding_NbCreditsEnrolled()
    NbElectiveCredits = self.decoding_NbElectiveCredits()
    NbDaysAttendingClasses=self.decoding_NbDaysAttendingClasses()
    LowNbHoursPerDay = self.decoding_LowNbHoursPerDay()
    maximumNbHoursPerDay =self.decoding_maximumNbHoursPerDay()
    NbMorningClasses = self.decoding_NbMorningClasses()
    NbAfternoonClasses = self.decoding_NbAfternoonClasses()
    NbEveningClasses = self.decoding_NbEveningClasses()
    FailAnyCourses = self.decoding_FailAnyCourses()
    GPAaffectedPositively = self.decoding_GPAaffectedPositively()
    nbInstructorsUnfamiliar = self.decoding_nbInstructorsUnfamiliar()
    nbPrefInstructors = self.decoding_nbPrefInstructors()
    nbNONPrefInstructors = self.decoding_nbNONPrefInstructors()
    followPrimaryPath = self.decoding_followPrimaryPath()
    
      
    
    # Check the value of a radiobutton and set 0 as the value of another variable
    
    test_case_list =[majorStudy,creditCompleted,timeOfDayMostSuited,preferredWeeklyAttendance,NbHoursDayMostProductive,	longBreaksBetweenClasses,Semester,NbCreditsEnrolled,NbElectiveCredits,NbDaysAttendingClasses,LowNbHoursPerDay,	maximumNbHoursPerDay,NbMorningClasses,NbAfternoonClasses,NbEveningClasses,FailAnyCourses,GPAaffectedPositively,	nbInstructorsUnfamiliar,nbPrefInstructors,nbNONPrefInstructors,followPrimaryPath]

    print(len(test_case_list))

    print(test_case_list)
    
    # Call the Anvil server function to send responses to Jupyter notebook
    result = anvil.server.call('get_predicted_output', test_case_list)
    print(result)

    # For demonstration purposes, let's assume the result is a placeholder value
    #result = "PlaceholderResult"

        # Open the ResultPage and pass the result as a parameter
    open_form('ResultPage', result=result)
