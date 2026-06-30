import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import random

threat = ["real", "fake"]

options = []

while len(options) < 5:
    num = random.randint(0,9)
    if num not in options:
        options.append(num)

incidents = {
             "Suspicious Login" : {"threat_lvl" : "Medium",
                                   "inv_real" : "Employee is on a vacation",
                                   "inv_fake" : "Activity matches recent employee behavior",
                                   "respond_real" : "Unauthorized access attempt contained",
                                   "respond_fake" : "Security team resources were wasted",
                                   "ignore_real" : "Account compromise went undetected",
                                   "ignore_fake" : "No action required"},

             "Phishing Emails" : {"threat_lvl" : "Low",
                                   "inv_real" : "Sender identity could not be verified",
                                   "inv_fake" : "Sender identity was successfully verified",
                                   "respond_real" : "Malicious email blocked",
                                   "respond_fake" : "Legitimate communication interrupted",
                                   "ignore_real" : "Employees exposed to phishing attempt",
                                   "ignore_fake" : "No action required"},

             "Malware Alert" : {"threat_lvl": "High",
                                "inv_real": "Suspicious software behavior was confirmed",
                                "inv_fake": "Software behavior appears legitimate",
                                "respond_real": "Malware successfully removed",
                                "respond_fake": "Legitimate software unnecessarily quarantined",
                                "ignore_real": "Malware spread through systems",
                                "ignore_fake": "No action required"},

             "Brute Force Attack" : {"threat_lvl": "Medium",
                                "inv_real": "Repeated unauthorized access attempts detected",
                                "inv_fake": "Activity appears consistent with user error",
                                "respond_real": "Attack source blocked",
                                "respond_fake": "Normal user activity disrupted",
                                "ignore_real": "Account security weakened",
                                "ignore_fake": "No action required"},

             "USB Device Detected" : {"threat_lvl": "Low",
                                "inv_real": "Device ownership could not be confirmed",
                                "inv_fake": "Device ownership was verified",
                                "respond_real": "Potential threat removed",
                                "respond_fake": "Approved device unnecessarily restricted",
                                "ignore_real": "Untrusted device remained connected",
                                "ignore_fake": "No action required"},

             "Large Data Download" : {"threat_lvl": "High",
                                "inv_real": "Download activity appears unauthorized",
                                "inv_fake": "Download activity matches approved operations",
                                "respond_real": "Data exfiltration prevented",
                                "respond_fake": "Business operations interrupted",
                                "ignore_real": "Sensitive data was leaked",
                                "ignore_fake": "No action required"},

             "Suspicious Wifi Connection" : {"threat_lvl": "Medium",
                                        "inv_real": "Connection originated from an untrusted network",
                                        "inv_fake": "Connection meets company security requirements",
                                        "respond_real": "Unsafe connection terminated",
                                        "respond_fake": "Legitimate connection interrupted",
                                        "ignore_real": "Device exposed to network threats",
                                        "ignore_fake": "No action required"},

             "Password Leak" : {"threat_lvl": "Critical",
                                "inv_real": "Active credentials were found in the leak",
                                "inv_fake": "Exposed credentials are no longer active",
                                "respond_real": "Credentials secured immediately",
                                "respond_fake": "Unnecessary password reset campaign launched",
                                "ignore_real": "Attackers gained account access",
                                "ignore_fake": "No action required"},

             "Ransomware Activity" : {"threat_lvl": "Critical",
                                "inv_real": "Malicious file activity was confirmed",
                                "inv_fake": "File activity appears legitimate",
                                "respond_real": "Ransomware contained successfully",
                                "respond_fake": "Critical systems unnecessarily shut down",
                                "ignore_real": "Company systems encrypted",
                                "ignore_fake": "No action required"},

             "Unauthorized Admin Privileges" : {"threat_lvl": "Critical",
                                                "inv_real": "Access escalation could not be justified",
                                                "inv_fake": "Access escalation was properly authorized",
                                                "respond_real": "Unauthorized privileges revoked",
                                                "respond_fake": "Legitimate administrator access removed",
                                                "ignore_real": "Attacker retained administrative control",
                                                "ignore_fake": "No action required"}
                                                }

