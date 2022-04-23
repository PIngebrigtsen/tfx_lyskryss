def B_grønn_A_Rød():
    global A, B
    LysgruppeA_grønn_rød()
    basic.pause(500)
    LysgruppeB_rød_grønn()
    A = 1
    B = 0
def A_grønn_B_Rød():
    global A, B
    LysgruppeB_grønn_rød()
    basic.pause(500)
    LysgruppeA_rød_grønn()
    A = 1
    B = 0

def on_button_pressed_a():
    global KnappAIsPressed
    KnappAIsPressed = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def LysgruppeB_rød_grønn():
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P6, 0)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 1)
def LysgruppeA_rød_grønn():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)

def on_button_pressed_b():
    global KnappBIsPressed
    KnappBIsPressed = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def LysgruppeB_grønn_rød():
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P6, 0)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 0)
def LysgruppeA_grønn_rød():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
KnappBIsPressed = 0
KnappAIsPressed = 0
B = 0
A = 0
led.enable(False)
timer = input.running_time()
A = 1
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)
pins.digital_write_pin(DigitalPin.P2, 1)
pins.digital_write_pin(DigitalPin.P4, 1)
pins.digital_write_pin(DigitalPin.P5, 0)
pins.digital_write_pin(DigitalPin.P6, 0)

def on_forever():
    global KnappAIsPressed, KnappBIsPressed, timer
    if KnappAIsPressed == 1 or KnappBIsPressed == 1:
        while input.running_time() - timer <= 10000:
            pass
        if A == 1:
            LysgruppeA_grønn_rød()
        else:
            LysgruppeB_grønn_rød()
        if KnappAIsPressed == 1:
            pins.digital_write_pin(DigitalPin.P8, 1)
            KnappAIsPressed = 0
        if KnappBIsPressed == 1:
            pins.digital_write_pin(DigitalPin.P8, 1)
            KnappBIsPressed = 0
        basic.pause(10000)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        if A == 1:
            LysgruppeB_rød_grønn()
        else:
            LysgruppeA_rød_grønn()
    if input.running_time() - timer >= 45000:
        if A == 1:
            B_grønn_A_Rød()
        else:
            A_grønn_B_Rød()
        timer = input.running_time()
basic.forever(on_forever)
