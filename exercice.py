#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number=-number
        return number
    else:
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    a=[]
    for c in prefixes:
     a.append(c + suffixe)
    return a



def prime_integer_summation() -> int:
    a = 0
    b = 0
    i = 2
    while b < 100 and i >= 2:
        for c in range(i-1, 0, -1):
            if i % c == 0:
                break
        if c == 1:
            a += i
            b += 1
        i += 1
    return a


def factorial(number: int) -> int:
    c=1
    for i in range (1, number+1, 1):
        c=c*i

    return c




def use_continue() -> None:
    for c in range(1,11,1):
        if c==5:
            continue
        else:
            print(c)





def verify_ages(groups: List[List[int]]) -> List[bool]:
  a=[]
  for i in range (1, len(groups)):
      for c in range (1, len(List)):
         if len(List)>10   or len(List)<3 :
             break
         elif c==25:
            a.append(List)
            break
         else:
            a.append(List)
  return a













def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
