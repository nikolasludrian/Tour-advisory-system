import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt 威海地图窗口')
        self.setGeometry(125, 100, 568, 600)
        # 创建一个QWidget作为地图的容器
        map_container = QWidget(self)
        
        # 创建QWebEngineView并设置其URL
        map_view = QWebEngineView(map_container)
        map_view.load(QUrl.fromLocalFile("D:\pycharm_projects\pythonProject\my_chart.html"))
        # 创建布局并添加地图视图
        layout = QVBoxLayout(map_container)
        layout.addWidget(map_view)
        
        # 设置地图容器的布局
        map_container.setLayout(layout)
        # 显示地图容器
        self.setCentralWidget(map_container)
# 创建应用程序实例并运行
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())