def B_grønn_A_Rød():
    global A
    LysgruppeA_grønn_rød()
    basic.pause(Helrød_tid)
    LysgruppeB_rød_grønn()
    A = 1
def A_grønn_B_Rød():
    global A
    LysgruppeB_grønn_rød()
    basic.pause(Helrød_tid)
    LysgruppeA_rød_grønn()
    A = 1

def on_button_pressed_a():
    global KnappAIsPressed
    KnappAIsPressed = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def LysgruppeB_rød_grønn():
    pins.digital_write_pin(DigitalPin.P3, 1)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P6, 0)
    basic.pause(Rødgul_tid)
    pins.digital_write_pin(DigitalPin.P3, 0)
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P6, 1)
def LysgruppeA_rød_grønn():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(Rødgul_tid)
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)

def on_button_pressed_b():
    global KnappBIsPressed
    KnappBIsPressed = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def LysgruppeB_grønn_rød():
    pins.digital_write_pin(DigitalPin.P3, 0)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P6, 0)
    basic.pause(Gultid)
    pins.digital_write_pin(DigitalPin.P3, 1)
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P6, 0)
def LysgruppeA_grønn_rød():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(Gultid)
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
KnappBIsPressed = 0
KnappAIsPressed = 0
Rødgul_tid = 0
Gultid = 0
Helrød_tid = 0
A = 0
led.enable(False)
timer = input.running_time()
A = 1
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)
pins.digital_write_pin(DigitalPin.P2, 1)
pins.digital_write_pin(DigitalPin.P3, 1)
pins.digital_write_pin(DigitalPin.P4, 0)
pins.digital_write_pin(DigitalPin.P6, 0)
Helrød_tid = 500
Gultid = 1000
Rødgul_tid = 1000
Grønntid_fotgjenger = 10000
Grønntid_max = 45000
Grønntid_min = 15000
"""

# P0=A rød

"""
"""

# P1=A Gul

"""
"""

# P2=A Grønn

"""
"""

# P3=B Rød

"""
"""

# P4=B Gul

"""
"""

# P5=Knapp A

"""
"""

# P6=B Rød

"""
"""

# P7= A Fotgjenger Grønn

"""
"""

# P8= A Fotgjenger Rød

"""
"""

# P9= B Fotgjenger Grønn

"""
"""

# P10= B Fotgjenger Rød

"""
"""

# P11=KnappB

"""

def on_forever():
    global KnappAIsPressed, KnappBIsPressed, timer
    if KnappAIsPressed == 1 or KnappBIsPressed == 1:
        while input.running_time() - timer <= Grønntid_min:
            pass
        if A == 1:
            LysgruppeA_grønn_rød()
        else:
            LysgruppeB_grønn_rød()
        if KnappAIsPressed == 1:
            pins.digital_write_pin(DigitalPin.P7, 1)
            KnappAIsPressed = 0
        if KnappBIsPressed == 1:
            pins.digital_write_pin(DigitalPin.P8, 1)
            KnappBIsPressed = 0
        basic.pause(Grønntid_fotgjenger)
        pins.digital_write_pin(DigitalPin.P7, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        if A == 1:
            LysgruppeB_rød_grønn()
        else:
            LysgruppeA_rød_grønn()
    if input.running_time() - timer >= Grønntid_max:
        if A == 1:
            B_grønn_A_Rød()
        else:
            A_grønn_B_Rød()
        timer = input.running_time()
basic.forever(on_forever)
