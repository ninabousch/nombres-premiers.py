""" Module principal pour la verification et l'afficahge des nombres premiers"""
#isprime.py
### fonction secondaire
def isprime(p):
    """renvoie True si p vaut 1 ou 0 """
    e={0,1}
    if p in e:
        return False
    for i in range (2,p):
        if p%i==0:
            return False
    return True
#### Fonction principale
def main():
    """teste la fonction isprime """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
            print()
    if __name__ == "__main__":
        main()
