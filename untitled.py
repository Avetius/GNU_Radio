#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy



from gnuradio import qtgui

class untitled(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "untitled")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0 = 0
        self.samp_rate = samp_rate = 20000000

        ##################################################
        # Blocks
        ##################################################
        _variable_qtgui_push_button_0_push_button = Qt.QPushButton('')
        _variable_qtgui_push_button_0_push_button = Qt.QPushButton('variable_qtgui_push_button_0')
        self._variable_qtgui_push_button_0_choices = {'Pressed': 1, 'Released': 0}
        _variable_qtgui_push_button_0_push_button.pressed.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Pressed']))
        _variable_qtgui_push_button_0_push_button.released.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Released']))
        self.top_layout.addWidget(_variable_qtgui_push_button_0_push_button)
        self.soapy_plutosdr_source_0 = None
        dev = 'driver=plutosdr'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_plutosdr_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_plutosdr_source_0.set_sample_rate(0, samp_rate)
        self.soapy_plutosdr_source_0.set_bandwidth(0, 4000000)
        self.soapy_plutosdr_source_0.set_gain_mode(0, False)
        self.soapy_plutosdr_source_0.set_frequency(0, 868000000)
        self.soapy_plutosdr_source_0.set_gain(0, min(max(70, 0.0), 73.0))
        self.soapy_plutosdr_source_0.set_min_output_buffer(4096)
        self.soapy_plutosdr_source_0.set_max_output_buffer(4096)
        self.soapy_plutosdr_sink_0 = None
        dev = 'driver=plutosdr'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_plutosdr_sink_0 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_plutosdr_sink_0.set_sample_rate(0, samp_rate)
        self.soapy_plutosdr_sink_0.set_bandwidth(0, 4000000)
        self.soapy_plutosdr_sink_0.set_frequency(0, 868000000)
        self.soapy_plutosdr_sink_0.set_gain(0, min(max(70, 0.0), 89.0))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.soapy_plutosdr_source_0, 0), (self.soapy_plutosdr_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "untitled")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_qtgui_push_button_0(self):
        return self.variable_qtgui_push_button_0

    def set_variable_qtgui_push_button_0(self, variable_qtgui_push_button_0):
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.soapy_plutosdr_sink_0.set_sample_rate(0, self.samp_rate)
        self.soapy_plutosdr_source_0.set_sample_rate(0, self.samp_rate)




def main(top_block_cls=untitled, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
