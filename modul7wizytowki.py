class Card:
   def __init__(self,name, surname, business, position, email):
       self.name = name
       self.surname = surname
       self.business = business
       self.position = position
       self.email = email

     
   def __str__(self) -> str:
      return (self.name +" " +self.surname+" "+self.email)
     
   def contact(self):
      print("Kontaktuję się z "+self.name +" " +self.surname+" "+self.email)
   
   @property
   def label_lenght(self):
        return  len(self.name)+ 1 +len(self.surname)
   
class BaseContact(Card):
   def __init__(self, phone, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.phone = phone 

   @property
   def label_lenght(self):
        return  len(self.name)+ 1 +len(self.surname)
   
   def contact_base(self):
      print("Wybieram numer "+self.phone +" dzwonie do " +self.name+" "+self.surname)

class BusinessContact(Card):
   def __init__(self, business_phone, company,*args, **kwargs):
       super().__init__(*args, **kwargs)
       self.business_phone = business_phone
       self.company = company

   def contact_business(self):
      print("Wybieram numer "+self.business_phone +" dzwonie do " +self.name+" "+self.surname)

   @property
   def label_lenght(self):
        return  len(self.name)+ 1 +len(self.surname)
cards = [
   Card("Sebastian","Kowal","Warsztat","Mechanik","blabla@jolo"),
   Card("Olek","Nowak","Niewiem","blabla","olek222@gmail.com"),
   Card("Ania","Kowalska","sekretarka","Biuro","aniaania@wp.pl"),
   Card("Marek","Adamski","sprzedawca","sklep","marek888@onet.pl"),
   Card("Basia","Pach","nauczycielka","przedszkole","basiabiasia@gmail.com")
  ]
card1 = Card("Sebastian","Kowal","Warsztat","Mechanik","blabla@jolo")
      
def display_cards(cards):
    for card in cards:
      #print(card.name +" " +card.surname+" "+card.email)
      print(card)

def create_contacts(Card):
    from faker import Faker
    fake = Faker()
    n=int((input("ile wizytówek?")))
    for _ in range(n):
     print(fake.name())
     print(fake.company())
     print(fake.email())



card1 = BaseContact(name="Sebastian",surname="Kowal",business="Warsztat",position="Mechanik",email="blabla@jolo",phone="1244444")       
#display_cards(cards)
card1.contact_base()
print(card1.label_lenght)
card2 = BusinessContact(name="Marek",surname="Adamski",business="sprzedawca",position="sklep",email="marek888@onet.pl",business_phone="605555121",company="ABC")   
card2.contact_business()
#display_cards(sorted(cards, key=lambda card:card.email))
print(card2.label_lenght)

print(create_contacts(BusinessContact))

                      


