#!/usr/bin/python2.7
import sys
import os

from cmdrunner import _run_command
from tvtlaunch_mw import Ui_tvtimelaunch
from PyQt4 import QtCore, QtGui

import subprocess, threading


class TVTimeRunner(QtCore.QThread):

    def __init__(self, thread_name, finished_slot, function,
                 *args, **kwargs):
        QtCore.QThread.__init__(self)

        self._thread_name = thread_name
        self._function = function
        self._args = args
        self._kwargs = kwargs

        self._finished_slot = finished_slot

    def __del__(self):
        self.exit()
        self.wait()

    def run(self):
        self._function(*self._args, **self._kwargs)

        self._finished_slot()


class StartTVTLaunch(QtGui.QMainWindow):
    _tvt_pid = -1
    _tvtime_launch_cmd = ''
    _wide = False

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_tvtimelaunch()
        self.ui.setupUi(self)
        self.ui.btnLaunch.clicked.connect(
            self._launch_tvtime)
        self.ui.btnKill.clicked.connect(
            self._kill_tvtime)
        self.ui.btnRefresh.clicked.connect(
            self._refresh)
        self.ui.chkAspect.clicked.connect(
            self._toggle_aspect)
        self.ui.btnReloadUsbtv.clicked.connect(
            self._reload_usbtv)
        self.ui.btnListen.clicked.connect(
            self._toggle_mic_listening)
        self._act_on_mic_listening = False
        self._init()

    def _enable_mic_listening(self):
        if self.ui.chbMagic.isChecked():
            cmd = 'pactl load-module module-remap-sink'
            cmd += ' sink_name=reverse-stereo master=0 channels=2'
            cmd += ' master_channel_map=front-right,front-left '
            cmd += 'channel_map=front-left,front-right'
            self._run_command(cmd)
            cmd = 'pactl load-module module-loopback sink=1'
        else:
            cmd = 'pactl load-module module-loopback'
        _run_command(self, cmd)

    def _disable_mic_listening(self):
        cmd = 'pactl unload-module module-loopback'
        _run_command(self, cmd)

    def _is_listening(self):
        cmd = 'pactl list modules | awk \'/Name/ {print $2}\''
        return 'module-loopback' in _run_command(self, cmd, split=True)

    def _toggle_mic_listening(self, start_up=False):
        if self._is_listening():
            if start_up:
                self.ui.btnListen.setText('Disable')
            else:
                self._disable_mic_listening()
                self.ui.btnListen.setText('Enable')
        else:
            self._enable_mic_listening()
            self.ui.btnListen.setText('Disable')

    def _get_pid(self):
        if self._tvtime_launch_cmd != '':
            cmd = "ps aux | grep -m1 '%s'" \
                  "| awk 'ORS=\"\"; {print $2}'" % self._tvtime_launch_cmd
            pid = _run_command(self, cmd, split=True)[0]
        else:
            pid = -1
        return pid

    def _search_for_term(self):
        cmd = '/usr/bin/ls /usr/bin/*term* | sort | tail -n -1'
        return _run_command(self, cmd)

    def _refresh(self):
        self.ui.cmbDevice.setDisabled(False)
        self.ui.btnLaunch.setDisabled(False)
        for _dev_item in range(self.ui.cmbDevice.count()):
            self.ui.cmbDevice.removeItem(0)
        for _mode_item in range(self.ui.cmbRegion.count()):
            self.ui.cmbRegion.removeItem(0)
        self._init()

    def _init(self):
        # Populate the devices combobox
        cmd = "/usr/bin/ls /dev/video* | " \
              "sort -r | awk '{print $1}'"
        _devices = _run_command(self, cmd, split=True)
        for _dev in _devices:
            if _dev[:11] == '/usr/bin/ls':
                _dev = '(None)'
                self.ui.cmbDevice.setDisabled(True)
                self.ui.btnLaunch.setDisabled(True)
            self.ui.cmbDevice.addItem(_dev)
        # Populate the region modes listview
        cmd = "tvtime -h 2>&1 | grep -A2 norm " \
              "| tail -n +2 | sed 's/,\|or/\\n/g' " \
              "| awk '/NTSC|PAL|SECAM/ {print $1}'"
        _modes = _run_command(self, cmd, split=True)
        for _mode in _modes:
            self.ui.cmbRegion.addItem(_mode)

        #self._toggle_mic_listening(start_up=True)

    def _launch_tvtime(self):
        _dev = self.ui.cmbDevice.currentText()
        _mode = self.ui.cmbRegion.currentText()
        _wide = self.ui.chkAspect.isChecked()
        if _wide:
            _aspect = '-a'
        else:
            _aspect = '-A'

        self._tvtime_launch_cmd = "tvtime --device={dev}" \
              " --norm={mode} {aspect}".format(
            dev=_dev,
            mode=_mode,
            aspect=_aspect
        )
        cmd = '{} &'.format(self._tvtime_launch_cmd)
        os.system(cmd)
        self.toggle_btns()

    def _kill_tvtime(self):
        pid = self._get_pid()
        print('PID IS {}'.format(pid))
        if pid and pid > 0:
            cmd = 'kill -9 {}'.format(pid)
            _run_command(self, cmd)
            self.toggle_btns()
        else:
            print('ERROR: pid is {}'.format(pid))

    def toggle_btns(self):
        launch_enabled = self.ui.btnLaunch.isEnabled()
        self.ui.btnKill.setDisabled(not launch_enabled)
        self.ui.btnLaunch.setDisabled(launch_enabled)

    def _toggle_aspect(self):
        self._wide = not self._wide
        if self._wide:
            self.ui.lbAspect.setText('16:9')
        else:
            self.ui.lbAspect.setText('4:3')
        pass

    def _reload_usbtv(self):
        cmd = 'pkexec $(pwd)/usbtvreload'
        print('reload module')
        self._run_command(cmd)

    def _start_pml(self):
        cmd = 'pmlistener'
        print('launch pml')
        _run_command(self, cmd, wait=False)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tvtimela = StartTVTLaunch()
    tvtimela.show()
    sys.exit(app.exec_())
