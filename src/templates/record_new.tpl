<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><!--

############################################################
Time Web - Record New
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/08
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
-->
<html>
    <head>
        <meta charset="iso-8859-1">
        <title>Novo Registro</title>
        <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <form action="save" id="cadastro" name="Cadastro" method="post">
                <ul>
                        <li>
                                Nome do objeto:</li>
                </ul>
                <p style="margin-left: 40px;">
                        ​<input name="name" size="80" type="text"/></p>
                <ul>
                        <li>
                                Código de rastreio:</li>
                </ul>
                <p style="margin-left: 40px;">
                        ​<input name="code" size="80" type="text"/></p>
                 <p style="margin-left: 40px;">
                        ​<input name="enviar" type="submit"/></p>
       </form>
    </body>
</html>
