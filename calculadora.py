#!/usr/bin/python


import webapp


class calculadoraRest(webapp.webApp):

    def parse(self,request):
        try:
            peticion = request.split(' ')
            metodo = request.split(' ')[0]
            recurso = request.split(' ')[1].split('/')[1:]
            if metodo == "PUT":
                cuerpo = request.split('\r\n\r\n',1)[1]
            else:
                cuerpo = ""
        except:
            return None
        return (metodo, recurso, cuerpo)

    def process(self, parsedRequest):
        httpCode = ""
        htmlBody = ""
        resultado = ""
        if parsedRequest:
            (metodo, recurso, cuerpo) = parsedRequest
            print metodo, recurso, cuerpo
            if metodo == "PUT":
                self.operacion = cuerpo
                httpCode = "200 OK"
                htmlBody = "<html><body>" + cuerpo + "Ok</body></html>"
            elif metodo == "GET":
                try:
                    operacion = recurso[0]
                    operando1 = float(recurso[1])
                    operando2 = float(recurso[2])
                    if operacion == "sumar":
                        resultado = operando1 + operando2
                    elif operacion == "restar":
                        resultado = operando1 - operando2
                    elif operacion == "multiplicar":
                        resultado = operando1 * operando2
                    elif operacion == "dividir":
                        try:
                            resultado = operando1/operando2
                        except ZeroDivisionError:
                            resultado = "Imposible dividir entre 0"
                    else:
                        return ("404 Bad Request", "<html><body><h1>" +
                                "Operacion incorrecta</h1></body></html>") 
                except:
                    resultado = " Incorrecto. Introduce dos numeros"   
                httpCode = "200 OK"
                htmlBody = "<html><body><h1>Calculadora!</h1><p>Resultado: " + str(resultado) + "</p></body><html>"
        else:
            httpCode = "404 Bad Request"
            htmlbody = "<html><body><h1>Uso: /operacion/operando1/operando2</h1></body></html>"
        return (httpCode, htmlBody)

if __name__ == "__main__":
    testcalc = calculadoraRest("localhost", 1234)
