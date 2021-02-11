def make_sandwich(*components: str):
    print(f"List of components of your sandwich: {', '.join(i for i in components)}.")

make_sandwich("колбаса", "паштет", "огурец")