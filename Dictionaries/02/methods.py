

def main():
    sal_info = {'Austin': 87236, 'Boston': 98854,
                'San Jose': 98578, 'Atlanta': 87549}

    print(sal_info.get("Austin", "Not found"))
    print(sal_info.keys())
    print(sal_info.values())

    # # # loop through items
    for k, v in sal_info.items():
        print(f"The key is {k} and the value is {v}")

    # # # the key for the highest value in the dictionary
    print(f"City with highest salary {max(sal_info, key=sal_info.get)}")
    print(f"City with highest salary {min(sal_info, key=sal_info.get)}")

    # # # sort the values
    print(sal_info)
    print(sorted(sal_info.keys()))
    print(sorted(sal_info.values()))


if __name__ == "__main__":
    main()
