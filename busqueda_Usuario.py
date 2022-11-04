from twarc import Twarc2, expansions
import json
import csv
import Autenticacion

# Replace your bearer token below
client = Twarc2(bearer_token=Autenticacion.Bearer_Token)


def tweets(usuario):
        user_timeline = client.timeline(user=usuario)
        for page in user_timeline:
            result = expansions.flatten(page)
            for tweet in result:
                guardar = json.dumps(tweet, indent=4)
                guardado = open("usuario1.json", "w")
                guardado.write(guardar)
                guardado.close()
                leer_tweets()
                Arreglo = leer_contexto()
                return Arreglo
            
            #with open('Prueba.csv','w', newline='') as file:
                #writer = csv.writer(file , delimiter=';')
                #writer.writerow(respuesta)
        
        


def leer_tweets():
    leer = open('usuario1.json', 'r')
    data = json.load(leer)
    leer.close()
    Trascribir(json.dumps(data['author'], indent=4))
    leer_user()


def Trascribir(parametro):
    save = open('usuario.json', 'w')
    save.write(parametro)
    save.close()


def leer_user():
    leer = open('usuario.json', 'r')
    data = json.load(leer)
    leer.close()
    Trascribir(json.dumps(data['public_metrics'], indent=4))


def leer_contexto():
    leer = open('usuario.json', 'r')
    data = json.load(leer)
    followers = data['followers_count']
    following = data['following_count']
    tweet = data['tweet_count']
    listed = data['listed_count']
    leer.close()
    Arreglos = [followers,following,tweet,listed]
    #Graficas(followers,following,tweet,listed)
    #print("Seguidores: ", followers, " Seguido: ",following, " tweets: ", tweet, " listed: ", listed)
    return Arreglos


