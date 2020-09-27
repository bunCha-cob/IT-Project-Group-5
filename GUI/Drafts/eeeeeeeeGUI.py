

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot


#!/usr/bin/python

import sqlite3


try:
	conn = sqlite3.connect('test.db')
	print "Opened database successfully";
except:
	print("Database was not opened successfully"); 

#most engaged customer
cursorMax1 = conn.execute("SELECT trackID FROM engaged WHERE MAX(engagement_time)")
cursorMax2 = conn.execute("SELECT MAX(engagement_time)")
cursorMax3 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1+"")
cursorMax4 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(0)+")

#least engaged customer
cursorMin1 = conn.execute("SELECT trackID FROM engaged WHERE MIN(engagement_time)")
cursorMin2 = conn.execute("SELECT MIN(engagement_time)")
cursorMin3 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMin1+"")
cursorMin4 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMin3(0)+")

#most engaged customers
cursorMaxTen1 = conn.execute("SELECT trackID FROM engaged ORDER BY engagement_time DESC LIMIT 10")
cursorMaxTen2 = conn.execute("SELECT engagement_time FROM engaged ORDER BY engagement_time DESC LIMIT 10")
cursorMaxTen3-1 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(0)+"")
cursorMaxTen3-2 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(1)+"")
cursorMaxTen3-3 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(2)+"")
cursorMaxTen3-4 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(3)+"")
cursorMaxTen3-5 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(4)+"")
cursorMaxTen3-6 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(5)+"")
cursorMaxTen3-7 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(6)+"")
cursorMaxTen3-8 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(7)+"")
cursorMaxTen3-9 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(8)+"")
cursorMaxTen3-10 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(9)+"")
cursorMaxTen4-1 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(0)+")
cursorMaxTen4-2 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(1)+")
cursorMaxTen4-3 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(2)+")
cursorMaxTen4-4 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(3)+")
cursorMaxTen4-5 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(4)+")
cursorMaxTen4-6 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(5)+")
cursorMaxTen4-7 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(6)+")
cursorMaxTen4-8 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(7)+")
cursorMaxTen4-9 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(8)+")
cursorMaxTen4-10 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(9)+")

#least engaged customers
cursorMinTen1 = conn.execute("SELECT trackID FROM engaged ORDER BY engagement_time ASC LIMIT 10")
cursorMinTen2 = conn.execute("SELECT engagement_time FROM engaged ORDER BY engagement_time ASC LIMIT 10")
cursorMinTen3-1 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(0)+"")
cursorMinTen3-2 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(1)+"")
cursorMinTen3-3 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(2)+"")
cursorMinTen3-4 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(3)+"")
cursorMinTen3-5 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(4)+"")
cursorMinTen3-6 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(5)+"")
cursorMinTen3-7 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(6)+"")
cursorMinTen3-8 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(7)+"")
cursorMinTen3-9 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(8)+"")
cursorMinTen3-10 = conn.execute("SELECT curstomerID, area FROM primary_table WHERE trackID = "+cursorMax1(9)+"")
cursorMinTen4-1 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(0)+")
cursorMinTen4-2 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(1)+")
cursorMinTen4-3 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(2)+")
cursorMinTen4-4 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(3)+")
cursorMinTen4-5 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(4)+")
cursorMinTen4-6 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(5)+")
cursorMinTen4-7 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(6)+")
cursorMinTen4-8 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(7)+")
cursorMinTen4-9 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(8)+")
cursorMinTen4-10 = conn.execute("SELECT all_areas_visited FROM total_areas WHERE customerID = "+cursorMax3(9)+")


#Average
cursorAvgEng = conn.execute("SELECT AVG(engagement_time) FROM engaged")

#Total Engagement Time
cursorTotalTime = conn.execute("SELECT SUM(engagement_time) FROM primaty_table")


#Total Customer
cursorTotalCust = conn.execute("SELECT SUM(trackingID) FROM primaty_table")

#Top areas
cursorArea1 = conn.execute("SELECT DISTINCT all_areas_visited FROM  total_areas")
for areas in cursorArea1:
	cursorArea2 = conn.execute("SELECT COUNT("+areas+") FROM total_areas WHERE all_areas_visited="+areas+"")
cursorArea3 = max(cursorArea2)

#Which area has highest area
cursorAreaEng1 = conn.execute("SELECT DISTINCT all_areas_visited FROM  total_areas")
for areas in cursorAreaEng1:
	cursorAreaEng2 = conn.execute("SELECT COUNT("+areas+") FROM total_areas WHERE all_areas_visited = "+areas+"")


#Tracking plot
cursorPlot1 = conn.execute("SELECT x FROM plot WHERE trackID ="+trackIDgiven+"")
cursorPlot2 = conn.execute("SELECT y FROM plot WHERE trackID ="+trackIDgiven+"")
cursorPlot3 = conn.execute("SELECT z FROM plot WHERE trackID ="+trackIDgiven+"")

plot(cursorPlot1, cursorPlot2, cursorPlot3)

	for x in cursorPlot1:
		for y in cursorPlot2:
			for z in cursorPlot3:


    				ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    				ax.set_xlabel('width')
    				ax.set_ylabel('height')
    				ax.set_zlabel('time')

    				ax.view_init(35, 80)

    				frame = plt.gca()

    				frame.axes.get_xaxis().set_ticks([])
    				frame.axes.get_yaxis().set_ticks([])

    				fig2 = plt.figure(2)
    				fig2_title = 'Walking pattern of a single customer( trackingID = ' + str(single_trackingID) + ')'
    				fig2.suptitle(fig2_title, fontsize=15)
    				plt.plot(x_single_tracking,y_single_tracking, 'ro')
    				plt.axis([0,w_numStep,h_numStep,0])

    				frame.axes.get_xaxis().set_ticks([])
    				frame.axes.get_yaxis().set_ticks([])

    				fig.savefig('engage_level.jpg')
    				fig2.savefig('single_tracking.jpg')
    				plt.show()

    				vid.release()
    				if FLAGS.ouput:
        				out.release()
        				list_file.close()
    				cv2.destroyAllWindows()





class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Satisfaction of Customers App'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
	self.statusBar().showMessage('Message in statusbar.')
	button = QPushButton('PyQt5 button', self)
`	button.setToolTip('Average')
	button.move(100,70)
	button = QPushButton('PyQt5 button', self)
`	button.setToolTip('Average')
	button.move(100,70)
	button = QPushButton('PyQt5 button', self)
`	button.setToolTip('Average')
	button.move(100,70)
        self.show()
    
	@pyqtSlot()
	def on_click(self):
    		print('PyQt5 button click')

if __name__ == '__main__':
    	app = QApplication(sys.argv)
    	ex = App()
    	sys.exit(app.exec_())
	conn.close()	