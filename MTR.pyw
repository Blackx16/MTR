#upadted version of code (used OOP)
import schedule
import time
import webbrowser
import pyttsx3

class ClassScheduler:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  # Set speaking speed
        self.setup_voice()
        self.classes = self.create_schedule()

    def setup_voice(self):
        voices = self.engine.getProperty('voices')
        # Uncomment the following line to set a female voice
        # self.engine.setProperty('voice', voices[1].id)
        self.engine.runAndWait()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def create_schedule(self):
        classes = {
            "eco": {
                "message": "It's Economics class now",
                "url": "https://us04web.zoom.us/j/79814235033?pwd=U014K0l4Z1ZhcjN1OWk0OEsxajNjQT09"
            },
            "eng": {
                "message": "It's English class now!!",
                "url": "https://us05web.zoom.us/j/9719627196?pwd=OVV5Y09nempaN3lGL0NVRzJiSHgwdz09"
            },
            "BS": {
                "message": "It's Business Studies class now!!",
                "url": "https://us04web.zoom.us/j/4711097803?pwd=TWkvVERmZkRsSU1yQ0VmOXAyaVJQUT09"
            },
            "ac": {
                "message": "It's Accounts class now!!",
                "url": "https://us04web.zoom.us/j/3158952513?pwd=bllXYW5UK1I2TysvRGc5cUhGbUwwZz09"
            },
            "comp": {
                "message": "It's Computer class now",
                "url": "https://us04web.zoom.us/j/6366119606?pwd=VFlORUdDOVB0b0p1OU9TZS9SakZLZz09"
            },
            "assembly": {
                "message": "It's assembly Time, Bro",
                "url": "https://us04web.zoom.us/j/3321067982?pwd=MitCaTV4R3VpV1VtZ0JabkhDQ2o2Zz09"
            },
            "ss": {
                "message": "THIS IS YOUR SELF STUDY PERIOD!! BRO!!! AND YOU HAVE TO DO THE SAME!!! PLEASE BRO!!!",
                "url": None
            }
        }
        return classes

    def schedule_classes(self):
        # Schedule each class
        self.schedule_daily("08:40", "assembly")
        self.schedule_weekly("monday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["eng", "BS", "comp", "eco", "eco"])
        self.schedule_weekly("tuesday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["comp", "BS", "eco", "ac", "ac"])
        self.schedule_weekly("wednesday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["eng", "eco", "ac", "ss", "ss"])
        self.schedule_weekly("thursday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["eng", "BS", "ss", "eco", "eco"])
        self.schedule_weekly("friday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["comp", "comp", "ac", "BS", "ac"])
        self.schedule_weekly("saturday", ["09:00", "09:45", "10:30", "11:20", "12:05"], ["eng", "BS", "ac", "BS", "eng"])

    def schedule_daily(self, time_str, class_name):
        schedule.every().day.at(time_str).do(self.start_class, class_name)

    def schedule_weekly(self, day, times, classes):
        for time_str, class_name in zip(times, classes):
            getattr(schedule.every(), day).at(time_str).do(self.start_class, class_name)

    def start_class(self, class_name):
        class_info = self.classes[class_name]
        self.speak(class_info["message"])
        if class_info["url"]:
            webbrowser.open_new_tab(class_info["url"])

    def run(self):
        self.schedule_classes()
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    scheduler = ClassScheduler()
    scheduler.run()
