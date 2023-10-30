# # # python advanced dictionaries
"""
    dictionary hold data in pairs of key value pairs and is mutable.
    This makes it possible to edi a dictionary once created unlike tupples

    keys are independent while values are dependent
    example === {"one":1, "two":2, "three":3}
"""

# creating dictionary
sal_info = {
    'Austin': 9118, 'Boston': 90171
}

print(sal_info)

# change the value of boston
print("updating the Boston value")
sal_info['Boston'] = 98456
print(sal_info)

# add new item
print("adding LA")
sal_info['LA'] = 78986
print(sal_info)

# delete an item
print("Deleting LA")
del sal_info['LA']
print(sal_info)

# clear all the values
print("flushing the dictionary")
sal_info.clear()
print(len(sal_info))
print(sal_info)
