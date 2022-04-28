input.onButtonPressed(Button.A, function () {
    KnappAIsPressed = 1
})
function LysgruppeB_rød_grønn () {
    pins.digitalWritePin(DigitalPin.P3, 1)
    pins.digitalWritePin(DigitalPin.P4, 1)
    pins.digitalWritePin(DigitalPin.P6, 0)
    basic.pause(Rødgul_tid)
    pins.digitalWritePin(DigitalPin.P3, 0)
    pins.digitalWritePin(DigitalPin.P4, 0)
    pins.digitalWritePin(DigitalPin.P6, 1)
    A = 0
}
function LysgruppeA_rød_grønn () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(Rødgul_tid)
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
    A = 1
}
input.onButtonPressed(Button.B, function () {
    KnappBIsPressed = 1
})
function LysgruppeB_grønn_rød () {
    pins.digitalWritePin(DigitalPin.P3, 0)
    pins.digitalWritePin(DigitalPin.P4, 1)
    pins.digitalWritePin(DigitalPin.P6, 0)
    basic.pause(Gultid)
    pins.digitalWritePin(DigitalPin.P3, 1)
    pins.digitalWritePin(DigitalPin.P4, 0)
    pins.digitalWritePin(DigitalPin.P6, 0)
}
function LysgruppeA_grønn_rød () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(Gultid)
    pins.digitalWritePin(DigitalPin.P0, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
}
// P0= A rød
// P1= A Gul
// P2= A Grønn
// P3= B Rød
// P4= B Gul
// P5= Knapp A
// P6= B Rød
// P7= A Fotgjenger Grønn
// P8= A Fotgjenger Rød
// P9= B Fotgjenger Grønn
// P10= B Fotgjenger Rød
// P11= Knapp B
let KnappBIsPressed = 0
let KnappAIsPressed = 0
let A = 0
let Rødgul_tid = 0
let Gultid = 0
let Helrød_tid = 500
Gultid = 1000
Rødgul_tid = 1000
let Grønntid_fotgjenger = 10000
let Grønntid_max = 45000
let Grønntid_min = 15000
led.enable(false)
let t = input.runningTime()
A = 1
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 1)
pins.digitalWritePin(DigitalPin.P3, 1)
pins.digitalWritePin(DigitalPin.P4, 0)
pins.digitalWritePin(DigitalPin.P6, 0)
pins.digitalWritePin(DigitalPin.P7, 0)
pins.digitalWritePin(DigitalPin.P8, 1)
pins.digitalWritePin(DigitalPin.P9, 0)
pins.digitalWritePin(DigitalPin.P10, 1)
basic.forever(function () {
    if (KnappAIsPressed == 1 || KnappBIsPressed == 1) {
        while (input.runningTime() - t < Grønntid_min) {
        	
        }
        if (A == 1) {
            LysgruppeA_grønn_rød()
        } else {
            LysgruppeB_grønn_rød()
        }
        if (KnappAIsPressed == 1) {
            pins.digitalWritePin(DigitalPin.P7, 1)
            KnappAIsPressed = 0
        }
        if (KnappBIsPressed == 1) {
            pins.digitalWritePin(DigitalPin.P9, 1)
            KnappBIsPressed = 0
        }
        basic.pause(Grønntid_fotgjenger)
        pins.digitalWritePin(DigitalPin.P7, 0)
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P9, 0)
        pins.digitalWritePin(DigitalPin.P10, 1)
        if (A == 1) {
            LysgruppeB_rød_grønn()
        } else {
            LysgruppeA_rød_grønn()
        }
        t = input.runningTime()
    }
    if (input.runningTime() - t >= Grønntid_max) {
        if (A == 1) {
            LysgruppeA_grønn_rød()
            basic.pause(Helrød_tid)
            LysgruppeB_rød_grønn()
        } else {
            LysgruppeB_grønn_rød()
            basic.pause(Helrød_tid)
            LysgruppeA_rød_grønn()
        }
        t = input.runningTime()
    }
})
