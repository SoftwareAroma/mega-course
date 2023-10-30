sal_info = dict()

print(f"original dictionary: {sal_info}")

sal_info = {'Austin': 87236, 'Boston': 98854, 'San Jose': 98578, 'Atlanta': 87549}

info = {'Austin': 87236, 'Boston': 98854, 'San Jose': 98578, 'Atlanta': 87549}

print(f"updated dictionary: {sal_info}")

# for k, v,n,m in sal_info.items(), info.items():
#     print(f"The key '{k}' has a value of '{v}'.")
#     print(f"The key '{n}' has a value of '{m}'.")

for k, v in sal_info.items():
    print(f"The key '{k}' has a value of '{v}'.")
    