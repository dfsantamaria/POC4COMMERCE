from OCCSE.QueryBuilderModule import *

q=Query([("Prefixnew","URL")], ["prova"], ["p1","p2"])
print(q.build())


q=QueryQF1()
print(q.build())

q=QueryQF2()
print(q.build())

q=QueryQF3([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQF4([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQF5([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQF6([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQF7([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())


#OC-Commerce default queries

q=QueryQC1()
print(q.build())

q=QueryQC2([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQC3()
print(q.build())

#OC-Ethereum default queries

q=QueryQE1()
print(q.build())

q=QueryQE2([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQE3([("Prefixnew","URL")], "Prefixnew:com")
print(q.build())

q=QueryQE4()
print(q.build())