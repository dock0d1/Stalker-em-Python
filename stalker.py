from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import getpass

set_workspace('/home/dock0d1/')

#crendenciais
insta_username = input("Usuário: ")
insta_password = getpass.getpass("Senha: ")

#iniciar sessão
session = Instapy(
	username=insta_username,
	password=insta_password,	
	headless_browser=False,
	want_check_browser=False
	)

comentarios = [
	u'@{} maravilhosa!!! :clap::clap::clap',
	u'amei :heart:'
]

with smart_run(session):
	#configuração
	session.set_comments(comentarios)
	session.set_do_comments(enabled=True,percentage=100)
	session.set_delimit_commenting(enabled=True, max_comments=10000, min_comments=0)
	session.set_do_like(enabled=True, percentage=100)

	#ação
	session.interact_by_users(['p.vitar'],amount=2,randomize=True,media='Photo')