def html_message(message_type, url, first_name, token):
    if message_type == "reset":
        message_html = """\
            <html>
                <head></head>
                <body style="background-color: #e4525a;">
                    <div style="background-color: #fff;">
                    <div style="margin: 5em;">
                        <div style="color: #fff">
                            <h1 style="color: #111">Olá, {}!</h1>
                            <h3 style="color: #111;">Recebemos seu pedido de redefinição de senha!</h3>
                                <h4 style="color: #111;">Clique no link abaixo para prosseguir:</h4>
                                <a href="{}forgot/password?token={}">Link para nova senha</a><br>
                                Caso não tenha sido você quem pediu, desconsidere esse e-mail.
                        </div>
                    </div>
                </body>
            </html>""".format(first_name, url, token)
    if message_type == "register":
        message_html = """\
            <html>
                <head></head>
                <body style="background-color: #e4525a;">
                    <div style="background-color: #fff;">
                    <div style="margin: 5em;">
                        <div style="color: #fff">
                            <h1 style="color: #111">Olá, {}!</h1>
                            <h3 style="color: #111;">Seja bem vindo ao Ifound! Antes de continuar, você ainda precisa confirmar a sua conta.</h3>
                            <h4 style="color: #111;">Clique no link abaixo para prosseguir:</h4>
                            <a href="{}user/confirm?token={}">Confirme sua conta</a><br>
                        </div>
                    </div>
                </body>
            </html>""".format(first_name, url, token)        
    return message_html