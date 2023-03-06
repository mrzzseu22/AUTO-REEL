class Configure():

    def __init__(self):

        self.LIST_DEVICES = "adb devices"
        self.GET_DEVICES_NAME = "adb -s {0} shell getprop ro.product.model"
        self.ON_OFF_SCREEN = "adb -s {0} shell input keyevent 26"
        self.REBOOT = "adb -s {0} reboot"
        self.SHUTDOWN = "adb -s {0} shell reboot -p"
        self.SET_BRIGHNESS = "adb -s {0} shell settings put system screen_brightness {1}"
        self.OFF_AUTO_BRIGHNESS = "adb -s {0} shell settings put system screen_brightness_mode 0"
        self.DISABLE_ROTATE = "adb -s {0} shell wm set-user-rotation lock 0"
        self.SET_VOLUME = "adb -s {0} shell service call audio 10 i32 3 i32 {1}"
        self.AIRPLANE_MODE = "adb -s {0} shell su -c am broadcast -a android.intent.action.AIRPLANE_MODE"
        self.AIRPLANE_ON = "adb -s {0} shell su -c settings put global airplane_mode_on 1"
        self.AIRPLANE_OFF = "adb -s {0} shell su -c settings put global airplane_mode_on 0"
        self.TAP_DEVICES = "adb -s {0} shell input tap {1} {2}"
        self.SWIPE_DEVICES = "adb -s {0} shell input swipe {1} {2} {3} {4} {5}"
        self.KEY_DEVICES = "adb -s {0} shell input keyevent {1}"
        self.INPUT_TEXT_DEVICES = "adb -s {0} shell input text '{1}'"
        self.CAPTURE_SCREEN_TO_DEVICES = "adb -s {0} shell screencap -p /sdcard/screen_{0}.png"
        self.PULL_FILE_FROM_DEVICES = "adb -s {0} pull \"{1}\" {2}"
        self.PUSH_FILE_FROM_DEVICES = 'adb -s {0} push "{1}" "{2}"'
        self.REMOVE_FILEFROM_DEVICES = "adb -s {0} shell rm -rf {1}"
        self.GET_SCREEN_RESOLUTION = "adb -s {0} shell wm size"
        self.ADB_FOLDER_PATH = ""
        self.INSTALL_APP = 'adb -s {0} install "{1}"'
        self.UNINSTALL_APP = "adb -s {0} uninstall {1}"
        self.CLEAR_PACKAGE = "adb -s {0} shell pm clear {1}"
        self.GRANT = "adb -s {0} shell pm grant {1} {2}"
        self.OPEN_PACKAGE = "adb -s {0} shell monkey -p {1} -c android.intent.category.LAUNCHER 1"
        self.FORCE_STOP = "adb -s {0} shell am force-stop {1}"
        self.OPEN_DEEPLINK = 'adb -s {0} shell am start -a android.intent.action.VIEW -d fb://{1} {2}'
        self.CLEAR_CACHE = "adb -s {0} shell su -c rm -rf {1}cache*"
        self.MIRROIR = "scrcpy -s {0} --window-title {0} --max-size {1} --window-x {2} --window-y {3}"
        self.MIRROIR_OFF_SCREEN = "scrcpy -s {0} -S --window-title {0} --max-size {1} --window-x {2} --window-y {3}"
        self.SCAN_PIC = "adb -s {0} shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///mnt/{1}"