### Type Casting is manual type conversion
### Type Coercion is implicit type conversion

### Pyhton is strongly typed, it means some operation on different data types are restricted
### JS is loosely typed

a=99999999999999999999999999999
a=a**3
print(a," Type -> ",type(a))
a=5.5
print(a," Type -> ",type(a))
a=4+2j
print(a," Type -> ",type(a))

a=int(6.99999)
print(a," Type -> ",type(a))

a=float(6)
print(a," Type -> ",type(a))


a='abc123***'
print(a," Type -> ",type(a))

a="sdfrgdfrgvdfg"
print(a," Type -> ",type(a))

a='''
    abc
    abc
  '''
print(a," Type -> ",type(a))

print(a[0]," Type -> ",type(a))

a=a.upper()
print(a," Type -> ",type(a))