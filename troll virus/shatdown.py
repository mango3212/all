from keyboard import is_pressed as _
from subprocess import run as d

while True:
    if _("esc"):
        d(['shutdown', '-s','-t','0'])
