##############################################################
# Mitchell McCluskey
# Tyre Temperature : Get tyre temperatures from AC
#
#############################################################

# import ac and acsys for necessary interactivity with Assetto Corsa
import ac
import acsys
import math

# global variables
appWindow=0
FL=0
FR=0
RL=0
RR=0
space=30

# class that is used for each of the tyres
class TyreTempText:
	
	# constructor takes the app window the name of the tyre and the offset position for each of the info
	def __init__(self, app, name, x, y):
		global space
		self.temp = 1
		self.xPosition = x
		self.yPosition = y
		self.name = name
		
		# create a label using the tyre name and a placeholder for the associated temperature
		self.labelTemperature = ac.addLabel(app, self.name + ":")
		ac.setPosition(self.labelTemperature, self.xPosition, self.yPosition)
		self.labelTemperatureValue = ac.addLabel(app, str(self.temp))
		ac.setPosition(self.labelTemperatureValue, self.xPosition + space, self.yPosition)

	# called when the acUpdate function is called - essentially constantly. update the temperature label
	def updateTemperature(self, temperature):
		# update the temperature using temperate given
		ac.setText(self.labelTemperatureValue, "{:.0f}°".format(temperature))

# This function gets called by AC when the App is initialised
# The function has to return a string with the App name
def acMain(ac_version):
	# use global variables
	global appWindow, FL, FR, RL, RR, space
	
	# create the app
	appWindow = ac.newApp("Tyre Temps")
	
	# setup the app window
	ac.setSize(appWindow,160,209)
	ac.drawBorder(appWindow,0)
	ac.setBackgroundOpacity(appWindow,0)
	# make the background a set of tyre outlines
	ac.setBackgroundTexture(appWindow,"apps/python/tyreTemps/tyretempsBackground.png")
	
	# create an object for each tyre
	FL = TyreTempText(appWindow, "FL", 25, 85)
	FR = TyreTempText(appWindow, "FR", 95, 85)
	RL = TyreTempText(appWindow, "RL", 25, 105)
	RR = TyreTempText(appWindow, "RR", 95, 105)
	
	return "Tyre Temps"

# This updates essentially all the time, where deltaT is the time passed since this was last called
def acUpdate(deltaT):
	# use global tyre objects
	global FL, FR, RL, RR
	# get the tyre temps from ac
	FLTyreTemp, FRTyreTemp, RLTyreTemp, RRTyreTemp = ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)
	# update temperatures for each of the tyres
	FL.updateTemperature(FLTyreTemp)
	FR.updateTemperature(FRTyreTemp)
	RL.updateTemperature(RLTyreTemp)
	RR.updateTemperature(RRTyreTemp)