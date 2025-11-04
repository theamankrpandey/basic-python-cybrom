fs1=({10,20,30,'python'})
fs2=({2,4,6,8,'java','python'})
print(fs2.issub(fs1))

fs1=frozenset({10,20,30,'python'})
fs2=frozenset({2,4,6,8,'java','python'})
print(fs2.issuperset(fs1))