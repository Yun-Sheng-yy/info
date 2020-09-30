def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('HUAWEI-jj', 'zxcvbnm1')
        while not sta_if.isconnected():
            pass
    import machine as m
    led=m.Pin(2,m.Pin.OUT)
    led.value(1)
    led.value(0)
    print('network config:', sta_if.ifconfig())
