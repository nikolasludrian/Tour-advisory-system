import sys

from PyQt5 import QtWidgets,QtCore
from 主界面ui import DockWidget as Menu_Ui
from 景点查询界面 import DockWidget as Search_Ui
from 景点榜单 import DockWidget as Rank_Ui
from 个性化定制 import DockWidget as Plan_Ui

#从此文件执行可得到程序完整效果

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#设置高分屏自适应
    # 创建应用程序实例
    app = QtWidgets.QApplication(sys.argv)
    Menu=Menu_Ui()
    Search=Search_Ui()
    Rank=Rank_Ui()
    Plan=Plan_Ui()
    Menu.pushButton_2.clicked.connect(Search.show)
    Menu.pushButton_2.clicked.connect(Menu.close)
    Search.pushButton_11.clicked.connect(Menu.show)
    Search.pushButton_11.clicked.connect(Search.close)






    Menu.show()
    sys.exit(app.exec())
