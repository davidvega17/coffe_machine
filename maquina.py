import math
class Maquina:
    def __init__(self, plata, agua, leche, cafe, vasos):
        self.plata = plata
        self.agua = agua 
        self.leche = leche
        self.coffe_beans = cafe
        self.vasos = vasos
        self.state = "s0"
    agua_esp = -250
    coffe_esp = -16
    valor_esp = 4
    leche_esp = 0

    agua_late = -350
    coffe_late = -20
    valor_late = 7
    leche_late = -75

    agua_cap = -200
    coffe_cap = -12
    valor_cap = 6
    leche_cap = -100

    def imprimir_estado(self):
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money""".format(self.agua, self.leche, self.coffe_beans, self.vasos, self.plata))

    def actualizar_insumos(self,n_agua, n_leche, n_coffe_beans, n_vasos):
        self.agua = self.agua + n_agua
        self.leche = self.leche + n_leche
        self.coffe_beans = self.coffe_beans + n_coffe_beans
        self.vasos = self.vasos + n_vasos
        
    def actualizar_dinero(self,n_dinero):
        self.plata = self.plata + n_dinero

    def verificar(self,tipo_cafe):
        
        if tipo_cafe == "late":
            agua_nes = Maquina.agua_late
            cafe_nes = Maquina.coffe_late
            leche_nes = Maquina.leche_late
            
        elif tipo_cafe == "cap":
            agua_nes = Maquina.agua_cap
            cafe_nes = Maquina.coffe_cap
            leche_nes = Maquina.leche_cap
            
        elif tipo_cafe == "esp":
            agua_nes = Maquina.agua_esp
            cafe_nes = Maquina.coffe_esp
            leche_nes = Maquina.leche_esp
        
        if self.agua + agua_nes < 0:
            # print("water")
            return "water"
        
        if self.leche + leche_nes < 0:
            # print("milk")
            return "milk"
        
        if self.coffe_beans + cafe_nes < 0:
            # print("coffe")
            return "coffee beans"
        
        if self.vasos < 1:
            # print("vasos")
            return "disposable cups"
        
        return "se puede"

    def vender(self,cafe_venta):
        if cafe_venta == "1":
            ver = self.verificar("esp")
            if (ver == "se puede"):
                self.actualizar_insumos(Maquina.agua_esp, Maquina.leche_esp, Maquina.coffe_esp, -1)
                self.actualizar_dinero(Maquina.valor_esp)
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough {}!".format(ver))
        elif cafe_venta == "2":
            ver = self.verificar("late")
            if (ver == "se puede"):
                self.actualizar_insumos(Maquina.agua_late, Maquina.leche_late, Maquina.coffe_late, -1)
                self.actualizar_dinero(Maquina.valor_late)
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough {}!".format(ver))
            
        elif cafe_venta == "3":
            ver = self.verificar("cap")
            if (ver == "se puede"):
                self.actualizar_insumos(Maquina.agua_cap, Maquina.leche_cap, Maquina.coffe_cap, -1)
                self.actualizar_dinero(Maquina.valor_cap)
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough {}!".format(ver))
            
        elif cafe_venta == "back":
            pass
    
    def run(self, string):
        if self.state == "s0":
            if string == "exit":
                exit()
            elif string == "take":
                #print("dar el billelle")
                print("I gave you ${}".format(self.plata))
                self.actualizar_dinero(-int(self.plata))
                self.state = "s0"
            elif string == "remaining":
                #print("resources")
                self.imprimir_estado()
                self.state = "s0"
            else:
                self.state = string
        elif self.state == "buy":
            #print("vender")
            self.vender(string)
            self.state = "s0"
        elif self.state == "fill":
            self.agua += int(string)
            #print("actualizar primer recurso")
            self.state = "fill2"
        elif self.state == "fill2":
            self.leche += int(string)
            #print ("actualizar recurso 2")
            self.state = "fill3"
        elif self.state == "fill3":
            #print("actualizar recurso 3")
            self.coffe_beans += int(string)
            self.state = "fill4"
        elif self.state == "fill4":
            #print("actualizar recurso 4")
            self.state = "s0"
            self.vasos += int(string)


maquina = Maquina(550, 400, 540, 120, 9)
while True:
    maquina.run(input())
    