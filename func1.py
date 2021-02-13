def favorite_book(book):
    print(f"One of my favorite books is '{book}'.")

def make_shirt(size = 'L', text = "I love Python."):
    print(f"Make t-shirt, size '{size}' and text '{text}'")

def describe_city(city, country = 'Russia'):
    print(f"{city} is in {country}")

def main():
#    book = input("Type the name of the book you like: ")
#    favorite_book(book)
#    make_shirt( size = 'L', text = 'I love footboll')
    city_country = {'london': 'england', 'rome': 'italia', "moscow": "russia"}
    for city, country in city_country.items():
        print(f"{city.capitalize()}, {country.capitalize()}")
    
if __name__ == '__main__':
    main()