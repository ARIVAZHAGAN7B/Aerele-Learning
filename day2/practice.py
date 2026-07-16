from typing import Literal, List

def sum(a:Literal[10,20]):
    return a + 10  #Literal just a decorator not restrict the values



if __name__ == "__main__":
    print(sum(10))  # Output: 20
    print(sum(20))  # Output: 30
    # print(sum(30))  # This will raise a type error if type checking is enforced
    