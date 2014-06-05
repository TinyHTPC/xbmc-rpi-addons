################################################################################
#      This file is part of TinyHomeTheatre PCs - http://www.tinyhtpc.co.nz
#      Copyright (C) 2014-2018 Josh Sunnex (josh@tinyhtpc.co.nz)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this software; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import os
import sys
import xbmcaddon
import time
import subprocess

__scriptname__ = "TinyHTPC PiPUB Switch"
__author__ = "TinyHTPC"
__url__ = "http://tinyhtpc.co.nz"
__settings__   = xbmcaddon.Addon(id='service.tinyhtpc.switch')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, 'bin', "switch.sh") )

#make binary files executable in adson bin folder
subprocess.Popen("chmod -R +x " + __cwd__ + "/bin/*" , shell=True, close_fds=True)

subprocess.Popen(__start__, shell=True, close_fds=True)

