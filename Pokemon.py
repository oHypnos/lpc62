import request
#Fernando Javier Marin Salas
#Matricula: 1679139

def get_pokemnos (url="https://pokeapi.co/api/v2/pokemon-form/"
	args = {"offset":offset} if offset else {}
	response = request.get(url, params=args)

	if response.status_code == 200:
		payload = response.json()
		results = payload.get("results",[])
		if results:
			for pokemon in results:
				name = pokemon["name"]
				print(name)
		next = input("¿Continuar listando [Y/N]").lower()
		if next == "y":
			get_pokemons(offset=offset+20)
if __name__=="__main__":
	url = "https://pokeapi.co/api/v2/pokemon-form/"
	get_pokemons()
