import json, os, sys, random, time
from requests import get

def random_ua():
	with open('uafile', 'rb') as uaf:
		ua = random.choice(uaf.readlines())
	return ua.strip()[1:-1-1]

def visit_ml():
	headers = {'User-Agent': random_ua()}
	get('http://produto.mercadolivre.com.br/******', headers=headers)

def main():
	x=1
	while True:
		visit_ml()
		print '[+]', str(x), 'visited! waiting...';x+=1
		time.sleep(float(str(random.randrange(5,10))+'.'+str(random.randrange(90))))

if __name__ == '__main__':
	os.system('clear')
	main()
