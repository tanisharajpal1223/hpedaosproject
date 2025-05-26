import subprocess



def main():
    print("=== DAOS Automation Script ===")

    # 1. Query system
    run_cmd("dmg system query -v", "Querying DAOS system status")

    # 2. Query storage usage
    run_cmd("dmg storage query usage", "Checking DAOS storage usage")

    # 3. Create pool
    run_cmd("dmg pool create --size=1G test_pool", "Creating 1G DAOS pool")

    # 4. Query pool
    run_cmd("dmg pool query test_pool", "Querying pool info")

if __name__ == "__main__":
    main()
