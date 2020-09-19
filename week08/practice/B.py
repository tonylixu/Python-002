import sys
print(f"1.B, Module name {sys.modules.get('A')}")
print(f"2.B, class name {locals().get('C')}")
from C import X
from A import C
print(f"1.B, Module name {sys.modules.get('A')}")
print(f"2.B, class name {locals().get('C')}")
print("A")
class D: pass

if __name__ == '__main__':
    d = D()