scores = {
    "Low": {
        "respond_real":  (4, 2, -2),
        "respond_fake":  (0, -4, -3),
        "ignore_real":   (-12, -8, 0),
        "ignore_fake":   (0, 0, 0)},

    "Medium": {
        "respond_real":  (8, 4, -4),
        "respond_fake":  (0, -6, -5),
        "ignore_real":   (-20, -15, 0),
        "ignore_fake":   (0, 0, 0)},

    "High": {
        "respond_real":  (12, 6, -6),
        "respond_fake":  (0, -8, -8),
        "ignore_real":   (-30, -25, 0),
        "ignore_fake":   (0, 0, 0)},

    "Critical": {
        "respond_real":  (16, 8, -8),
        "respond_fake":  (0, -12, -10),
        "ignore_real":   (-45, -35, 0),
        "ignore_fake":   (0, 0, 0)}
}

class CyberApp(QWidget):
    def __init__(self):
        super().__init__()
        self.current_inc = 1
        self.tstatus = random.choice(threat)
        self.secs = 100
        self.rep = 100
        self.bud = 100

        # Main menu
        self.secscore = QLabel(f"Security Score = {self.secs}",self)
        self.reputation = QLabel(f"Reputation = {self.rep}",self)
        self.budget = QLabel(f"Budget = {self.bud}",self)
        self.welcome = QLabel("Welcome To The Game", self)
        self.click = QLabel("Click Start Shift To Begin", self)
        self.inv = QLabel("    Investigate 5 Incidents To End Shift\nMaintain security score and reputation", self)
        self.start = QPushButton("Start Shift", self)
        self.rules = QPushButton("Rules", self)
        self.exit = QPushButton("Exit", self)
        self.invbt = QPushButton("Investigate", self)
        self.ignore = QPushButton("Ignore", self)
        self.respond = QPushButton("Respond", self)
        self.change = QLabel(self)
        self.next = QPushButton("Next", self)
        self.result = QPushButton("Result", self)
        self.back = QPushButton("Back", self)
        self.rule = QLabel("RULES\n\n"
"• Complete 5 incidents per shift.\n"
"• Investigate before making a decision.\n"
"• Choose either Respond or Ignore.\n"
"• Incidents may be Real or Fake.\n"
"• Investigation clues help reveal the truth.\n"
"• Responding to fake threats wastes resources.\n"
"• Ignoring real threats can severely damage the company.\n"
"• Your decisions affect Security Score, Reputation, and Budget.\n"
"• Higher threat levels have greater consequences.\n"
"• Make the best decisions to achieve the highest rank.\n\n"
"TIP: Not every threat is real, and not every alert should be ignored.",self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cybersecurity Sentinel")

        # Scores
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.secscore)
        hbox1.addWidget(self.reputation)
        hbox1.addWidget(self.budget)
        vbox.addLayout(hbox1)

        # Welcome
        vbox.addWidget(self.welcome, alignment=Qt.AlignCenter)
        vbox.addWidget(self.click, alignment=Qt.AlignCenter)
        vbox.addWidget(self.inv, alignment=Qt.AlignCenter)
        vbox.addWidget(self.change, alignment=Qt.AlignCenter)
        vbox.addWidget(self.rule, alignment=Qt.AlignCenter)

        # Buttons
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.start)
        hbox2.addWidget(self.rules)
        hbox2.addWidget(self.exit)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.invbt)
        hbox3.addWidget(self.respond)
        hbox3.addWidget(self.ignore)
        hbox3.addWidget(self.next)
        hbox3.addWidget(self.result)
        hbox3.addWidget(self.back)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)
        
        self.invbt.hide()
        self.ignore.hide()
        self.respond.hide()
        self.change.hide()
        self.next.hide()
        self.result.hide()
        self.back.hide()
        self.rule.hide()

        # Names
        self.welcome.setObjectName("welcome")
        self.click.setObjectName("click")
        self.inv.setObjectName("inv")
        self.start.setObjectName("start")
        self.rules.setObjectName("rules")
        self.exit.setObjectName("exit")
        self.secscore.setObjectName("secscore")
        self.reputation.setObjectName("reputation")
        self.budget.setObjectName("budget")
        self.invbt.setObjectName("invbt")
        self.ignore.setObjectName("ignore")
        self.respond.setObjectName("respond")
        self.change.setObjectName("change")
        self.next.setObjectName("next")
        self.result.setObjectName("result")
        self.back.setObjectName("back")
        self.rule.setObjectName("rule")
        

        self.setStyleSheet("""
            QLabel, QPushButton{
                    font-family: calibri;
                    font-size: 20px;
                    font-weight: bold;
                                }
            QLabel#secscore, QLabel#reputation, QLabel#budget{
                    font-weight: bold;
                    color: #666666;
                           }
            QLabel#welcome{
                    font-size: 40px;
                    font-weight: bold;
                           }
            QLabel#click{
                    font-size: 25px;
                           }
            QLabel#inv, QLabel#change{
                    font-size: 20px;
                           }
            QPushButton{
                    padding: 10px;
                    border: 1px solid white;
                    border-radius: 20px;
                    color: white;
                           }
            QPushButton:hover{
                    border: 2px solid black;
                           }
            QPushButton#start, QPushButton#invbt{
                    background-color: #23DB3A;
                           }
            QPushButton#rules, QPushButton#respond{
                    background-color: #F5AD27;
                           }
            QPushButton#exit, QPushButton#ignore{
                    background-color: #FF5252;
                           }
            QPushButton#next, QPushButton#result, QPushButton#back{
                    background-color: #27A3F5;
                           }
            QLabel#rule{
                    font-size: 20px;
                           }
""")
        
        self.start.clicked.connect(self.shift)
        self.exit.clicked.connect(self.close)
        self.invbt.clicked.connect(self.investigate)
        self.respond.clicked.connect(self.responded)
        self.ignore.clicked.connect(self.ignored)
        self.next.clicked.connect(self.nextin)
        self.next.clicked.connect(self.shift)
        self.result.clicked.connect(self.display_result)
        self.rules.clicked.connect(self.display_rules)
        self.back.clicked.connect(self.get_back)
    
    def shift(self):
        self.start.hide()
        self.rules.hide()
        self.exit.hide()

        self.invbt.show()
        self.respond.show()
        self.ignore.show()
        self.welcome.show()

        inc_no = options[self.current_inc - 1]
        name = list(incidents)[inc_no]

        self.welcome.setText(f"INCIDENT #{self.current_inc}")
        self.click.setText(name)
        self.inv.hide()

    def investigate(self):
        inc_no = options[self.current_inc - 1]
        name = list(incidents)[inc_no]

        if self.tstatus == "real":
            self.inv.setText(incidents[name]["inv_real"])
        elif self.tstatus == "fake":
            self.inv.setText(incidents[name]["inv_fake"])
        self.inv.show()

        self.invbt.hide()

    def responded(self):
        inc_no = options[self.current_inc - 1]
        name = list(incidents)[inc_no]

        if self.tstatus == "real":
            self.click.setText(incidents[name]["respond_real"])
        elif self.tstatus == "fake":
            self.click.setText(incidents[name]["respond_fake"])

        if self.tstatus == "real":
            tlvl = incidents[name]["threat_lvl"]
            nest = scores[tlvl]["respond_real"]
            self.change.setText(f"{nest[0]} Security Score\n {nest[1]} Reputation\n {nest[2]} Budget")
        elif self.tstatus == "fake":
            tlvl = incidents[name]["threat_lvl"]
            nest = scores[tlvl]["respond_fake"]
            self.change.setText(f"{nest[0]} Security Score\n {nest[1]} Reputation\n {nest[2]} Budget")
        
        self.secs += nest[0]
        self.rep += nest[1]
        self.bud += nest[2]
        self.secscore.setText(f"Security Score = {self.secs}")
        self.reputation.setText(f"Reputation = {self.rep}")
        self.budget.setText(f"Budget = {self.bud}")

        self.welcome.hide()
        self.inv.hide()
        self.invbt.hide()
        self.respond.hide()
        self.ignore.hide()
        self.change.show()

        if self.current_inc == 5:
            self.result.show()
        else:
            self.next.show()

    def ignored(self):
        inc_no = options[self.current_inc - 1]
        name = list(incidents)[inc_no]

        if self.tstatus == "real":
            self.click.setText(incidents[name]["ignore_real"])
        elif self.tstatus == "fake":
            self.click.setText(incidents[name]["ignore_fake"])

        if self.tstatus == "real":
            tlvl = incidents[name]["threat_lvl"]
            nest = scores[tlvl]["ignore_real"]
            self.change.setText(f"{nest[0]} Security Score\n {nest[1]} Reputation\n {nest[2]} Budget")
        elif self.tstatus == "fake":
            tlvl = incidents[name]["threat_lvl"]
            nest = scores[tlvl]["ignore_fake"]
            self.change.setText(f"{nest[0]} Security Score\n {nest[1]} Reputation\n {nest[2]} Budget")
        
        self.secs += nest[0]
        self.rep += nest[1]
        self.bud += nest[2]
        self.secscore.setText(f"Security Score = {self.secs}")
        self.reputation.setText(f"Reputation = {self.rep}")
        self.budget.setText(f"Budget = {self.bud}")

        self.welcome.hide()
        self.inv.hide()
        self.invbt.hide()
        self.respond.hide()
        self.ignore.hide()
        self.change.show()

        if self.current_inc == 5:
            self.result.show()
        else:
            self.next.show()

    def nextin(self):
        self.current_inc += 1
        self.next.hide()
        self.tstatus = random.choice(threat)
        self.change.hide()

    def display_result(self):
        self.result.hide()
        self.exit.show()

        self.fscore = round((self.bud + self.rep + self.secs)/3)
        self.click.setText(f"Your final score is {self.fscore}")

        if self.fscore > 95:
            self.change.setText("Your rank is S+\nElite Defender")
        elif 90 < self.fscore <= 95:
            self.change.setText("Your rank is S\nThreat Master")
        elif 80 < self.fscore <= 90:
            self.change.setText("Your rank is A\nStrong Analyst")
        elif 70 < self.fscore <= 80:
            self.change.setText("Your rank is B\nReliable Operator")
        elif 60 < self.fscore <= 70:
            self.change.setText("Your rank is C\nAverage Analyst")
        elif 50 < self.fscore <= 60:
            self.change.setText("Your rank is D\nPoor Judgement")
        elif 40 < self.fscore <= 50:
            self.change.setText("Your rank is E\nSecurity Failure")
        elif 0 < self.fscore <= 40:
            self.change.setText("Your rank is F\nShit Failure")

    def display_rules(self):
        self.start.hide()
        self.rules.hide()
        self.exit.hide()
        self.welcome.hide()
        self.click.hide()
        self.inv.hide()
        self.back.show()
        self.rule.show()

    def get_back(self):
        self.start.show()
        self.rules.show()
        self.exit.show()
        self.welcome.show()
        self.click.show()
        self.inv.show()
        self.back.hide()
        self.rule.hide()
        self.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cyber_app = CyberApp()
    cyber_app.show()
    sys.exit(app.exec_())