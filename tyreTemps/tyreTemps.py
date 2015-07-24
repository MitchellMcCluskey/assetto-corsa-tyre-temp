##############################################################
# Mitchell McCluskey
# Tyre Temperature : Get tyre temperatures from AC
#
# To activate create a folder with the name tyreTemps
# in apps/python. Ex apps/python/tyreTemps
# Then copy this file inside it and launch AC
#############################################################

import ac
import acsys
import math

appWindow=0
FL=0
FR=0
RL=0
RR=0
space=30

class TyreTempText:
	
	def __init__(self, app, name, x, y):
		global space
		self.temp = 1
		self.xPosition = x
		self.yPosition = y
		self.name = name
		
		self.labelTemperature = ac.addLabel(app, self.name + ":")
		ac.setPosition(self.labelTemperature, self.xPosition, self.yPosition)
		self.labelTemperatureValue = ac.addLabel(app, str(self.temp))
		ac.setPosition(self.labelTemperatureValue, self.xPosition + space, self.yPosition)
	
	# def setTemperature(_temp):
		# self.temp = _temp
	
	# def getTemperature():
		# return self.temp
	
	def updateTemperature(self):
		FLTyreTemp, FRTyreTemp, RLTyreTemp, RRTyreTemp = ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp);
		
		if self.name == "FL":
			ac.setText(self.labelTemperatureValue, "{:.0f}°".format(FLTyreTemp))
		if self.name == "FR":
			ac.setText(self.labelTemperatureValue, "{:.0f}°".format(FRTyreTemp))
		if self.name == "RL":
			ac.setText(self.labelTemperatureValue, "{:.0f}°".format(RLTyreTemp))
		if self.name == "RR":
			ac.setText(self.labelTemperatureValue, "{:.0f}°".format(RRTyreTemp))

			

# This function gets called by AC when the App is initialised
# The function has to return a string with the App name
def acMain(ac_version):
	global appWindow, FL, FR, RL, RR, space
	
	appWindow = ac.newApp("Tyre Temps")
	
	ac.setSize(appWindow,160,209)
	ac.drawBorder(appWindow,0)
	ac.setBackgroundOpacity(appWindow,0)
	# Make the background a set of tyre outlines
	ac.setBackgroundTexture(appWindow,"apps/python/tyreTemps/tyretempsBackground.png")
	
	FL = TyreTempText(appWindow, "FL", 25, 85)
	FR = TyreTempText(appWindow, "FR", 95, 85)
	RL = TyreTempText(appWindow, "RL", 25, 105)
	RR = TyreTempText(appWindow, "RR", 95, 105)
	
	return "Tyre Temps"

def acUpdate(deltaT):
	global FL, FR, RL, RR
	FL.updateTemperature()
	FR.updateTemperature()
	RL.updateTemperature()
	RR.updateTemperature()