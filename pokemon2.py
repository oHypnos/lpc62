import requests
def get_pokmeons (url="https://pokeapi.co/api/v2/pokemon-form/")
	args = {"offset":offset} if offset else{}

	response = requests.get(url, params=args)

	if response.status_code == 200:
		payload = response.json()
		results = payload.get("results",[])

		if results:
			for pokemon in results:
				name = pokemon["name"]
				print(name)
		next = input("¿Continuar listando? [Y/N]").lower()
		if next == "y":
			get_pokemons(offset=offset+20)
if __name__=="__main__":
	url = "https://pokeapi.co/api/v2/pokemon-form/"
	get_pokemons()
#Script en python que consulta el api de pokemon
#Para listar los nombres de pokemon pero se le agrego
#Interaccion para que listaras mas pokemon segun se vaya requiriendo.
#Contribuyu: Fernando Javier Marin Salas
#Fecha: 19/02/2023
