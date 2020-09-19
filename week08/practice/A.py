import sys
print(f"1.A, Module name {sys.modules.get('B')}")
print(f"2.A, class name {locals().get('D')}")
from B import D
print(f"1.A, Module name {sys.modules.get('B')}")
print(f"2.A, class name {locals().get('D')}")
print("A")
class C: pass

if __name__ == '__main__':
    c = C()
