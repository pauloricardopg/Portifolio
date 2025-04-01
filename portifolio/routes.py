from flask import Flask, render_template, url_for, request, redirect, flash, abort
from portifolio import app, mail
from flask_mail import Message
from portifolio.forms import FormContato

@app.route('/', methods=['GET', 'POST'])
def home():
    form_contato = FormContato()
    form_contato = FormContato()

    if form_contato.validate_on_submit():
        nome = form_contato.username.data
        email = form_contato.email.data
        mensagem = form_contato.corpo.data

        # Montando o e-mail
        msg = Message(
            subject=f'Novo contato de {nome}',
            sender=app.config['MAIL_USERNAME'],
            recipients=['pauloricardo1705@gmail.com'],  # Para onde vai o e-mail
            body=f'''
            Você recebeu uma nova mensagem pelo site:

            Nome: {nome}
            Email: {email}
            Mensagem:
            {mensagem}
            '''
                    )

        # Envia o e-mail
        mail.send(msg)
        flash('Mensagem enviada com sucesso!', 'alert-success')
        return redirect(url_for('home'))     # ou outra rota de sucesso
    return render_template('home.html', form_contato=form_contato)