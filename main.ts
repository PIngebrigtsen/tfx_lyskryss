function B_grønn_A_Rød () {
    LysgruppeA_grønn_rød()
    basic.pause(500)
    LysgruppeB_rød_grønn()
    A = 1
    B = 0
}
function A_grønn_B_Rød () {
    LysgruppeB_grønn_rød()
    basic.pause(500)
    LysgruppeA_rød_grønn()
    A = 1
    B = 0
}
input.onButtonPressed(Button.A, function () {
    KnappAIsPressed = 1
})
function LysgruppeB_rød_grønn () {
    pins.digitalWritePin(DigitalPin.P4, 1)
    pins.digitalWritePin(DigitalPin.P5, 1)
    pins.digitalWritePin(DigitalPin.P6, 0)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P4, 0)
    pins.digitalWritePin(DigitalPin.P5, 0)
    pins.digitalWritePin(DigitalPin.P6, 1)
}
function LysgruppeA_rød_grønn () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
}
input.onButtonPressed(Button.B, function () {
    KnappBIsPressed = 1
})
function LysgruppeB_grønn_rød () {
    pins.digitalWritePin(DigitalPin.P4, 0)
    pins.digitalWritePin(DigitalPin.P5, 1)
    pins.digitalWritePin(DigitalPin.P6, 0)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P4, 1)
    pins.digitalWritePin(DigitalPin.P5, 0)
    pins.digitalWritePin(DigitalPin.P6, 0)
}
function LysgruppeA_grønn_rød () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
let KnappBIsPressed = 0
let KnappAIsPressed = 0
let B = 0
let A = 0
led.enable(false)
let timer = input.runningTime()
A = 1
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 1)
pins.digitalWritePin(DigitalPin.P4, 1)
pins.digitalWritePin(DigitalPin.P5, 0)
pins.digitalWritePin(DigitalPin.P6, 0)
basic.forever(function () {
    if (KnappAIsPressed == 1 || KnappBIsPressed == 1) {
        while (input.runningTime() - timer <= 10000) {
        	
        }
        if (A == 1) {
            LysgruppeA_grønn_rød()
        } else {
            LysgruppeB_grønn_rød()
        }
        if (KnappAIsPressed == 1) {
            pins.digitalWritePin(DigitalPin.P8, 1)
            KnappAIsPressed = 0
        }
        if (KnappBIsPressed == 1) {
            pins.digitalWritePin(DigitalPin.P8, 1)
            KnappBIsPressed = 0
        }
        basic.pause(10000)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P9, 0)
        if (A == 1) {
            LysgruppeB_rød_grønn()
        } else {
            LysgruppeA_rød_grønn()
        }
    }
    if (input.runningTime() - timer >= 45000) {
        if (A == 1) {
            B_grønn_A_Rød()
        } else {
            A_grønn_B_Rød()
        }
        timer = input.runningTime()
    }
})
